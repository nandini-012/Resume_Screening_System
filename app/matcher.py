def match_skills(resume_skills, jd_skills):

    matched = []

    missing = []
    
    resume_skills_lower = [
    skill.lower()
    for skill in resume_skills
]

    for skill in jd_skills:

        if skill.lower() in resume_skills_lower:
            matched.append(skill)

        else:
            missing.append(skill)

    if len(jd_skills) == 0:

        return {
        "score": 0,
        "matched": [],
        "missing": []
    }

    score = (
    len(matched)
    /
    len(jd_skills)
    ) * 100

    return {
        "score": round(score, 2),
        "matched": matched,
        "missing": missing
        }