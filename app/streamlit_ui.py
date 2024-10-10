import streamlit as st
from io import BytesIO
from PyPDF2 import PdfReader
import docx
from chatbot_logic import start_chatbot

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_docx(uploaded_file)
    else:
        return "Unsupported file type."

def extract_text_from_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def main():
    st.title("AI Career Roadmap Generator")
    
    uploaded_file = st.file_uploader("Upload your CV (PDF or DOCX)", type=["pdf", "docx"])
    
    if uploaded_file:
        cv_content = extract_text_from_file(uploaded_file)
        st.write("CV uploaded and analyzed successfully!")
        
        # Call the chatbot logic to process the CV and generate a roadmap
        roadmap = start_chatbot(cv_content, None, None, None)
        
        if roadmap:
            # Display the roadmap in a table format
            st.write("Generated Roadmap:")
            for skill, material, time in zip(roadmap["skills_to_learn"], roadmap["learning_materials"], roadmap["time_estimations"]):
                st.write(f"Skill: {skill}, Suggested Material: {material}, Estimated Time: {time} weeks")
            
            # Generate PDF download
            generate_pdf(roadmap)
    
def generate_pdf(roadmap):
    from fpdf import FPDF
    
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
    
    # Output the PDF as a downloadable file
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)
    
    st.download_button(
        label="Download Roadmap as PDF",
        data=pdf_output,
        file_name="roadmap.pdf",
        mime="application/pdf",
    )

if __name__ == "__main__":
    main()
