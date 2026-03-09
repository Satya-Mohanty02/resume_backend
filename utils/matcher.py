def match_resume(resume_skills, jd_skills):

    if len(jd_skills) == 0:
        return 0

    matched = len(set(resume_skills) & set(jd_skills))

    score = (matched / len(jd_skills)) * 100

    return round(score,2)