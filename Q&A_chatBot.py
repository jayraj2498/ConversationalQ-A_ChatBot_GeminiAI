from dotenv import load_dotenv 
load_dotenv() 

import os 
import streamlit as st 
import google.generativeai as genai 


genai.configure(api_key=os.getenv('GOOGLE_API_KEY')) 

model= genai.GenerativeModel("gemini-pro") 

chat=model.start_chat(history=[])

def get_gemini_respone(question): 
    response=chat.send_message(question,stream=True)
    return response 

st.set_page_config(page_title="Q&A Demo")
st.title("Gemini LLM Q&A Application App ")

# if "chat_history" is not present then we create it (initiallize the chat history if it dosent Exit)  

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [] 
    
    
input= st.text_input("Input" , key="input") 
submit=st.button("Enter Here :") 

if submit and input : 
    response=get_gemini_respone(input) 
    # we are adding user input history in our chat_history 
    st.session_state["chat_history"].append(("Input Command." , input) )
    st.subheader("The Response is:") 
    
    for chunk in response : 
        st.write(chunk.text) 
        st.session_state["chat_history"].append(("BoT Response is :" , chunk.text)) 
    
st.subheader("All Chat history is :") 

for role , text in st.session_state["chat_history"]:
    st.write(f"{role} :{text}")

    
    

# --------------------------------------------------------------
# def get_gemini_respone(question): 
#     response=model.generate_content(question)
#     return response.text 

# Q= input("enter your Question :") 
# answer=get_gemini_respone(Q)

# print(answer)
# --------------------------------------------------------------