import os
import sys
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
from models.roadmap_generator import generate_roadmap

# Set the API key for the Groq model
os.environ['My_AI'] = "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"
chat = ChatGroq(api_key=os.environ['My_AI'])

def summarize_cv(cv_content):
    # Summarize CV content (placeholder implementation)
    summary = f"Summary of CV: {cv_content[:200]}..."  # Take first 200 characters as summary
    return summary

def start_chatbot(cv_content):
    cv_summary = summarize_cv(cv_content)
    
    # System message with CV summary
    system_message = SystemMessage(content=f"You are an AI that helps users create a roadmap to acquire new skills. Here is the user's CV summary: {cv_summary} Based on this, ask 3 questions to understand what skills they need to develop.")
    
    # Initialize conversation with system message
    messages = [system_message]
    
    # Questions for the user
    questions = [
        "From your CV, it looks like you have experience in [current experience]. What is your current skill or experience level?",
        "What new skill or field are you interested in learning?",
        "How much time per week can you dedicate to learning this new skill?"
    ]
    
    user_inputs = {}
    
    # Loop through and ask the user 3 questions
    for i, question in enumerate(questions):
        # Display the question to the user
        print(question)
        
        # Get the user's input
        user_input = input("Your response: ")
        
        # Store user input
        user_inputs[f"question_{i+1}"] = user_input
        
        # Add the user's message to the conversation
        human_message = HumanMessage(content=user_input)
        messages.append(human_message)
    
    # Send the messages to the model
    response = chat.invoke(messages)
    
    # Generate the roadmap based on user inputs and CV content
    roadmap = generate_roadmap(user_inputs, cv_content)
    
    return cv_summary, roadmap

if __name__ == "__main__":
    # Example CV content for testing purposes
    cv_content = "Example CV content with detailed information about the person's experience and skills."
    
    cv_summary, roadmap = start_chatbot(cv_content)
    print("\nCV Summary:")
    print(cv_summary)
    print("\nGenerated Roadmap:")
    print(roadmap)
