# 🦄 Dashboard de Análise de Empresas Unicórnio

### 📌 Visão Geral do Projeto

Este projeto apresenta uma análise exploratória do ecossistema global de empresas unicórnio, desde a etapa de tratamento e preparação dos dados até a construção de um dashboard interativo, utilizando dados reais sobre startups privadas avaliadas em USD 1 bilhão ou mais. O objetivo é explorar como essas empresas estão distribuídas por setores, países, cidades e ao longo do tempo. 

O dashboard foi desenvolvido utilizando Python, Pandas, Plotly e Streamlit, com foco em visualizações interativas, clareza na comunicação dos dados e geração de insights de negócio.

### 🔗 [Acesse o Dashboard pelo Streamlit](https://unicorn-companies-analysis.streamlit.app/)
### ⛲ [Fonte de Dados: CB Insights](https://www.cbinsights.com/research-unicorn-companies?)

---

### 📊 Dataset

A base utilizada contém informações sobre empresas privadas que atingiram valuation de pelo menos US$ 1 bilhão, incluindo empresa, valuation, data de entrada no grupo de unicórnios, país, cidade, indústria e investidores.

```
Registros iniciais: 1.569
Colunas: 8
Período: 2007–2026
```

---

### 🎯 Perguntas Respondidas

Este projeto busca explorar o ecossistema global de empresas unicórnio por meio de análises exploratórias e visualizações de dados, identificando padrões, tendências, crescimento e concentração dessas empresas. Para isso, foram respondidas as seguintes questões de negócio:

- Quais setores concentram o maior número de empresas unicórnio?

- Quais setores apresentam o maior valor total de valuation?

- Quais países lideram em quantidade de unicórnios e em valor total?

- Quais foram as primeiras empresas a se tornar unicórnio?

- Quais cidades se consolidaram como os principais hubs globais de inovação ao longo dos anos?

- Como o valuation das empresas unicórnio varia ano a ano (YoY)?

- Como evoluiu a criação de empresas unicórnio ao longo do tempo?

- Qual é a distribuição de empresas unicórnio por continente?

- Quais setores apresentaram maior crescimento acumulado entre 2020 e 2026?

- Quais investidores possuem o maior número de investimentos em empresas unicórnio?

- Quais cidades concentram o maior número de empresas unicórnio?

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

### 💪🏽 Desafios Encontrados

Durante a análise exploratória e o tratamento da base de dados alguns desafios precisaram ser resolvidos:

- A coluna Investors apresentava registros ausentes. Para preservar essas empresas na análise, as informações foram complementadas por meio de consulta à fonte de dados utilizada.
- A coluna Investors armazenava múltiplos investidores em uma única célula. Foi necessário transformar essa estrutura para que cada investidor ocupasse um registro individual, permitindo análises por investidor.

---

### ✔️ Competências Demonstradas

- Python para Análise de Dados
- Pandas
- Data Cleaning
- Data Wrangling
- Análise Exploratória de Dados (EDA)
- Feature Engineering
- Agregação e transformação de dados
- Análise temporal e YoY
- Análise geográfica
- Data Visualization
- Storytelling com Dados
- Desenvolvimento de Dashboards

---

### 🧠 Principais Insights

Após a análise exploratória e a construção do dashboard foi possível encontrar insights relevantes:

- A Europa reúne o maior número de países com empresas unicórnio, indicando uma distribuição mais equilibrada das oportunidades de inovação no continente.
- América do Norte é o continente com mais empresas unicórnio, sendo o dobro do segundo colocado.
- Os Estados Unidos lideram tanto em quantidade de empresas unicórnio quanto em valuation total.
- San Francisco e New York se destacam como hubs globais de inovação.
- O ecossistema unicórnio apresentou crescimento acelerado nos últimos anos, especialmente após 2018.
- Os setores Enterprise Tech, Fintech, Internet Software & Services, Industrials e Financial Services apresentaram o maior crescimento acumulado no número de empresas unicórnio entre 2020 e 2026.

---

### 1️⃣ Total de Empresas Unicórnio por Setor

Este gráfico apresenta a quantidade de empresas unicórnio por setor, destacando onde há maior concentração dessas empresas.

Principais insights:

- Tecnologia Empresarial, Tecnologia Financeira e Serviços de Internet e Software representam os setores de maior relevância para startups de alto valor de mercado, refletindo a forte demanda global por soluções tecnológicas e digitais voltadas ao ambiente corporativo e ao setor financeiro.

- Setores fortemente ligados à tecnologia dominam o ecossistema unicórnio.

<img width="873" height="529" alt="image" src="https://github.com/user-attachments/assets/8f5a4757-f3ba-474e-84c0-d18ea0bf9752" />

---

### 2️⃣ Distribuição de Valuation Total por Setor

Esta visualização mostra o valor total de valuation (em bilhões de dólares) agregado por setor.

Principais insights:

