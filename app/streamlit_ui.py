import streamlit as st
import fitz  # PyMuPDF
import docx
import os
import sys

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chatbot.chatbot_logic import start_chatbot
from fpdf import FPDF

def main():
    st.title("Skill Roadmap Chatbot")
    
    # CV Upload
    uploaded_file = st.file_uploader("Upload your CV", type=["pdf", "docx"])
    
    # User Inputs
    st.write("Please answer the following questions:")
    skill_level = st.selectbox("What is your current skill or experience level?", ["Beginner", "Intermediate", "Advanced"])
    goal = st.text_input("What specific skill or field are you interested in learning or improving?")
    time_available = st.number_input("How many hours per week can you dedicate to learning this new skill?", min_value=1, max_value=40, step=1)
    
    if st.button("Generate Roadmap"):
        if uploaded_file is not None:
            # Extract text from the uploaded file
            cv_content = extract_text_from_file(uploaded_file)
            
            # Call the chatbot function with the extracted CV content and user inputs
            cv_summary, roadmap = start