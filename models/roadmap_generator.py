import json
from langchain_groq import ChatGroq  # Import ChatGroq for Groq API

# Initialize ChatGroq with the API key
chat = ChatGroq(api_key="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")

def generate_roadmap(user_inputs):
    # Prepare the prompt for the ChatGroq model
    prompt = f"""
    You are a roadmap generator AI. Based on the following user inputs, create a personalized learning roadmap.
    Skill Level: {user_inputs['skill_level']}
    Goal: {user_inputs['goal']}
    Time Available: {user_inputs['time_available']} hours per week
    Learning Preference: {user_inputs['learning_preference']}
    Target Industry: {user_inputs['target_industry']}
    
    Please respond with a JSON object in the following format:
    {{
        "skills_to_learn": ["skill1", "skill2", ...],
        "learning_materials": ["material1", "material2", ...],
        "time_estimations": ["time1", "time2", ...]
    }}
    Do not include any additional text or explanations.
    """
    
    # Call the ChatGroq model with the prompt
    response = chat.ask(prompt)
    
    # Print the raw response for debugging purposes
    print("Raw Response from ChatGroq:", response)
    print("Type of Raw Response:", type(response))  # Print the type of response

    # Ensure the response is a string before processing
    if isinstance(response, str):
        response = response.strip()
    
    # Attempt to parse the response as JSON
    try:
        roadmap_data = json.loads(response)
        # Debugging output: Print the type of the parsed data
        print("Parsed roadmap data:", roadmap_data)
        print("Type of Parsed Data:", type(roadmap_data))

        # Check if the parsed data is a valid dictionary with expected keys
        if isinstance(roadmap_data, dict) and all(
            key in roadmap_data for key in ["skills_to_learn", "learning_materials", "time_estimations"]
        ):
            return roadmap_data
        else:
            print("Invalid JSON structure in response")
            return {"skills_to_learn": [], "learning_materials": [], "time_estimations": []}

    except json.JSONDecodeError as e:
        print("JSON Parse Error:", e)  # Print the error for debugging
        print("Response was:", response)  # Show what the response was
        return {"skills_to_learn": [], "learning_materials": [], "time_estimations": []}

