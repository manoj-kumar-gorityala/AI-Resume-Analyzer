def skill_gap(user_skills):

    required = [
        "python",
        "machine learning",
        "sql",
        "statistics",
        "deep learning"
    ]

    missing = []

    for skill in required:
        if skill not in user_skills:
            missing.append(skill)

    return missing