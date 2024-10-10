import os
from langchain_groq import ChatGroq  # Import ChatGroq for Groq API
from langchain.schema import HumanMessage, SystemMessage
from models.roadmap_generator import generate_roadmap  # Import the roadmap generator

# Set the API key for the Groq model
os.environ['My_AI'] = "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"
chat = ChatGroq(api_key=os.environ['My_AI'])  # Initialize ChatGroq with the API key

def start_chatbot(skill_level, goal, time_available, learning_preference, target_industry):
    # Collect user inputs into a dictionary
    user_inputs = {
        "skill_level": skill_level,
        "goal": goal,
        "time_available": time_available,
        "learning_preference": learning_preference,
        "target_industry": target_industry
    }

    # Generate the roadmap based on user inputs
    roadmap = generate_roadmap(user_inputs)  # Pass user inputs
    
    return roadmap

if __name__ == "__main__":
    # Example inputs for testing purposes
    skill_level = "Intermediate"
    goal = "Frontend"
    time_available = 10
    learning_preference = "Hands-on projects"
    target_industry = "Tech"

    roadmap = start_chatbot(skill_level, goal, time_available, learning_preference, target_industry)
    print("\nGenerated Roadmap:")
    print(roadmap)