- O elevado valuation concentrado no setor de Tecnologia Empresarial demonstra sua importância estratégica, refletindo um forte valor por soluções voltadas à transformação digital e à gestão corporativa.

- Alguns setores possuem menos empresas, mas alto valuation médio por companhia.

- O setor de Inteligência Artificial teve uma alta crescente nos últimos anos.

<img width="952" height="512" alt="image" src="https://github.com/user-attachments/assets/a8c49165-22c3-4bcd-a81f-b7d7895df03a" />

---

### 3️⃣ Top 15 Países por Quantidade de Empresas Unicórnio

Este gráfico apresenta os 15 países com o maior número de empresas unicórnio.

Principais insights:

- Os Estados Unidos lideram com ampla vantagem, consolidando-se como o principal ecossistema global para a criação e o crescimento de empresas unicórnio.

- China e Índia destacam-se como os principais ecossistemas asiáticos, refletindo o crescimento acelerado de seus mercados de tecnologia e startups.

<img width="894" height="527" alt="image" src="https://github.com/user-attachments/assets/bbba4101-0002-4995-81af-885b8a743989" />

---

### 4️⃣ Top 15 Países por Valuation Total de Empresas Unicórnio

Este gráfico mostra os países ordenados pelo valor total combinado de valuation das empresas unicórnio.

Principais insights:

- Os Estados Unidos lideram com ampla vantagem em valuation total, reforçando sua posição como o principal mercado global de empresas unicórnio e de geração de valor para startups.

- China e Reino Unido ocupam as posições seguintes, demonstrando que esses países concentram empresas unicórnio de elevado valor de mercado, mesmo com um número inferior de empresas em relação aos Estados Unidos.

- A comparação com o ranking de quantidade de empresas mostra que alguns países possuem menos unicórnios, porém com valuations médios mais elevados, refletindo maior concentração de capital e empresas de alto valor de mercado.

<img width="894" height="515" alt="image" src="https://github.com/user-attachments/assets/85509889-a6f7-4e11-a1f0-221226ae521e" />

---

### 5️⃣ Linha do Tempo das Primeiras Empresas Unicórnio

**🎯 Objetivo da análise:** Analisar o surgimento das primeiras empresas unicórnio e observar como o fenômeno começou a se distribuir geograficamente ao longo dos anos.

**🧠 Principais insights:**

- As primeiras empresas unicórnio surgiram entre 2007 e 2013, marcando o início da consolidação do ecossistema global de startups de alto valor de mercado.

- Embora os Estados Unidos tenham liderado esse movimento, o surgimento de empresas na França, China, Suécia e Hong Kong demonstra que o ecossistema unicórnio começou a se desenvolver em diferentes regiões do mundo desde seus primeiros anos.

- Os Estados Unidos concentraram a maior parte das primeiras empresas unicórnio, consolidando sua posição como principal polo mundial de inovação, tecnologia e empreendedorismo.

<img width="873" height="459" alt="image" src="https://github.com/user-attachments/assets/0ba21343-a17e-4ea6-8510-19e94289c0d2" />

---

### 6️⃣ Evolução Acumulada de Empresas Unicórnio – Top 5 Cidades

**🎯 Objetivo da análise:** Acompanhar a evolução da concentração de empresas unicórnio nas principais cidades e comparar o crescimento desses hubs ao longo do período analisado.

**🧠 Principais insights:**

- San Francisco e Nova York apresentam forte crescimento na criação de empresas unicórnio ao longo do período analisado, consolidando-se como os principais hubs globais de inovação, tecnologia e empreendedorismo.

<img width="885" height="445" alt="image" src="https://github.com/user-attachments/assets/1e7a725f-dd0d-4014-945a-5debb2b691be" />

---

### 7️⃣ Variação Ano a Ano (YoY) do Valuation das Empresas Unicórnio

**🎯 Objetivo da análise:** Avaliar as variações anuais do valuation agregado das empresas unicórnio e identificar períodos de maior expansão ou retração.

**🧠 Principais insights:**

- O valuation das empresas unicórnio apresentou forte expansão entre 2017 e 2021, atingindo seu maior crescimento anual em 2021 (+US$ 650 bilhões). Nos anos seguintes, o mercado passou por um período de maior volatilidade e correção dos valuations, refletindo mudanças no cenário econômico global e na dinâmica dos investimentos em startups.

- Entre 2020 e 2021, a aceleração da digitalização impulsionada pela pandemia, o aumento da liquidez global e os recordes de investimentos em Venture Capital favoreceram o crescimento das empresas unicórnio. Já entre 2022 e 2024, o aumento das taxas de juros, a inflação global, a desaceleração econômica e a redução dos investimentos em startups contribuíram para revisões de valuation e maior volatilidade no mercado.

<img width="901" height="405" alt="image" src="https://github.com/user-attachments/assets/6383815c-f660-442b-979d-4a640b0f3826" />

---

### 8️⃣ Quantidade de Empresas Unicórnio por Ano

