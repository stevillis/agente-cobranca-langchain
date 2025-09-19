"""
This module provides a debt negotiation agent.
"""

from langchain.agents import AgentType, initialize_agent
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import MessagesPlaceholder
from langchain_openai import ChatOpenAI

from prompts import system_message
from tools import NegociacaoTools

llm = ChatOpenAI(model_name="gpt-4.1-nano", temperature=0)

tools = [
    NegociacaoTools.consultar_cpf,
    NegociacaoTools.ver_divida,
    NegociacaoTools.ver_acordo,
    NegociacaoTools.registrar_acordo,
]

memory = ConversationBufferWindowMemory(
    memory_key="chat_history",
    return_messages=True,
)

agent_kwargs = {
    "extra_prompt_messages": [
        MessagesPlaceholder(variable_name="chat_history"),
        system_message,
    ],
}

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    memory=memory,
    agent_kwargs=agent_kwargs,
    verbose=True,
)
