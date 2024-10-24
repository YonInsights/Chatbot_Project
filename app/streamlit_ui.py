import streamlit as st
import os
import sys
from fpdf import FPDF
from io import BytesIO
from PIL import Image

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from chatbot.chatbot_logic import start_chatbot  
# Correct import for chatbot_logic

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_margins(25.4, 25.4, 25.4)  
        # Set 1-inch margins (25.4 mm)
        self.first_page = True

    def header(self):
        if self.first_page:
            # Add logo at the header (top right)
            self.image(r"D:\Project_1\skill_roadmap_chatbot\Icon bleu2 Eleka.png", x=170, y=8, w=30)  
            # Adjust size and position
            self.set_font("Times", 'B', 16)  
            # Header font size
            self.cell(0, 10, 'Personalized Study Roadmap', 0, 1, 'C')
            self.set_font("Times", 'I', 12)  
            # Slogan font size
            self.cell(0, 10, 'Study Today, Succeed Tomorrow!', 0, 1, 'C')
            self.ln(5)
            # Add rocket icon in header
            self.image(r"D:\Project_1\skill_roadmap_chatbot\Icons\Rocket_Icon.png", x=10, y=8, w=30)  
            # Adjust path, size, and position
            self.first_page = False
        else:
            self.set_font("Times", 'I', 12)  # Slogan font size
            self.cell(0, 10, 'Study Today, Succeed Tomorrow!', 0, 1, 'C')
            self.ln(5)

    def footer(self):
        # Add footer with social media icons
        self.set_y(-15)
        self.set_font("Times", 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 1, 'C')
        self.ln(5)
        # Social media icons
        self.image(r"D:\Project_1\skill_roadmap_chatbot\Icons\facebook-logo.png", x=10, w=10) 
         # Adjust path, size, and position
        self.image(r"D:\Project_1\skill_roadmap_chatbot\Icons\telegram.png", x=25, w=10)  
        # Adjust path, size, and position
        self.image(r"D:\Project_1\skill_roadmap_chatbot\Icons\linkedin.png", x=40, w=10) 
         # Adjust path, size, and position
        self.image(r"D:\Project_1\skill_roadmap_chatbot\Icons\instagram.png", x=55, w=10) 
         # Adjust path, size, and position

    def chapter_title(self, title):
        self.set_font("Times", 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Times", '', 12)
        self.multi_cell(0, 10, body)  # Set to a line height of 10
        self.ln(0)  # No additional line spacing after the paragraph

    def add_bullet_points(self, items, indent=10):
        """Add bullet points for suggested materials with dynamic indent."""
        self.set_font("Times", '', 12)
        for item in items:
            self.cell(indent)  # Indent for bullet points
            # Add yellow star bullet point icon
            self.image(r"D:\Project_1\skill_roadmap_chatbot\Icons\star.png", x=self.get_x(), y=self.get_y(), w=5)  # Adjust path, size, and position
            self.cell(indent + 0.2)  # Adjust text indentation to avoid overlap with icon
            if "http" in item:  # Check if it's a link
                self.set_text_color(0, 0, 255)  # Set link color to blue
                self.cell(0, 10, item, ln=1, link=item)  # Create clickable link
            else:
                self.set_text_color(0, 0, 0)  # Reset color for normal text
                self.cell(0, 10, item, ln=1)

    def add_summary_table(self, weeks, materials, estimated_times):
        self.set_font("Times", 'B', 10)
        self.cell(30, 10, "Week", border=1)
        self.cell(100, 10, "Suggested Material", border=1)
        self.cell(30, 10, "Estimated Time", border=1)
        self.ln()
        self.set_font("Times", '', 10) 
         # Set the table body font size to 10
        for week, material, estimated_time in zip(weeks, materials, estimated_times):
            self.cell(30, 10, week, border=1)
            self.multi_cell(100, 10, material, border=1, align='L') 
             # Ensure content wraps within the cell
            self.cell(30, -10, estimated_time, border=1)
            self.ln(0)  
            # Ensure no additional line spacing after the row

def calculate_estimated_time(weeks, time_available):
    estimated_times = [f"{time_available} hours" for _ in weeks]
    return estimated_times

def generate_resources(goal):
    # Generate dynamic resources based on the user's goal
    resources = [
        f"https://www.udemy.com/course/{goal.replace(' ', '-')}",
        f"https://www.coursera.org/search?query={goal.replace(' ', '%20')}",
        f"https://www.youtube.com/results?search_query={goal.replace(' ', '+')}",
        f"https://www.edx.org/learn/{goal.replace(' ', '-')}",
        f"https://medium.com/tag/{goal.replace(' ', '-')}"
    ]
    return resources

def generate_motivational_story(goal, target_industry):
    # Create a motivational story based on the user's goal and target industry
    story = (f"There was once a professional who wanted to excel in {goal} within the {target_industry} industry. "
             f"Despite having no prior experience, they dedicated an hour each day to learning. "
             f"Over time, their dedication paid off, and they not only mastered {goal} but also "
             f"landed a dream job in {target_industry}. The key to success was consistency, belief in the process, "
             f"and a commitment to never give up.")
    return story

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

        # Ensure the roadmap is a dictionary and contains the expected keys
        if isinstance(roadmap, dict) and "skills_to_learn" in roadmap and "learning_materials" in roadmap and "time_estimations" in roadmap:
            st.write("Roadmap is not None:", roadmap)

            # Prepare data for the PDF
            skills_to_learn = roadmap["skills_to_learn"]
            learning_materials = roadmap["learning_materials"]
            time_estimations = roadmap["time_estimations"]

            # Generate PDF content
            pdf = PDF()
            pdf.add_page()
            pdf.set_font("Times", '', 12)

            # Introduction Section
            introduction = ("Welcome to your personalized skill development roadmap! This roadmap is tailored to "
                            "help you acquire the necessary skills for your future career. We understand your learning "
                            "preferences and time constraints, and have created a step-by-step guide for you to follow.\n\n"
                            "By following this roadmap, you'll progress through several key milestones, mastering "
                            "the essential skills for backend development. Stay committed, and you'll be amazed at your progress!")
            pdf.chapter_body(introduction)

            # Add dynamic motivational story based on user input
            motivational_story = generate_motivational_story(goal, target_industry)
            pdf.chapter_body(motivational_story)

            # Add dynamic resources based on user input
            resources = generate_resources(goal)

            # Add all weeks, materials, and estimated times to PDF
            for week, material, estimated_time in zip(skills_to_learn, learning_materials, time_estimations):
                pdf.chapter_title(f"Week: {week}")
                pdf.add_bullet_points(material.split("\n"), indent=13)  # Add bullet points for materials
                pdf.add_bullet_points(resources, indent=15)  # Add dynamic resources for each topic with 1-inch indent
                pdf.chapter_body(f"Estimated Time: {estimated_time}")

            # Add a summary table at the end of the PDF
            pdf.chapter_title("Summary of Roadmap")
            pdf.add_summary_table(skills_to_learn, learning_materials, time_estimations)

            # Prepare PDF for download
            pdf_output = BytesIO()
            pdf.output(pdf_output, 'S')  # Output PDF to BytesIO stream
            pdf_output.seek(0)

            # Provide download button
            st.download_button(
                label="Download Roadmap as PDF",
                data=pdf_output.getvalue(),
                file_name="roadmap.pdf",
                mime="application/pdf",
            )
        else:
            st.write("No roadmap generated. Please ensure all inputs are correct.")

if __name__ == "__main__":
    main()
