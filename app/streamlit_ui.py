import streamlit as st
import os
import sys
from fpdf import FPDF
from io import BytesIO

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from chatbot.chatbot_logic import start_chatbot  # Correct import for chatbot_logic

def main():
    st.title("Skill Roadmap Chatbot")
    
    # User Inputs
    st.write("Please answer the following questions:")
    skill_level = st.selectbox("What is your current skill or experience level?", ["Beginner", "Intermediate", "Advanced"])
    goal = st.text_input("What new skill or field are you interested in learning?")
    time_available = st.number_input("How much time per week can you dedicate to learning this new skill?", min_value=1, max_value=40, step=1)
    learning_preference = st.selectbox("What is your preferred learning style?", ["Hands-on projects", "Reading", "Watching videos", "Interactive tutorials"])
    target_industry = st.text_input("What industry are you targeting for your new skills?")

    if st.button("Generate Roadmap"):
        # Call the chatbot function with the user inputs
        roadmap = start_chatbot(skill_level, goal, time_available, learning_preference, target_industry)
        
        # Display the roadmap in a table
        st.write("Here is your personalized roadmap:")
        st.table({
            "Skill": roadmap["skills_to_learn"],
            "Suggested Material": roadmap["learning_materials"],
            "Estimated Time": roadmap["time_estimations"]
        })
        
        # Add motivational section
        st.write("Remember, consistency is key to mastering new skills. Believe in yourself and stay dedicated. You can do this!")
        
        # Generate PDF content
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
            
        pdf.cell(200, 10, txt="Personalized Study Roadmap", ln=True, align="C")
        pdf.ln(10)
            
        for skill, material, time in zip(roadmap["skills_to_learn"], roadmap["learning_materials"], roadmap["time_estimations"]):
            pdf.cell(200, 10, txt=f"Skill: {skill}", ln=True)
            pdf.cell(200, 10, txt=f"Suggested Material: {material}", ln=True)
            pdf.cell(200, 10, txt=f"Estimated Time: {time}", ln=True)
            pdf.ln(5)
            
        pdf.ln(10)
        pdf.cell(200, 10, txt="Motivational Section:", ln=True)
        pdf.multi_cell(0, 10, txt="Remember, consistency is key to mastering new skills. Believe in yourself and stay dedicated. You can do this!")
        
        pdf_output = BytesIO()
        pdf.output(pdf_output)
        pdf_output.seek(0)
        
        # Provide download button
        st.download_button(
            label="Download Roadmap as PDF",
            data=pdf_output,
            file_name="roadmap.pdf",
            mime="application/pdf",
        )

if __name__ == "__main__":
    main()
