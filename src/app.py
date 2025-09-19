"""
App for chat with a debt negotiation agent.
"""

import streamlit as st

from agent import agent

if __name__ == "__main__":
    st.set_page_config(
        page_title="Agente de Negociação de Dívidas", page_icon="💬", layout="centered"
    )

    st.title("💬 Agente de IA para Negociação de Dívidas")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Faça uma pergunta ou envie uma mensagem"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Processando..."):
                result = agent.invoke({"input": prompt})

                if isinstance(result, dict) and "output" in result:
                    text_result = result["output"]
                else:
                    text_result = str(result)

                st.markdown(text_result)

        st.session_state.messages.append({"role": "assistant", "content": text_result})
