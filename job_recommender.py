def recommend_jobs(role):

    jobs = {

        "Data Scientist": [
            "Machine Learning Engineer",
            "AI Engineer",
            "Data Analyst",
        ],

        "Web Developer": [
            "Frontend Developer",
            "Full Stack Developer",
        ],

        "Software Engineer": [
            "Backend Developer",
            "System Engineer",
        ],
    }

    return jobs.get(role, [])