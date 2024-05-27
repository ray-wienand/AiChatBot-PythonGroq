import os
import streamlit as st
from langchain.chains.conversation.memory import ConversationBufferWindowMemory


from langchain.chains import ConversationChain, LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate


from dotenv import load_dotenv

load_dotenv()

st.title("Chat with the Machine Learning Tutor")
st.write("Hello! I'm your Machine Learning tutor. I can tutor you, or answer your questions. Ask me about anything else and I will give you a mouthful!")

conversational_memory_length = 10 # Remembers the last 10 messages
memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)

 # session state variable
if 'chat_history' not in st.session_state:
    st.session_state.chat_history=[]
else:
    for message in st.session_state.chat_history:
        memory.save_context(
            {'input':message['human']},
            {'output':message['AI']}
            )


# Initialize Groq Langchain chat object and conversation
groq_chat = ChatGroq(
        groq_api_key=os.environ.get("GROQ_API_KEY"),   
        model_name="llama3-8b-8192",
)


user_question = st.text_input("Ask a question:")
# If the user has asked a question,
if user_question:

    # Construct a chat prompt template using various components
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content="You are a Machine Learning Algorithms expert tutor. You must guide me and tutor me through my learning journey. You are not allowed to answer any question or provide any information that are not Machine Learning Algorithms related. If anyone asks you a question or guidance on other topics you must reply with a sarcastic answer informing them that you cannot assist them and don't feel like wasting your time to learn about other topics, Your answers should be maximum three paragraphs if possible and preferably a sentence should not be longer than twenty seven words."
            ),  # This is the persistent system prompt that is always included at the start of the chat.

            MessagesPlaceholder(
                variable_name="chat_history"
            ),  # This placeholder will be replaced by the actual chat history during the conversation. It helps in maintaining context.

            HumanMessagePromptTemplate.from_template(
                "{human_input}"
            ),  # This template is where the user's current input will be injected into the prompt.
        ]
    )

    # Create a conversation chain using the LangChain LLM (Language Learning Model)
    conversation = LLMChain(
        llm=groq_chat,  # The Groq LangChain chat object initialized earlier.
        prompt=prompt,  # The constructed prompt template.
        verbose=True,   # Enables verbose output, which can be useful for debugging.
        memory=memory,  # The conversational memory object that stores and manages the conversation history.
    )
    
    # The chatbot's answer is generated by sending the full prompt to the Groq API.
    response = conversation.predict(human_input=user_question)
    message = {'human':user_question,'AI':response}
    st.session_state.chat_history.append(message)
    st.write("Chatbot:", response)