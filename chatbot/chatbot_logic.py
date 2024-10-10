import os
import sys

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from langchain_groq import ChatGroq  # Import ChatGroq for Groq API
from langchain.schema import HumanMessage, SystemMessage
from models.roadmap_generator import generate_roadmap  # Import the roadmap generator

# Set the API key for the Groq model
os.environ['My_AI'] = "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"
chat = ChatGroq(api_key=os.environ['My_AI'])  # Initialize ChatGroq with the API key

def start_chatbot(skill_level, goal, time_available, cv_content):
    # System message to introduce the bot
    system_message = SystemMessage(content="You are an AI that helps users create a roadmap to acquire new skills. You have analyzed the CV to understand the user's background. Ask up to 3 questions to further clarify their learning needs.")
    
    # Initialize conversation with system message
    messages = [system_message]
    
    # Summarize CV
    cv_summary = summarize_cv(cv_content)
    messages.append(SystemMessage(content=f"CV Summary: {cv_summary}"))
    
    # Store user inputs in a dictionary
    user_inputs = {
        "current_skill_level": skill_level,
        "goal": goal,
        "time_available": time_available
    }
    
    # Add the user's inputs to the conversation
    for key, value in user_inputs.items():
        human_message = HumanMessage(content=f"{key.replace('_', ' ').capitalize()}: {value}")
        messages.append(human_message)
    
    # Send the messages to the model
    response = chat.invoke(messages)
    
    # Generate the roadmap based on user inputs and CV content
    roadmap = generate_roadmap(user_inputs, cv_content)  # Pass user inputs and CV content
    
    return cv_summary, roadmap

def summarize_cv(cv_text):
    # Simple summarization logic (can be improved with NLP techniques)
    sentences = cv_text.split('.')
    summary = ' '.join(sentences[:3])  # Taking the first 3 sentences as summary
    return summary

if __name__ == "__main__":
    # Example inputs for testing purposes
    skill_level = "Beginner"
    goal = "Frontend"
    time_available = 10
    cv_content = "Example CV content"
    
    cv_summary, roadmap = start_chatbot(skill_level, goal, time_available, cv_content)
    print("\nCV Summary:")
    print(cv_summary)
    print("\nGenerated Roadmap:")
    print(roadmap)
