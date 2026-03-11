def ats_score(resume):

    keywords = [
        "python","machine learning","deep learning",
        "data analysis","sql","tensorflow","pandas"
    ]

    score = 0

    for word in keywords:
        if word in resume:
            score += 1

    ats = (score / len(keywords)) * 100

    return int(ats)