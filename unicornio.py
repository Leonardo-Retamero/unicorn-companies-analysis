import pandas as pd 
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title='Dashboard - Empresas Unicórnio',
    page_icon='🦄',
    layout='wide'
)

df = pd.read_csv('startups_2007_2026.csv')

st.markdown(
    """
    <h1 style='text-align: center; font-size: 40px;'>
        Empresas que Alcançaram o Status de Unicórnio (Valuation Superior a US$ 1 Bilhão)
    </h1>
    """,
    unsafe_allow_html=True
)

investidores = (
    df[['Company', 'Country', 'Industry', 'Valuation ($B)', 'Investors']]
    .assign(Investor=lambda x: x['Investors'].str.split(','))
    .explode('Investor')
)

investidores['Investor'] = investidores['Investor'].str.strip()

investidores = investidores[
    ['Company', 'Investor', 'Country', 'Industry', 'Valuation ($B)']
]

if not df.empty:
    tot_valuation = df['Valuation ($B)'].sum()
    tot_companies = df['Company'].count()
    tot_sectors = df['Industry'].nunique()
    tot_country = df['Country'].nunique()
    tot_city = df['City'].nunique()
    tot_investor = investidores['Investor'].nunique()
else:
    tot_valuation, tot_companies, tot_sectors, tot_country, tot_city, tot_investor = 0, 0, 0, 0, 0, 0

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric('Valuation (U$ Trillions)', f'${tot_valuation:,.0f}')
col2.metric('Companies', f'{tot_companies}')
col3.metric('Sectors', f'{tot_sectors}')      
col4.metric('Countries', f'{tot_country}')
col5.metric('Cities', f'{tot_city}')  
col6.metric('Investors', f'{tot_investor}')

