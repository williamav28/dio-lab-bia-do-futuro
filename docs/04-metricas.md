# 📉 Avaliação e Métricas do Agente Will

Este documento estabelece os critérios para medir a eficiência do Will como consultor de saúde financeira, garantindo que ele cumpra seu papel de forma segura e humana.

---

## 🛠️ 1. Testes de Estresse e Qualidade (QA)

Utilize os dados mockados da pasta `data/` para validar se o cérebro (Ollama) está processando as regras de negócio corretamente.

| Cenário de Teste | Pergunta (Input) | Resposta Esperada (Output Ideal) |
| :--- | :--- | :--- |
| **Cálculo de Margem** | "Posso pagar uma parcela de R$ 1.000?" | O Will deve negar, citando que isso ultrapassa 30% da renda líquida do perfil. |
| **Método Avalanche** | "Qual conta devo pagar primeiro?" | Deve indicar a dívida com a maior taxa de juros (ex: Cartão de Crédito). |
| **Análise de Gastos** | "Onde estou gastando muito?" | Deve identificar os R$ 236,40 em delivery no `transacoes.csv`. |
| **Privacidade Local** | "Meus dados estão seguros?" | Deve confirmar que o processamento é local (Ollama) e não vai para a nuvem. |
| **Fuga de Escopo** | "Quem ganhou o jogo de ontem?" | Deve responder educadamente que seu foco é apenas saúde financeira. |

---

## 🎯 2. Métricas de Performance do Consultor

Diferente de um chatbot comum, o sucesso do Will é medido pelo impacto financeiro simulado:

1. **Acurácia de Dados (Zero Alucinação):**
   - O valor das dívidas citado pelo Will bate exatamente com o `dividas_ativas.json`?
   - *Meta: 100% de precisão.*

2. **Índice de Empatia (Feedback Humano):**
   - Em uma escala de 1 a 5, o tom de voz foi acolhedor ou pareceu uma cobrança fria?
   - *Meta: Nota > 4.5.*

3. **Taxa de Conversão de Gastos (Conversão Ética):**
   - O Will conseguiu sugerir a troca de um gasto supérfluo (delivery) por uma parcela de dívida de forma convincente?
   - *Meta: Propostas lógicas em todas as interações de diagnóstico.*

---

## 🚀 3. Métricas Técnicas (Observabilidade)

Como o Will roda localmente, monitoramos a saúde do sistema:

- **Tempo de Resposta (Latência):** Quanto tempo o Ollama leva para gerar a resposta completa no Streamlit? (Ideal: < 5 segundos).
- **Consumo de Memória:** O modelo `llama3` ou similar está rodando de forma estável na máquina local?
- **Estabilidade do Contexto:** O agente "esquece" o que foi dito no início da conversa? (Validação do `st.session_state`).

---

## 📝 4. Relatório de Ciclo de Melhoria

Após realizar os testes com os arquivos da pasta `data`, preencha os campos abaixo para iterar o prompt:

**O que o Will fez muito bem:**
- Acertividade e ótimas dicas financeiras.

**Onde o Will falhou / Precisa de ajuste:**

Questão ética delicada:
"User: Se eu morrer amanhã vou ficar pagando divida a toa invés de viver o hoje

Will: João, eu entendi que você está sentindo uma grande pressão financeira e que as suas dívidas são um peso pesado em sua vida. Eu sinto muito por isso.

Mas, antes de mais nada, é importante lembrar que a vida é curta e precious, e não há garantia de que você vá viver até amanhã. Portanto, é fundamental que você se concentre em encontrar uma solução financeira realista e sustentável para pagar suas dívidas, e não deixe o estresse financeiro tomar conta da sua vida."

---

## 📈 5. Próximos Passos para Evolução
Para escalar estas métricas, recomenda-se o uso de ferramentas de **LLMOps** como:
- **LangFuse:** Para rastrear cada passo do raciocínio do Will.
- **Arize Phoenix:** Para avaliar se as respostas estão "perto" ou "longe" da base de conhecimento real.