**🎯 Objetivo da análise:** Analisar a evolução anual do surgimento de novas empresas unicórnio e identificar períodos de maior crescimento ou desaceleração.

**🧠 Principais insights:**

- O recorde de empresas unicórnio em 2021 foi impulsionado pela transformação digital acelerada na pandemia, pela liquidez global e pelo volume histórico de aportes em Venture Capital. A partir de 2022, esse cenário reverteu, a inflação global e a consequente alta dos juros encareceram o crédito e reduziram o capital disponível. Isso desacelerou o mercado de startups e encolheu o surgimento de novas empresas avaliadas acima de US$ 1 bilhão.

<img width="901" height="456" alt="image" src="https://github.com/user-attachments/assets/0b67d6d1-8dd7-4f19-a906-f1c938a9c2eb" />

--- 

### 9️⃣ Quantidade de Empresas Unicórnio por Continente

**🎯 Objetivo da análise:** Examinar a distribuição e avaliar o nível de concentração regional das empresas unicórnio entre os continentes: América do Norte, América do Sul, América Central, Europa, Ásia, África e Oceania.

**🧠 Principais insights:**

- A América do Norte concentra a maior quantidade de empresas unicórnio, destacando-se como o principal ecossistema global de empresas unicórnio.

- A distribuição geográfica das empresas unicórnio revela uma forte concentração em regiões com ecossistemas de inovação consolidados, elevada disponibilidade de capital de risco (Venture Capital) e mercados de tecnologia mais maduros.

<img width="878" height="514" alt="image" src="https://github.com/user-attachments/assets/1b8131a4-2f8c-4684-a864-c554d691a9bc" />

---

### 🔟 Evolução Acumulada dos 5 Principais Setores de Empresas Unicórnio

**🎯 Objetivo da análise:** Acompanhar a evolução dos principais setores nos últimos anos e avaliar quais apresentaram maior expansão no número acumulado de empresas unicórnio.

**🧠 Principais insights:**

- A partir de 2022, observa-se uma maior concentração de novos unicórnios em Tecnologia Empresarial, indicando uma mudança gradual no foco dos investimentos para soluções voltadas ao mercado corporativo.

- Os setores de Tecnologia Financeira (Fintech) e Software & Serviços de Internet apresentaram rápida expansão no início do período, impulsionados pela aceleração da transformação digital durante a pandemia.

<img width="888" height="461" alt="image" src="https://github.com/user-attachments/assets/d35db56b-0804-4e72-b2fa-9b9825bd91b3" />

---

### 1️⃣1️⃣ Top 10 Investidores por Quantidade de Empresas

**🎯 Objetivo da análise:** Identificar os investidores com o maior número de participações em empresas unicórnio, revelando os principais atores do ecossistema global de Venture Capital.

**🧠 Principais insights:**

- Andreessen Horowitz, Accel e Sequoia Capital aparecem entre os investidores associados ao maior número de empresas unicórnio da base, destacando sua forte presença no ecossistema global de startups.

- O ranking é composto majoritariamente por fundos e empresas de investimento especializados em startups, evidenciando a presença recorrente de grandes investidores no financiamento de empresas que atingiram o status de unicórnio.

<img width="896" height="496" alt="image" src="https://github.com/user-attachments/assets/6c6ca7fe-3d14-4dbb-9db3-7e456a943c0f" />

---

### 1️⃣2️⃣ Top 10 Cidades com Maior Número de Empresas Unicórnio

**🎯 Objetivo da análise:** Identificar as cidades que concentram o maior número de empresas unicórnio e destacar os principais hubs globais de inovação.

**🧠 Principais insights:**

- San Francisco lidera o ranking com ampla vantagem, consolidando-se como o principal polo mundial de startups de alto valor de mercado, impulsionado pelo ecossistema do Vale do Silício.

- New York ocupa a segunda posição, reforçando a liderança dos Estados Unidos como o país que concentra os principais centros globais de inovação e Venture Capital.

- Beijing, Shanghai e Shenzhen demonstram a força do ecossistema chinês de startups, posicionando a China como a principal potência tecnológica fora dos Estados Unidos.

- As 10 principais cidades concentram aproximadamente 45% das empresas unicórnio da base, evidenciando uma forte concentração geográfica do ecossistema.

<img width="931" height="458" alt="image" src="https://github.com/user-attachments/assets/3c374952-0cc9-47f5-a76d-166e870e91ac" />

---

### 🛠️ Ferramentas e Tecnologias

- **Python** – linguagem principal utilizada no desenvolvimento do projeto.
- **Pandas** – limpeza, tratamento, transformação e preparação dos dados.
- **Matplotlib** – criação de gráficos para a Análise Exploratória de Dados (EDA).
- **Seaborn** – visualizações estatísticas durante a exploração dos dados.
- **Plotly** – desenvolvimento das visualizações interativas do dashboard.
- **Streamlit** – construção e disponibilização do dashboard interativo.
- **GitHub** – documentação, versionamento e publicação do projeto.
