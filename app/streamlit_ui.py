import streamlit as st
import fitz  # PyMuPDF
import docx
from chatbot.chatbot_logic import start_chatbot

def main():
    st.title("Skill Roadmap Chatbot")
    
    # CV Upload
    uploaded_file = st.file_uploader("Upload your CV", type=["pdf", "docx"])
    
    # User Inputs
    st.write("Please answer the following questions:")
    skill_level = st.selectbox("What is your current skill or experience level?", ["Beginner", "Intermediate", "Advanced"])
    goal = st.text_input("What new skill or field are you interested in learning?")
    time_available = st.number_input("How much time per week can you dedicate to learning this new skill?", min_value=1, max_value=40, step=1)
    
    if st.button("Generate Roadmap"):
        if uploaded_file is not None:
            # Extract text from the uploaded file
            cv_content = extract_text_from_file(uploaded_file)
            
            # Call the chatbot function with the extracted CV content and user inputs
            roadmap = start_chatbot(skill_level, goal, time_available, cv_content)
            
            # Display the roadmap
            st.write("Here is your personalized roadmap:")
            for i, skill in enumerate(roadmap["skills_to_learn"]):
                st.write(f"Skill: {skill}")
                st.write(f"Suggested Material: {roadmap['learning_materials'][i]}")
                st.write(f"Estimated Time: {roadmap['time_estimations'][i]}\n")
        else:
            st.write("Please upload your CV.")

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_docx(uploaded_file)
    else:
        return "Unsupported file type."

def extract_text_from_pdf(file):
    document = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in document:
        text += page.get_text()
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

if __name__ == "__main__":
    main()
