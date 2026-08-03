# 🦄 Dashboard de Análise de Empresas Unicórnio

### 📌 Visão Geral do Projeto

Este projeto apresenta um dashboard analítico focado em empresas unicórnio globais, utilizando dados reais sobre startups privadas avaliadas em USD 1 bilhão ou mais. O objetivo é explorar como essas empresas estão distribuídas por setores, países, cidades e ao longo do tempo. 

O dashboard foi desenvolvido utilizando Python, Pandas, Plotly e Streamlit, com foco em visualizações interativas, clareza na comunicação dos dados e geração de insights de negócio.

### 🔗 [Acesse o Dashboard pelo Streamlit](https://unicorn-companies-analysis.streamlit.app/)

---

### 📝 Processo de Desenvolvimento

Durante a construção do projeto foram realizadas as seguintes etapas:

### Importação dos dados

- Carregamento do dataset utilizando Pandas.
- Utilização da fonte de dados da CB Insights.

### Análise Exploratória (EDA)

Iniciei a Análise Exploratória realizando as seguintes verificações da Qualidade e Estrutura dos Dados:

- Tamanho da base de dados (linhas e colunas).
- Estrutura do DataFrame e os tipos de dados das colunas.
- Existência de valores ausentes.

### Tratamento dos dados

Após a etapa de exploração da base de dados, foram realizadas as seguintes transformações para melhorar a qualidade, consistência e confiabilidade das informações:

- Preenchimento dos valores ausentes da coluna Investors com investidores confirmados por meio da fonte CB Insights.
- Preenchimento dos valores ausentes da coluna Country utilizando a cidade como referência.
- Preenchimento dos valores ausentes da coluna City utilizando o país ou a empresa como referência, quando aplicável.
- Correção de registros com informações de cidade e país invertidas.
- Padronização dos nomes das categorias da coluna Industry para garantir consistência nas análises.
- Conversão da coluna Date Joined para o tipo datetime.
- Conversão da coluna Valuation ($B) para o tipo float, permitindo a realização de cálculos e agregações.

### Engenharia de Atributos (Feature Engineering)

Com a base de dados tratada, foram criados novos atributos para ampliar as possibilidades de análise:

- Criação da coluna Year a partir da coluna Date Joined, facilitando análises temporais.
- Criação da coluna Continent a partir da coluna Country, permitindo análises geográficas em nível continental.
- Criação de uma tabela auxiliar de investidores, separando múltiplos investidores em registros individuais para possibilitar análises como quantidade de empresas investidas e valuation acumulado por investidor.

### Preparação das Tabelas Analíticas

Para apoiar as análises exploratórias e a construção das visualizações, foram desenvolvidas tabelas agregadas com métricas específicas:

- Cidades: quantidade de empresas unicórnio e valuation acumulado das 20 maiores cidades em quantidade de empresas unicórnio.
- Brasil: quantidade de empresas unicórnio e valuation por ano no Brasil.
- YoY de Empresas: cálculo da variação percentual anual (Year over Year) da quantidade de empresas unicórnio.
- YoY de Valuation: cálculo da variação percentual anual do valuation acumulado das empresas unicórnio.
- Investidores: consolidação da quantidade de empresas investidas e do valuation acumulado associado a cada investidor.
- Continentes: quantidade de países, quantidade de empresas e o valuation por continente.
- Evolução das Indústrias: analisar a evolução acumulada do número de empresas unicórnio por indústria entre 2020 e 2026, identificando os setores que mais expandiram sua participação ao longo dos últimos anos.
- Investidores por Indústria: analisar quais setores atraíram o maior número de investidores diferentes.

---

### 💪🏽 Desafios encontrados

Durante a análise exploratória e o tratamento da base de dados alguns desafios precisaram ser resolvidos:

- Á busca pela base de dados atualizada de empresas unicórnio.
- Durante a importação da base de dados ocorreu um erro onde alguns registros da coluna de investidores estavam ausentes, tive que buscar cada empresa que estava com valores ausentes dos investidores e utilizar um filtro em python para preencher esses valores com as respectivas informações dos seus investidores.
- Para a realização de análises por investidores, tive que criar uma função em python para separar cada investidor em uma linha porque cada empresa poderia ter mais de um investidor em uma mesma linha separados por vírgula.

---

### 🧠 Principais Insights

Após a análise exploratória e a construção do dashboard foi possível encontrar insights relevantes:

- Investidores com mais quantidade de empresas investidas não significa estar associados ás empresas com maior valor de mercado.
- O continente europeu possuí mais países com empresas unicórnio.
- América do Norte é o continente com mais empresas unicórnio, sendo o dobro do segundo colocado.
- Os Estados Unidos lideram tanto em quantidade de empresas unicórnio quanto em valuation total.
- San Francisco e New York se destacam como hubs globais de inovação.
- O ecossistema unicórnio apresentou crescimento acelerado nos últimos anos, especialmente após 2018.
- Os setores Enterprise Tech, Fintech, Internet Software & Services, Industrials e Financial Services apresentaram o maior crescimento acumulado no número de empresas unicórnio entre 2020 e 2026.

