def generate_roadmap(user_inputs, cv_content):
    skills_to_learn = []
    learning_materials = []
    time_estimations = []

    # Debug: Print user inputs and CV content for troubleshooting
    print("\n[DEBUG] generate_roadmap() called with the following parameters:")
    print(f"user_inputs: {user_inputs}")
    print(f"cv_content: {cv_content}")

    # Example logic to generate a roadmap based on user inputs and CV content
    if user_inputs["current_skill_level"].lower() == "beginner":
        if "frontend" in user_inputs["goal"].lower():
            skills_to_learn.extend(["HTML & CSS", "JavaScript Basics"])
            learning_materials.extend([
                "HTML & CSS by Jon Duckett",
                "Eloquent JavaScript by Marijn Haverbeke"
            ])
            time_estimations.extend(["4 weeks", "6 weeks"])

    # Add more logic based on cv_content and other user inputs

    return {
        "skills_to_learn": skills_to_learn,
        "learning_materials": learning_materials,
        "time_estimations": time_estimations
    }
