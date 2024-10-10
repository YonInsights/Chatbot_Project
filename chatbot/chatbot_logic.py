import os
import sys

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from langchain_groq import ChatGroq  # Import ChatGroq for Groq API
from langchain.schema import HumanMessage, SystemMessage
from models.roadmap_generator import generate_roadmap  # Import the roadmap generator

# Set the API key for the Groq model
os.environ['My_AI'] = "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"
chat = ChatGroq(api_key=os.environ['My_AI'])  # Initialize ChatGroq with the API key

# Function to start the chatbot interaction
def start_chatbot(skill_level, goal, time_available, cv_content):
    # System message to introduce the bot
    system_message = SystemMessage(content="You are an AI that helps users create a roadmap to acquire new skills. Ask a maximum of 3 questions to understand their skill level.")
    
    # Initialize conversation with system message
    messages = [system_message]
    
    # Store user inputs in a dictionary
    user_inputs = {
        "current_skill_level": skill_level,
        "goal": goal,
        "time_available": time_available,
        "cv_content": cv_content
    }
    
    # Add the user's inputs to the conversation
    for key, value in user_inputs.items():
        human_message = HumanMessage(content=f"{key}: {value}")
        messages.append(human_message)
    
    # Send the messages to the model
    response = chat.invoke(messages)
    
    # Generate the roadmap based on user inputs and CV content
    roadmap = generate_roadmap(user_inputs, cv_content)  # Pass user inputs and CV content
    
    return roadmap

if __name__ == "__main__":
    # Example inputs for testing purposes
    roadmap = start_chatbot("Beginner", "Frontend", 10, "Example CV content")
    print(roadmap)