---

### 🎯 Perguntas Respondidas

• Quais setores concentram o maior número de empresas unicórnio?

• Quais setores apresentam o maior valor total de valuation?

• Quais países lideram em quantidade de unicórnios e em valor total?

• Quais foram as primeiras empresas a se tornar unicórnio?

• Qual o crescimento acumulado das cidades com mais empresas unicórnio?

• Como o valuation das empresas unicórnio varia ano a ano (YoY)?

• Como evoluiu a criação de empresas unicórnio ao longo do tempo?

• Qual é a distribuição de empresas unicórnio por continente?

• Quais indústrias mais cresceram nos últimos anos?

• Quais são os maiores grupos de investidores?

---

### 1️⃣ Total de Empresas Unicórnio por Setor

Este gráfico apresenta a quantidade de empresas unicórnio por setor, destacando onde há maior concentração dessas empresas.

Principais insights:

• Fintech e Internet Software & Services lideram em número de empresas.

• Setores fortemente ligados à tecnologia dominam o ecossistema unicórnio.

<img width="873" height="529" alt="image" src="https://github.com/user-attachments/assets/8f5a4757-f3ba-474e-84c0-d18ea0bf9752" />

---

### 2️⃣ Distribuição de Valuation Total por Setor

Esta visualização mostra o valor total de valuation (em bilhões de dólares) agregado por setor.

Principais insights:

• O setor de Fintech lidera também em valuation total.

• Alguns setores possuem menos empresas, mas alto valuation médio por companhia.

• O setor de Inteligência Artificial teve uma alta crescente nos últimos anos.

<img width="952" height="512" alt="image" src="https://github.com/user-attachments/assets/a8c49165-22c3-4bcd-a81f-b7d7895df03a" />

---

### 3️⃣ Top 15 Países por Quantidade de Empresas Unicórnio

Este gráfico ranqueia os 15 países com maior número de empresas unicórnio.

Principais insights:

• Os Estados Unidos lideram com ampla vantagem.

• China e Índia se destacam como grandes polos fora dos EUA.

<img width="891" height="508" alt="image" src="https://github.com/user-attachments/assets/af7d110f-f41d-451d-a7c8-788b82e87017" />

---

### 4️⃣ Top 15 Países por Valuation Total de Empresas Unicórnio

Este gráfico mostra os países ordenados pelo valor total combinado de valuation das empresas unicórnio.

Principais insights:

• Os Estados Unidos dominam também em valuation total.

• Alguns países apresentam posição melhor em valuation do que em quantidade, indicando maior concentração de capital.

<img width="914" height="529" alt="image" src="https://github.com/user-attachments/assets/b630078f-47d9-4985-8e25-357fdc246a95" />

---

### 5️⃣ Linha do Tempo das Primeiras Empresas Unicórnio

Esta visualização apresenta as primeiras empresas a atingirem o status de unicórnio, organizadas ao longo do tempo e coloridas por país.

Principais insights:

• As primeiras empresas unicórnio surgiram majoritariamente entre 2007 e 2013.

• O gráfico evidencia a diversidade geográfica do início do ecossistema unicórnio.

<img width="911" height="488" alt="image" src="https://github.com/user-attachments/assets/cb939f4e-033f-498e-8d5d-03ac78878552" />

---

### 6️⃣ Evolução Acumulada de Empresas Unicórnio – Top 5 Cidades

Este gráfico mostra a evolução acumulada do número de empresas unicórnio ao longo do tempo para as 5 principais cidades.

Principais insights:

• Cidades como Beijing, San Francisco e New York apresentam forte aceleração após 2015.

• O crescimento evidencia hubs globais de inovação e empreendedorismo.

<img width="929" height="474" alt="image" src="https://github.com/user-attachments/assets/ffef6ca1-3c13-4dad-802e-b81a3cdd81ba" />

---

### 7️⃣ Variação Ano a Ano (YoY) do Valuation das Empresas Unicórnio

Este gráfico ilustra a variação anual do valuation total, destacando aumentos e quedas ao longo dos anos.

Principais insights:

• O crescimento do valuation se intensifica a partir de 2016.

• Mesmo com quedas pontuais, o mercado apresenta fortes recuperações.

<img width="897" height="457" alt="image" src="https://github.com/user-attachments/assets/5ee96315-ea6f-46fe-aaf6-d0a663f7b8a7" />

---

### 8️⃣ Quantidade de Empresas Unicórnio por Ano

Esta visualização apresenta o número de novas empresas unicórnio criadas a cada ano.

Principais insights:

• Observa-se uma forte aceleração após 2018.

• O pico reflete períodos de alta atividade de venture capital.

<img width="892" height="487" alt="image" src="https://github.com/user-attachments/assets/b3229011-e264-45f0-8355-976231fdc118" />

--- 

### 🛠️ Ferramentas e Tecnologias

• Python

• Pandas – limpeza, transformação e agregação de dados

• Plotly – visualizações interativas

• Streamlit – construção do dashboard
