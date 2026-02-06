import streamlit as st
import ollama
import json
import pandas as pd
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Will - Seu Guia Financeiro", page_icon="💰")

# --- AJUSTE DE CAMINHOS ---
# Definimos o caminho base subindo um nível a partir de onde o app.py está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data")

# --- CARREGAMENTO DE DADOS ---
def load_data():
    try:
        # Usamos os caminhos completos construídos dinamicamente
        with open(os.path.join(DATA_PATH, 'perfil_endividado.json'), 'r', encoding='utf-8') as f:
            perfil = json.load(f)
        
        with open(os.path.join(DATA_PATH, 'dividas_ativas.json'), 'r', encoding='utf-8') as f:
            dividas = json.load(f)
            
        transacoes = pd.read_csv(os.path.join(DATA_PATH, 'transacoes.csv'), encoding='utf-8')
        
        return perfil, dividas, transacoes
    except FileNotFoundError as e:
        st.error(f"Erro: Arquivo não encontrado no caminho: {DATA_PATH}")
        st.info("Verifique se a pasta 'data' está no mesmo nível da pasta 'src'.")
        return None, None, None

perfil, dividas, transacoes = load_data()

# --- DEFINIÇÃO DO SYSTEM PROMPT ---
SYSTEM_PROMPT = f"""
Você é o Will, um consultor financeiro empático e técnico.
Sua missão é ajudar o cliente a sair das dívidas usando os dados fornecidos.

DIRETRIZES:
1. Use os dados do perfil: {json.dumps(perfil)}
2. Analise as dívidas: {json.dumps(dividas)}
3. Considere os gastos recentes: {transacoes.to_dict() if transacoes is not None else 'Sem transações'}
4. NUNCA comprometa mais de 30% da renda mensal (R$ {perfil['situacao_financeira']['renda_mensal'] * 0.3 if perfil else 0}) em parcelas.
5. Seja motivador, use emojis e foco no método avalanche (juros maiores primeiro).
"""

# --- INTERFACE STREAMLIT ---
st.title("🤖 Will: Consultor de Saúde Financeira")
st.markdown("---")

# Sidebar com resumo do perfil
if perfil:
    st.sidebar.header("📊 Seu Perfil")
    st.sidebar.metric("Renda Mensal", f"R$ {perfil['situacao_financeira']['renda_mensal']:.2f}")
    st.sidebar.metric("Score", perfil['situacao_financeira']['score_credito'])
    st.sidebar.progress(perfil['situacao_financeira']['score_credito'] / 1000)

# Histórico de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("Como posso te ajudar com suas dívidas hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        # Chamada ao Ollama (Certifique-se que o serviço do Ollama está rodando)
        try:
            response = ollama.chat(
                model='llama3', # ou o modelo que você baixou (ex: 'mistral', 'gemma')
                messages=[
                    {'role': 'system', 'content': SYSTEM_PROMPT},
                    *st.session_state.messages
                ],
                stream=True
            )
            
            for chunk in response:
                full_response += chunk['message']['content']
                response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"Erro ao conectar com Ollama: {e}")

    st.session_state.messages.append({"role": "assistant", "content": full_response})
