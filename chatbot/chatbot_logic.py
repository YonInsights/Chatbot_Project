import os
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage

# Set the API key for the Groq model
os.environ['My_AI'] = "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"
chat = ChatGroq(api_key=os.environ['My_AI'])

def generate_roadmap(user_inputs):
    # Dummy logic to handle user inputs, assuming `time_available` is in hours per week
    roadmap_data = {
        "skills_to_learn": [],
        "learning_materials": [],
        "time_estimations": []
    }

    time_per_week = user_inputs['time_available']
    
    # Dummy hardcoded roadmap (you can modify based on real API response)
    roadmap_text = """
        Weeks 1-4: HTML, CSS, responsive design, videos from Codecademy, FreeCodeCamp.
        Weeks 5-8: JavaScript fundamentals, interactive web pages, DOM manipulation.
        Weeks 9-12: Frontend frameworks (React/Vue.js), state management.
        Weeks 13-16: Testing, debugging, Git/GitHub.
        Weeks 17-20: Accessibility, performance optimization.
    """
    
    # Adjust the number of weeks based on time available
    weeks_factor = 40 / time_per_week  # Assuming 40 hours per week for a full roadmap
    roadmap_steps = roadmap_text.strip().split("Weeks")

    # Parse roadmap and adjust time accordingly
    for step in roadmap_steps[1:]:
        week_range, content = step.split(":")
        content = content.strip()
        
        # Estimate time for each segment based on the `weeks_factor`
        skill_week = f"Weeks {week_range.strip()}"
        estimated_time = f"{int((int(week_range.split('-')[1]) - int(week_range.split('-')[0]) + 1) * weeks_factor)} weeks"
        
        roadmap_data["skills_to_learn"].append(skill_week)
        roadmap_data["learning_materials"].append(content)
        roadmap_data["time_estimations"].append(estimated_time)
    
    return roadmap_data

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
