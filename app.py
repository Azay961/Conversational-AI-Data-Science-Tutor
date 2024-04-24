import streamlit as st
import google.generativeai as genai

st.title("Data Science Tutor chatbot")

f=open("D:/Innomatics/chatbot/.keys.txt")
key=f.read()


genai.configure(api_key = key)

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              system_instruction="""You are expert in "Data science fields". Your job is to provide the clear
                              explanation of the questions asked with polite manner. if a question is not related to "Data Science",
                              You can tell them to ask questions about "Data science" related topics only.
                              """)

if "Chat_history" not in st.session_state:
    st.session_state["chat_history"]=[]

chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].txt)

user_prompt = st.chat_input()

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response = chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state["chat_history"]=chat.history