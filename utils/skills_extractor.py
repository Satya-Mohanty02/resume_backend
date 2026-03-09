skills_list = [
"python","java","c++","machine learning","react",
"node","sql","mongodb","flask","django",
"html","css","javascript","aws","docker",
"linux","bootstrap","kali","networking",
"ethical hacking","penetration testing"
]

#skills mapping
domain_skills = {

"web development":[
"html","css","javascript","react","node","bootstrap"
],

"frontend developer":[
"html","css","javascript","react","bootstrap","ui","ux"
],

"backend developer":[
"python","java","node","django","flask","sql","mongodb"
],

"software engineering":[
"java","python","c++","data structures","algorithms","git"
],

"data science":[
"python","machine learning","pandas","numpy","data analysis","matplotlib"
],

"machine learning":[
"python","machine learning","deep learning","tensorflow","pytorch","data science"
],

"ai engineer":[
"python","deep learning","machine learning","nlp","tensorflow","pytorch"
],

"data analyst":[
"sql","excel","python","pandas","data visualization","power bi","tableau"
],

"cloud computing":[
"aws","docker","kubernetes","linux","cloud","devops"
],

"devops":[
"docker","kubernetes","jenkins","aws","linux","ci/cd"
],

"mobile development":[
"java","kotlin","flutter","react native","android","ios"
],

"cybersecurity":[
"python","linux","kali","networking","ethical hacking","penetration testing"
]

}

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


def extract_domain_skills(text):

    text = text.lower()

    jd_skills = []

    for domain in domain_skills:
        if domain in text:
            jd_skills.extend(domain_skills[domain])

    return list(set(jd_skills))