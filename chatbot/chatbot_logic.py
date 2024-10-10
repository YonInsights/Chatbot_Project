import os
import sys
from langchain_groq import ChatGroq  # Import ChatGroq for Groq API
from langchain.schema import HumanMessage, SystemMessage
from models.roadmap_generator import generate_roadmap  # Import the roadmap generator

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
    
    # Specific questions based on CV summary
    questions = [
        f"Based on your CV, I understand you have experience in {cv_summary}. What is your current skill or experience level?",
        f"What new skill or field are you interested in learning?",
        f"How much time per week can you dedicate to learning this new skill?"
    ]

    # Collect user responses
    user_inputs = {}
    for question in questions:
        print(question)
        user_input = input("Your response: ")
        user_inputs[question] = user_input

    # Generate the roadmap based on user inputs and CV summary
    roadmap = generate_roadmap(user_inputs, cv_summary)  # Pass user inputs and CV summary
    
    return roadmap

if __name__ == "__main__":
    # Example inputs for testing purposes
    skill_level = "Intermediate"
    goal = "Frontend"
    time_available = 3
    cv_content = "Example CV content"
    
    roadmap = start_chatbot(cv_content, skill_level, goal, time_available)
    print("\nGenerated Roadmap:")
    print(roadmap)
