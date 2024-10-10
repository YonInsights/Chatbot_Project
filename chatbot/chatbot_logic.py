# chatbot_logic.py

import os
from langchain_groq import ChatGroq  # Import ChatGroq for Groq API
from langchain.schema import HumanMessage, SystemMessage
from models.roadmap_generator import generate_roadmap  # Import the roadmap generator

# Set the API key for the Groq model
os.environ['My_AI'] = "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"
chat = ChatGroq(api_key=os.environ['My_AI'])  # Initialize ChatGroq with the API key

# Function to start the chatbot interaction
def start_chatbot():
    # System message to introduce the bot
    system_message = SystemMessage(content="You are an AI that helps users create a roadmap to acquire new skills. Ask a maximum of 3 questions to understand their skill level.")
    
    # Questions for the user
    questions = [
        "What is your current skill or experience level?",
        "What new skill or field are you interested in learning?",
        "How much time per week can you dedicate to learning this new skill?"
    ]
    
    # Initialize conversation with system message
    messages = [system_message]
    
    # Dictionary to store user inputs
    user_inputs = {}

    # Loop through and ask the user 3 questions
    for i, question in enumerate(questions):
        print(question)
        user_input = input("Your response: ")
        
        # Store the user input in a dictionary
        if i == 0:
            user_inputs["current_skill_level"] = user_input
        elif i == 1:
            user_inputs["goal"] = user_input
        elif i == 2:
            user_inputs["time_available"] = user_input
        
        # Add the user's message to the conversation
        human_message = HumanMessage(content=user_input)
        messages.append(human_message)
    
    # Once the user has answered the questions, send the messages to the model
    response = chat.invoke(messages)
    
    # Print the AI's response (for now, we'll print it; later, we'll display it on Streamlit)
    print("\nAI Response:")
    print(response.content)
    
    # Generate the roadmap based on user inputs and an empty CV content
    roadmap = generate_roadmap(user_inputs, cv_content="")  # Pass user inputs and CV content
    
    # Display the roadmap to the user
    print("\nHere is your personalized roadmap:")
    for i, skill in enumerate(roadmap["skills_to_learn"]):
        print(f"Skill: {skill}")
        print(f"Suggested Material: {roadmap['learning_materials'][i]}")
        print(f"Estimated Time: {roadmap['time_estimations'][i]}\n")

# For testing purposes, you can run the chatbot here
if __name__ == "__main__":
    start_chatbot()
