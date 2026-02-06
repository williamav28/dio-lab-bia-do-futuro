# 💰 Agente Will: Consultor de Saúde Financeira Local

O **Will** é um agente de inteligência artificial projetado para auxiliar pessoas endividadas a recuperarem sua dignidade financeira. Diferente de soluções genéricas, o Will atua como um mentor personalizado, analisando dados reais de transações e dívidas para criar planos de ação baseados no **Método Avalanche** (quitação prioritária de juros altos).



## 🚀 Diferencial: Privacidade em Primeiro Lugar
O maior diferencial deste projeto é o uso do **Ollama** para processamento de linguagem natural. 
- **100% Local:** Nenhum dado financeiro sensível (JSON/CSV) sai da máquina do usuário.
- **Soberania de Dados:** Privacidade total em conformidade com as melhores práticas de segurança e LGPD.

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**: Linguagem base do projeto.
- **Streamlit**: Interface de usuário fluida e interativa.
- **Ollama**: Orquestração do modelo de linguagem (LLM) rodando localmente.
- **Pandas**: Manipulação e análise dos dados históricos de transações.
- **Markdown & JSON**: Estruturação da base de conhecimento e documentação.

## 📂 Estrutura do Projeto
```text
dio-lab-bia-do-futuro/
├── data/               # Base de conhecimento (JSON, CSV)
├── src/                # Código fonte da aplicação
│   └── app.py          # Aplicação Streamlit integrada ao Ollama
├── docs/               # Documentação detalhada do agente
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
└── requirements.txt    # Dependências do sistema

```

## 🤖 Como o Will pensa?

O Will segue três pilares fundamentais definidos no `system_prompt`:

1. **Trava de Segurança:** Nunca sugere parcelas que comprometam mais de 30% da renda mensal do usuário.
2. **Análise Comportamental:** Identifica gastos não essenciais (ex: excesso de delivery) e propõe a conversão desses valores em "parcelas de liberdade".
3. **Empatia Técnica:** Linguagem acolhedora, mas baseada em cálculos matemáticos precisos de juros e prazos.

## ⚙️ Como Executar

1. **Pré-requisito:** Instale o [Ollama](https://ollama.ai/) e baixe o modelo Llama3:
```bash
ollama pull llama3

```


2. **Instale as dependências:**
```bash
pip install -r requirements.txt

```


3. **Rode a aplicação:**
```bash
cd src
streamlit run app.py

```



## 📈 Métricas de Sucesso

O projeto é avaliado com base em:

* **Assertividade:** Precisão nos cálculos de juros e descontos.
* **Segurança:** Capacidade de manter o escopo apenas em finanças.
* **Humanização:** Nota de feedback sobre o tom de voz do agente.

---

⭐ Este projeto foi desenvolvido como parte do laboratório de IA da DIO.
