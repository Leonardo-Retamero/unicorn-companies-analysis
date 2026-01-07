import pandas as pd 
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title='Dashboard - Empresas Unicórnio',
    page_icon='🦄',
    layout='wide'
)

df = pd.read_csv('startups_2021.csv')

st.markdown(
    "<h1 style='text-align: center;'>Companies Achieving Unicorn Status ($1B+ Valuation)</h1>",
    unsafe_allow_html=True
)

if not df.empty:
    tot_companies = df['Company'].count()
    tot_sectors = df['Industry'].nunique()
    tot_country = df['Country'].nunique()
    tot_valuation = df['Valuation ($B)'].sum()
else:
    tot_companies, tot_sectors, tot_country, tot_valuation = 0, 0, 0, 0

col1, col2, col3, col4 = st.columns(4)

col1.metric('Companies', f'{tot_companies}')
col2.metric('Sectors', f'{tot_sectors}')
col3.metric('Countries', f'{tot_country}')
col4.metric('Valuation (U$ Trillions)', f'${tot_valuation:,.0f}')

st.markdown('---')

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df.empty:
        top_industry = (
            df.groupby('Industry')['ID']
            .count()
            .sort_values(ascending=False)
            .reset_index()
        )

        grafico1_industry = px.bar(
            top_industry,
            y='Industry',
            x='ID',
            labels={'ID': 'Count', 'Industry': 'Sector'},
            category_orders={'Industry': top_industry['Industry'].tolist()},
            text='ID',
            color_discrete_sequence=['#636EFA']
        )

        grafico1_industry.update_layout(
            title=dict(
                text='Total Number Unicorn Companies by Sector',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            title_font_size=18
        )

        grafico1_industry.update_traces(textposition='outside')
        st.plotly_chart(grafico1_industry, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir no gráfico de indústrias')
       
with col_graf2:
    if not df.empty:
        top_industry_value = (
            df.groupby('Industry')['Valuation ($B)']
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

        grafico2_industry = px.bar(
            top_industry_value,
            y='Industry',
            x='Valuation ($B)',
            labels={'Industry': 'Sector'},
            category_orders={'Industry': top_industry_value['Industry'].tolist()},
            text='Valuation ($B)',
            color_discrete_sequence=['#636EFA']
        )

        grafico2_industry.update_layout(
            title=dict(
                text='Sector Distribution by Total Unicorn Value',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            title_font_size=18
        )

        grafico2_industry.update_traces(textposition='outside')
        st.plotly_chart(grafico2_industry, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir no gráfico de indústrias')

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df.empty:
        top_pais_qtd = (
            df.groupby('Country')['ID']
            .count()
            .nlargest(15)
            .sort_values(ascending=False)
            .reset_index()
        )

        grafico1_pais = px.bar(
            top_pais_qtd,
            y='Country',
            x='ID',
            title='TOP 15 Country Largest',
            labels={'ID': 'Count'},
            category_orders={'Country': top_pais_qtd['Country'].tolist()},
            text='ID',
            color_discrete_sequence=['#636EFA']
        )

        grafico1_pais.update_layout(
            title=dict(
                text='Top 15 Countries by Number of Unicorn Companies',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            title_font_size=18
        )

        grafico1_pais.update_traces(textposition='outside')
        st.plotly_chart(grafico1_pais, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir no gráfico de países')

with col_graf4:
    if not df.empty:
        top_pais_value = (
            df.groupby('Country')['Valuation ($B)']
            .sum()
            .nlargest(15)
            .sort_values(ascending=False)
            .reset_index()
        )

        grafico2_pais = px.bar(
            top_pais_value,
            y='Country',
            x='Valuation ($B)',
            category_orders={'Country': top_pais_value['Country'].tolist()},
            text='Valuation ($B)',
            color_discrete_sequence=['#636EFA']
        )

        grafico2_pais.update_layout(
            title=dict(
                text='Top 15 Countries by Total Unicorn Valuation',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            title_font_size=18
        )

        grafico2_pais.update_traces(textposition='outside')
        st.plotly_chart(grafico2_pais, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir no gráfico de países')

col_graf5, col_graf6 = st.columns(2)

df['Date Joined'] = pd.to_datetime(df['Date Joined'], errors='coerce')

purple_dark = [
    "#907DCB",  
    "#3A25F3",
    "#636EFA",
    "#1368E7",
    "#6C4CF7"
]

with col_graf5:
    if not df.empty:
        top10_company = (
            df.sort_values('Date Joined')
            .drop_duplicates(subset='Company', keep='first')
            .head(10)
            .reset_index(drop=True)
            .loc[:, ['Company', 'Country', 'Date Joined']]
        )

        top10_company['End Date'] = top10_company['Date Joined'] + pd.Timedelta(days=30)

        grafico1_company = px.timeline(
            top10_company,
            x_start='Date Joined',
            x_end='End Date',
            y='Company',
            color='Country',
            color_discrete_sequence=purple_dark
        )

        grafico1_company.update_layout(
            title=dict(
                text='Timeline of the Firts Unicorn Companies',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            title_font_size=18,
            xaxis_title='Date Joined',
            yaxis_title='Company',
            legend_title_text='Country',
        )
        
        grafico1_company.update_traces(
            hovertemplate=
            '<b>%{y}</b><br>' +
            'Country: %{customdata[0]}<br>' +
            'Date Joined: %{x|%Y-%m}<extra></extra>',
            customdata=top10_company[['Country']]
        )

        grafico1_company.update_yaxes(autorange='reversed')

        st.plotly_chart(grafico1_company, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir no gráfico de empresas')

with col_graf6:
    if not df.empty:
        top5_cities = (
            df.groupby('City')
            .agg(qtd_total=('Company', 'nunique'))
            .sort_values('qtd_total', ascending=False)
            .head(5)
            .index
        )

        df_top5 = df[df['City'].isin(top5_cities)]
        city_year = (
            df_top5.groupby(['City', 'Year'], as_index=False)
            .agg(qtd_unicorns=('Company', 'nunique'))
            .sort_values(['City', 'Year'])
        )

        city_year['total_acumulado'] = (
            city_year
            .groupby('City')['qtd_unicorns']
            .cumsum()
        )

        grafico_top5_city = px.line(
            city_year,
            x='Year',
            y='total_acumulado',
            markers=True,
            color='City',
            color_discrete_sequence=["#907DCB", "#8e12e7", "#1368E7", "#8ed4f9", "#02C1F2"]
        )

        grafico_top5_city.update_layout(
            title=dict(
                text='Cumulative Unicorn Companies Over Time - Top 5 Cities',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            title_font_size=18,
            xaxis_title='Year',
            yaxis_title='Total Unicorn Companies',
            legend_title_text='City'
        )

        st.plotly_chart(grafico_top5_city, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir no gráfico de cidades')

col_graf7, col_graf8 = st.columns(2)

with col_graf7:

    if not df.empty:

        valuation_por_ano = (
            df.groupby('Year')['Valuation ($B)']
            .sum()
            .reset_index()
            .sort_values('Year')
        )

        valuation_por_ano['Delta'] = valuation_por_ano['Valuation ($B)'].diff()

        labels = []
        values = []
        measures = []
        texts = []

        labels.append(str(valuation_por_ano.iloc[0]['Year']))
        values.append(valuation_por_ano.iloc[0]['Valuation ($B)'])
        measures.append('absolute')
        texts.append(f"{valuation_por_ano.iloc[0]['Valuation ($B)']:.0f}")

        for i in range(1, len(valuation_por_ano)):
            delta = valuation_por_ano.iloc[i]['Delta']

            labels.append(str(valuation_por_ano.iloc[i]['Year']))
            values.append(delta)
            measures.append('relative')
            texts.append(f"{delta:+.0f}")

        labels.append('Total Final')
        values.append(valuation_por_ano['Valuation ($B)'].iloc[-1])
        measures.append('total')
        texts.append(f"{valuation_por_ano['Valuation ($B)'].iloc[-1]:,.0f}")

        grafico_cascata = go.Figure(
            go.Waterfall(
                orientation='v',
                measure=measures,
                x=labels,
                y=values,
                text=texts,
                textposition='outside',
                increasing=dict(marker=dict(color="#636EFA")),
                decreasing=dict(marker=dict(color='#e74c3c')),
                totals=dict(marker=dict(color='#f1c40f')),
                connector=dict(line=dict(color="#FFFFFF"))
            )
        )

        grafico_cascata.update_layout(
            title=dict(
                text='YoY Change in Unicorn Valuation',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            title_font_size=18,
            yaxis_title='Valuation ($B)',
            showlegend=False
        )

        st.plotly_chart(grafico_cascata, use_container_width=True)

    else:
        st.warning('Nenhum dado para exibir o gráfico de cascata')

with col_graf8:

    if not df.empty:

        uni_por_ano = (
            df.groupby('Year')['ID']
            .count()
            .reset_index(name='Total Unicorns')
        )

        grafico_unicorn = px.line(
            uni_por_ano,
            x='Year',
            y='Total Unicorns',
            markers=True,
            text='Total Unicorns'
        )

        grafico_unicorn.update_traces(
            line=dict(color='#636EFA', width=3),
            hovertemplate='<b>%{y}</b> unicorns<br>Year: %{x}<extra></extra>',
            textposition='top center',
            marker=dict(size=8)
        )
        grafico_unicorn.update_layout(
            title=dict(
                text='Number of Unicorn Companies per Year',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
             title_font_size=18
        )
        st.plotly_chart(grafico_unicorn, use_container_width=True)

    else:
        st.warning('Nenhum dado para exibir o gráfico de unicórnios')