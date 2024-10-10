import os
from langchain_groq import ChatGroq  # Import ChatGroq for Groq API
from langchain.schema import HumanMessage, SystemMessage
from models.roadmap_generator import generate_roadmap  # Import the roadmap generator
import streamlit as st

# Set the API key for the Groq model
os.environ['My_AI'] = "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"
chat = ChatGroq(api_key=os.environ['My_AI'])  # Initialize ChatGroq with the API key

def analyze_cv(cv_content):
    # Send the CV content to the model and get a summary
    system_message = SystemMessage(content="You are an AI that helps users create a roadmap to acquire new skills.")
    messages = [system_message, HumanMessage(content=cv_content)]
    response = chat.invoke(messages)
    return response.content

def start_chatbot(cv_content, skill_level, goal, time_available):
    cv_summary = analyze_cv(cv_content)
    
    # Instead of asking questions via input, use Streamlit to collect responses
    st.write(f"Based on your CV, I understand you have experience in {cv_summary}.")
    skill_level = st.selectbox("What is your current skill or experience level?", ["Beginner", "Intermediate", "Advanced"])
    goal = st.text_input("What new skill or field are you interested in learning?")
    time_available = st.slider("How much time per week can you dedicate to learning this new skill?", 1, 20, 5)
    
    # Generate the roadmap based on user inputs and CV summary
    if st.button("Generate Roadmap"):
        roadmap = generate_roadmap({"skill_level": skill_level, "goal": goal, "time_available": time_available}, cv_summary)
        return roadmap
    return None
