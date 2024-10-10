# roadmap_generator.py

# Import any required libraries
import os

# Function to generate the learning roadmap
def generate_roadmap(user_input, cv_content):
    """
    Generate a personalized learning roadmap based on user input and CV.
    
    Parameters:
        user_input (dict): A dictionary containing the user's responses to the questions.
        cv_content (str): The content of the user's CV (parsed).
    
    Returns:
        dict: A structured roadmap with skills, learning materials, and time estimates.
    """
    
    # Sample predefined skills and learning materials (this could be dynamic in the future)
    roadmap = {
        "skills_to_learn": [],
        "learning_materials": [],
        "time_estimations": []
    }
    
    # Analyze user input
    if "data science" in user_input["goal"].lower():
        roadmap["skills_to_learn"] = ["Python", "SQL", "Data Visualization", "Machine Learning"]
        roadmap["learning_materials"] = [
            "Python for Data Science (Course)",
            "SQL Essentials for Data Analysts (Tutorial)",
            "Data Visualization using Matplotlib and Seaborn (Video Series)",
            "Machine Learning Basics (Book)"
        ]
        roadmap["time_estimations"] = [
            "3 weeks",  # Python
            "2 weeks",  # SQL
            "2 weeks",  # Data Visualization
            "4 weeks"   # Machine Learning
        ]
    
    # Add more conditions to match other learning paths
    # For example, if the user wants to transition into Web Development
    if "web development" in user_input["goal"].lower():
        roadmap["skills_to_learn"] = ["HTML", "CSS", "JavaScript", "React.js"]
        roadmap["learning_materials"] = [
            "Intro to HTML/CSS (Course)",
            "JavaScript for Beginners (Course)",
            "React.js Basics (Video Series)"
        ]
        roadmap["time_estimations"] = [
            "2 weeks",  # HTML/CSS
            "3 weeks",  # JavaScript
            "4 weeks"   # React.js
        ]
    
    # Future functionality could analyze CV content to further tailor the roadmap
    
    return roadmap
