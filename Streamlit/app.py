import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage
from  api_calls import api_call_question,get_chat_history




# if "chat_history" not in st.session_state:
#     st.session_state['chat_history'] =[]

messages =get_chat_history()

st.title("Ask Blue Chatbot")

st.sidebar.title('Bluechip Technologies Self Service Bot ')
st.sidebar.markdown("""
**Welcome to the Bluechip Technologies Self Service Bot.**

This bot is designed to assist internal staff with various information about the companies policies,benefits and every important company information.
""")
st.sidebar.markdown("---")
st.sidebar.markdown("Powered by BlueChip Technologies Data science team  | [Visit our website](https://bluechiptech.biz/)")
#conversation
for message in messages:
    if  message['type'] =="human":
        with st.chat_message("Human"):
            st.markdown(message['content'])
        
    else:
        with st.chat_message("Ai"):
            st.markdown(message['content'])


user_input = st.chat_input("Enter your message:")
if user_input is not None and user_input != "":
    with st.chat_message("Human"):
        st.markdown(user_input)

    with st.chat_message("Ai"):
        ai_answer =api_call_question(user_input)
        st.markdown(ai_answer)

 

