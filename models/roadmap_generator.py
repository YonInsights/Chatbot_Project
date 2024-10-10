def generate_roadmap(user_inputs, cv_content):
    skills_to_learn = []
    learning_materials = []
    time_estimations = []

    # Logic to generate a roadmap based on user inputs and CV content
    goal = user_inputs["goal"].lower()
    
    if "frontend" in goal:
        skills_to_learn.extend(["HTML & CSS", "JavaScript Basics"])
        learning_materials.extend([
            "HTML & CSS by Jon Duckett",
            "Eloquent JavaScript by Marijn Haverbeke"
        ])
        time_estimations.extend(["4 weeks", "6 weeks"])

    # More logic based on user_inputs and cv_content

    return {
        "skills_to_learn": skills_to_learn,
        "learning_materials": learning_materials,
        "time_estimations": time_estimations
    }