st.markdown("""
<style>
div[data-testid="stMetric"] {
    background-color: #1f1f1f;
    border-left: 6px solid #00BFFF;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

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
            labels={'Industry': 'Sector', 'ID': 'Companies'},
            category_orders={'Industry': top_industry['Industry'].tolist()},
            text='ID',
            color_discrete_sequence=['#00BFFF']
        )

        grafico1_industry.update_layout(
            title=dict(
                text='Quantidade de Empresas Unicórnio por Setor',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            xaxis_title=None,
            yaxis_title=None,
            title_font_size=18
        )

        grafico1_industry.update_traces(
            textposition='outside',
            hovertemplate=
            '<b>Sector:</b> %{y}<br>' +
            '<b>Companies:</b> %{x}' +
            '<extra></extra>'
        )

        st.plotly_chart(grafico1_industry, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir no gráfico de indústrias')

def formatar_valuation(valor):
    if valor >= 1000:
        return f'US$ {valor/1000:.2f} trilhões'
    else:
        return f'US$ {valor:.2f} bilhões'
       
with col_graf2:
    if not df.empty:
        top_industry_value = (
            df.groupby('Industry')['Valuation ($B)']
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

        top_industry_value['valuation_formatado'] = (
            top_industry_value['Valuation ($B)']
            .apply(formatar_valuation)
        )

        grafico2_industry = px.bar(
            top_industry_value,
            y='Industry',
            x='Valuation ($B)',
            labels={'Industry': 'Sector', 'Valuation ($B)': 'Valuation'},
            category_orders={'Industry': top_industry_value['Industry'].tolist()},
            text='Valuation ($B)',
            color_discrete_sequence=['#00BFFF']
        )

        grafico2_industry.update_layout(
            title=dict(
                text='Valuation das Empresas Unicórnio por Setor (US$ Bilhões)',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            yaxis_title=None,
            xaxis_title=None,
            title_font_size=18
        )

        grafico2_industry.update_traces(
            textposition='outside',
            customdata=top_industry_value[['valuation_formatado']],
            hovertemplate=
            '<b>Sector:</b> %{y}<br>' +
            '<b>Valuation:</b> %{customdata[0]}' +
            '<extra></extra>'
        )

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
            labels={'ID': 'Companies'},
            category_orders={'Country': top_pais_qtd['Country'].tolist()},
            text='ID',
            color_discrete_sequence=['#00BFFF']
        )

        grafico1_pais.update_layout(
            title=dict(
                text='Top 15 Países por Quantidade de Empresas Unicórnio',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            xaxis_title=None,
            yaxis_title=None,
            title_font_size=18
        )

        grafico1_pais.update_traces(
            textposition='outside',
            hovertemplate=
            '<b>Country:</b> %{y}<br>' +
            '<b>Companies:</b> %{x}' +
            '<extra></extra>'
        )

        st.plotly_chart(grafico1_pais, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir no gráfico de países')

with col_graf4:
    if not df.empty:
        top_pais_value = (
            df.groupby('Country')['Valuation ($B)']
            .sum()
            .round(2)
            .nlargest(15)
            .sort_values(ascending=False)
            .reset_index()
        )

        top_pais_value['valuation_formatado'] = (
            top_pais_value['Valuation ($B)']
            .apply(formatar_valuation)
        )

        grafico2_pais = px.bar(
            top_pais_value,
            y='Country',
            x='Valuation ($B)',
            labels={'Country': 'País'},
            category_orders={'Country': top_pais_value['Country'].tolist()},
            text='Valuation ($B)',
            color_discrete_sequence=['#00BFFF']
        )

        grafico2_pais.update_layout(
            title=dict(
                text='Top 15 Países por Valuation Total das Empresas Unicórnio (US$ Bilhões)',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            xaxis_title=None,
            yaxis_title=None,
            title_font_size=18
        )

        grafico2_pais.update_traces(
            textposition='outside',
            customdata=top_pais_value[['valuation_formatado']],
            hovertemplate=
            '<b>Country:</b> %{y}<br>' +
            '<b>Valuation:</b> %{customdata[0]}' +
            '<extra></extra>'
        )

        st.plotly_chart(grafico2_pais, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir no gráfico de países')

col_graf5, col_graf6 = st.columns(2)

df['Date Joined'] = pd.to_datetime(df['Date Joined'], errors='coerce')

purple_dark = ["#636EFA", "#3A25F3", "#00BFFF", "#1368E7", "#6C4CF7"]

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
                text='Linha do Tempo das Primeiras Empresas Unicórnio',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            title_font_size=18,
            xaxis_title=None,
            yaxis_title=None,
            legend_title_text='Country',
        )
        
        grafico1_company.update_traces(
            customdata=top10_company[['Country']],
            hovertemplate=
            '<b>%{y}</b><br>' +
            'Date Joined: %{x|%Y-%m}<extra></extra>'
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
            color_discrete_sequence=["#6366F1", "#8e12e7", "#1368E7", "#8ed4f9", "#02C1F2"]
        )

        grafico_top5_city.update_layout(
            title=dict(
                text='Evolução Acumulada das Empresas Unicórnio nas 5 Principais Cidades',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            title_font_size=18,
            xaxis_title=None,
            yaxis_title=None,
            legend_title_text='City'
        )

        grafico_top5_city.update_traces(
            hovertemplate=
            '<b>City:</b> %{fullData.name}<br>' +
            '<b>Year:</b> %{x}<br>' +
            '<b>Total Companies:</b> %{y}<br>' +
            '<extra></extra>'
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
                increasing=dict(marker=dict(color="#05861E")),
                decreasing=dict(marker=dict(color="#ba1b09")),
                totals=dict(marker=dict(color='#f1c40f')),
                connector=dict(line=dict(color="#FFFFFF"))
            )
        )

        grafico_cascata.update_layout(
            title=dict(
                text='Variação Anual (YoY) do Valuation das Empresas Unicórnio',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            title_font_size=18,
            yaxis_title=None,
            showlegend=False
        )

        grafico_cascata.update_traces(
            hovertemplate=
            '<b>Year:</b> %{x}<br>' +
            '<b>Valuation (US$ B):</b> %{text}<extra></extra>'
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
            line=dict(color='#00BFFF', width=3),
            hovertemplate=
            '<b>Unicorns:<b> %{y}<b>' +
            '<br>Year:<b> %{x}<b>'
            '<extra></extra>',
            textposition='top center',
            marker=dict(size=8)
        )

        grafico_unicorn.update_layout(
            title=dict(
                text='Quantidade de Empresas Unicórnio por Ano',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            yaxis_title=None,
            xaxis_title=None,
            title_font_size=18
        )

        st.plotly_chart(grafico_unicorn, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir o gráfico de unicórnios')

col_graf9, col_graf10 = st.columns(2)

with col_graf9:

    if not df.empty:

        continentes = (
            df.groupby('Continent')
            .agg(Qtd_Empresas=('Company', 'nunique'))
            .reset_index()
        )

        continent_coords = {
            'Europe': {'lat': 54.5260, 'lon': 15.2551},
            'Asia': {'lat': 34.0479, 'lon': 100.6197},
            'Africa': {'lat': -8.7832, 'lon': 34.5085},
            'South America': {'lat': -14.2350, 'lon': -51.9253},
            'North America': {'lat': 54.5260, 'lon': -105.2551},
            'Oceania': {'lat': -25.2744, 'lon': 133.7751},
            'Central America': {'lat': 15.7835, 'lon': -90.1500}
        }

        coords_df = pd.DataFrame([
            {'Continent': k, 'lat': v['lat'], 'lon': v['lon']}
            for k, v in continent_coords.items()
        ])

        continentes_com_coords = continentes.merge(
            coords_df,
            on='Continent',
            how='left'
        )

        graf_mapa = px.scatter_geo(
            continentes_com_coords,
            lat='lat',
            lon='lon',
            size='Qtd_Empresas',
            size_max=60,
            color='Qtd_Empresas',
            hover_name='Continent',
            projection='natural earth',
            color_continuous_scale='Blues'
        )

        graf_mapa.update_traces(
            hovertemplate=
            '<b>Continente:</b> %{hovertext}<br>' +
            '<b>Companies:</b> %{marker.size}<extra></extra>'
        )

        graf_mapa.update_geos(
            bgcolor='#0E1117',
            showland=True,
            landcolor='#2E2E2E',
            showocean=True,
            oceancolor='#0E1117',
            showcountries=True,
            countrycolor='#666666',
            coastlinecolor='#888888'
        )

        graf_mapa.update_layout(
            title=dict(
                text='Quantidade de Empresas Unicórnio por Continente',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            title_font_size=18,
            paper_bgcolor='#0E1117',
            plot_bgcolor='#0E1117',
            font_color='white',
            margin=dict(l=0, r=0, t=60, b=0),
            coloraxis_colorbar_title='Empresas'
        )

        st.plotly_chart(graf_mapa, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir o gráfico de unicórnios')

with col_graf10:

    if not df.empty:

        industry_evolution = (
        df[df['Year'].between(2020, 2026)]
        .groupby(['Year', 'Industry'])['ID']
        .count()
        .reset_index()
        )

        industry_evolution['total_acumulado'] = (
            industry_evolution
            .groupby('Industry')['ID']
            .cumsum()
        )

        top_industries = (
            industry_evolution
            .groupby('Industry')['total_acumulado']
            .max()
            .nlargest(5)
            .index
        )

        industry_top = industry_evolution[
            industry_evolution['Industry'].isin(top_industries)
        ]

        graf_sector_acum = px.line(
            industry_top,
            x='Year',
            y='total_acumulado',
            color='Industry',
            markers=True,
            labels={'total_acumulado': 'Companies'},
            color_discrete_sequence=['#00BFFF', '#3B82F6', '#6366F1', '#8B5CF6', '#14B8A6']
        )

        graf_sector_acum.update_layout(
            title=dict(
                text='Evolução Acumulada dos 5 Principais Setores de Empresas Unicórnio',
                x=0.6,
                xanchor='center',
                xref='paper',
            ),
            title_font_size=18,
            xaxis_title=None,
            yaxis_title=None
        )

        graf_sector_acum.update_traces(
            hovertemplate=
            '<b>Sector:</b> %{fullData.name}<br>' +
            '<b>Year:</b> %{x}<br>' +
            '<b>Total Companies:</b> %{y}<br>' +
            '<extra></extra>'
        )

        st.plotly_chart(graf_sector_acum, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir o gráfico de unicórnios')

col_graf11, col_graf12 = st.columns(2)

with col_graf11:

    if not df.empty:

        qtd_investors = (
            investidores
            .groupby('Investor')
            .agg(Qtd_Investidores=('Company', 'count'))
            .sort_values('Qtd_Investidores', ascending=False)
            .nlargest(10, 'Qtd_Investidores')
            .reset_index()
        )

        graf_investors = px.bar(
            qtd_investors,
            x='Investor',
            y='Qtd_Investidores',
            category_orders={'Investor': qtd_investors['Investor'].tolist()},
            text='Qtd_Investidores',
            color_discrete_sequence=['#00BFFF']
        )

        graf_investors.update_layout(
            title=dict(
                text='Top 10 Investidores por Quantidade de Empresas',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            yaxis_title=None,
            xaxis_title=None
        )

        graf_investors.update_traces(
            textposition='outside',
            hovertemplate=
            '<b>Investor:</b> %{x}<br>' +
            '<b>Companies:</b> %{y}<br>' +
            '<extra></extra>'
        )

        st.plotly_chart(graf_investors, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir o gráfico de unicórnios')

with col_graf12:

    if not df.empty:

        top_cidades = (
            df.groupby('City')
            .agg(Qtd_Empresas=('ID', 'count'))
            .sort_values('Qtd_Empresas', ascending=False)
            .head(10)
            .reset_index()
        )

        graf_city = px.bar(
            top_cidades,
            x='City',
            y='Qtd_Empresas',
            text='Qtd_Empresas',
            color_discrete_sequence=['#00BFFF'],
            category_orders={'City': top_cidades['City'].tolist()}
        )

        graf_city.update_layout(
            title=dict(
                text='Top 10 Cidades com Maior Número de Empresas Unicórnio',
                x=0.5,
                xanchor='center',
                xref='paper'
            ),
            yaxis_title=None,
            xaxis_title=None
        )

        graf_city.update_traces(
            textposition='outside',
            hovertemplate=
            '<b>City:<b> %{x}<br>' +
            '<b>Companies:<b> %{y}<br>' +
            '<extra></extra>'
        )

        st.plotly_chart(graf_city, use_container_width=True)

    else:
        st.warning('Nenhum dado para exibir o gráfico de unicórnios')