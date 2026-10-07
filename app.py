import streamlit as st
from pypdf import PdfReader
import re

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from io import BytesIO




# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CV Analyzer",
    page_icon="📄",
    layout="wide"
)


# ============================================================
# EXTRACT NAME
# ============================================================

def extract_name(text):

    lines = text.strip().split("\n")

    for line in lines:

        line = line.strip()

        if line:
            return line

    return "Not found"


# ============================================================
# EXTRACT EMAIL
# ============================================================

def extract_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not found"


# ============================================================
# EXTRACT PHONE NUMBER
# ============================================================

def extract_phone_number(text):

    pattern = r"(?:\+92|0092|0)?[\s-]?3\d{2}[\s-]?\d{3}[\s-]?\d{4}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not found"


# ============================================================
# EXTRACT CANDIDATE SKILLS
# ============================================================

def extract_skills(text):

    skills = [
        "python",
        "java",
        "javascript",
        "html",
        "css",
        "react",
        "node.js",
        "php",
        "mysql",
        "sql",
        "pandas",
        "numpy",
        "matplotlib",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "machine learning",
        "deep learning",
        "data science",
        "flask",
        "django",
        "streamlit",
        "git",
        "github"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills:

        if skill in text:
            found_skills.append(skill)

    return found_skills



# ============================================================
# EXTRACT CANDIDATE EDUCATION
# ============================================================

def extract_education(text):

    education_keywords = [
        "bachelor",
        "master",
        "phd",
        "b.sc",
        "bsc",
        "bs",
        "b.s",
        "m.sc",
        "msc",
        "ms",
        "m.s",
        "mba",
        "bba",
        "computer science",
        "software engineering",
        "information technology"
    ]

    education = []

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if line:

            for keyword in education_keywords:

                if keyword.lower() in line.lower():

                    education.append(line)

                    break

    return education


# ============================================================
# EXTRACT CANDIDATE EXPERIENCE
# ============================================================

def extract_experience(text):

    experience_keywords = [
        "experience",
        "work experience",
        "professional experience",
        "employment",
        "worked as",
        "developer",
        "engineer",
        "manager",
        "intern",
        "internship",
        "software engineer",
        "web developer",
        "data scientist",
        "machine learning engineer"
    ]

    experience = []

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if line:

            for keyword in experience_keywords:

                if keyword.lower() in line.lower():

                    experience.append(line)

                    break

    return experience


# ============================================================
# EXTRACT CANDIDATE PROJECTS
# ============================================================

def extract_projects(text):

    project_keywords = [
        "project",
        "github",
        "live demo",
        "technologies",
        "developed",
        "built",
        "created"
    ]

    projects = []

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if line:

            for keyword in project_keywords:

                if keyword.lower() in line.lower():

                    projects.append(line)

                    break

    return projects


# ============================================================
# EXTRACT CERTIFICATIONS
# ============================================================

def extract_certifications(text):

    certification_keywords = [
        "certificate",
        "certification",
        "certified",
        "course",
        "training",
        "workshop",
        "diploma",
        "udemy",
        "coursera",
        "kaggle",
        "freecodecamp",
        "hackerrank"
    ]

    certifications = []

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if line:

            for keyword in certification_keywords:

                if keyword.lower() in line.lower():

                    certifications.append(line)

                    break

    return certifications


# ============================================================
# CALCULATE CV SCORE
# ============================================================

def calculate_cv_score(
    email,
    phone,
    skills,
    education,
    experience,
    projects,
    certifications
):

    email_score = 0

    if email != "Not found":
        email_score += 5
    else:
        email_score += 0



    phone_score = 0

    if phone != "Not found":
        phone_score += 5
    else:
        phone_score += 0


    skill_score = 0

    if len(skills) >= 5:
        skill_score += 20
    elif len(skills) >= 3:
        skill_score += 15
    elif len(skills) >= 1:
        skill_score += 10
    else:
        skill_score += 0


    education_score = 0

    if len(education) >= 2:
        education_score += 15
    elif len(education) >= 1:
        education_score += 10
    else:
        education_score += 0



    experience_score = 0

    if len(experience) >= 2:
        experience_score += 20
    elif len(experience) >= 1:
        experience_score += 15
    else:
        experience_score += 0


    projects_score = 0

    if len(projects) >= 5:
        projects_score += 20
    elif len(projects) >= 3:
        projects_score += 15
    elif len(projects) >= 1:
        projects_score += 10
    else:
        projects_score += 0


    certification_score = 0

    if len(certifications) >= 2:
        certification_score += 15
    elif len(certifications) >= 1:
        certification_score += 10
    else:
        certification_score += 0

    Total_score = (
        email_score 
        + phone_score
        + skill_score 
        + education_score
        + experience_score
        + projects_score
        + certification_score
    )

    return (
        Total_score,
        email_score,
        phone_score,
        skill_score,
        education_score,
        experience_score,
        projects_score,
        certification_score 
    )



# ============================================================
# GENERATE PDF REPORT
# ============================================================


def generate_pdf_report(
    user_name,
    user_email,
    user_phone,
    Total_score,
    score_percentage,
    cv_grade,
    email_score,
    phone_score,
    skills_score,
    education_score,
    experience_score,
    project_score,
    certification_score,
    strengths,
    weaknesses,
    recommendations,
    user_skills,
    user_education,
    user_experience,
    user_projects,
    user_certifications
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading_style = styles["Heading2"]
    normal_style = styles["BodyText"]

    story = []

    # Title

    story.append(
        Paragraph("CV ANALYSIS REPORT", title_style)
    )

    story.append(Spacer(1 , 20))

    # Condidate Information

    story.append(
        Paragraph("Condidate Information", heading_style)
    )

    condidate_data = [
        ["Name", user_name],
        ["Email", user_email],
        ["Phone", user_phone]
    ]

    table = Table(condidate_data , colWidths=[120 , 350])

    table.setStyle(
        TableStyle([
            ("GRID", (0,0), (-1,-1) , 0.5, colors.grey),
            ("BACKGROUND", (0,0), (0,-1) , colors.lightgrey),
            ("VALIGN", (0,0) , (-1,-1), "TOP"),
            ("PADDING", (0,0), (-1,-1), 6)
        ])
    )

    story.append(table)
    story.append(Spacer(1, 20))

    # CV Score

    story.append(
        Paragraph("CV Score", heading_style)
    )

    score_data = [
        ["Total Score", f"{Total_score} / 100"],
        ["CV Percentage", f"{score_percentage}%"],
        ["CV Grade", cv_grade]
    ]

    table = Table(score_data , colWidths=[180 , 290])
    
    table.setStyle(
        TableStyle([
            ("GRID", (0,0), (-1,-1) , 0.5, colors.grey),
            ("BACKGROUND", (0,0), (0,-1) , colors.lightgrey),
            ("PADDING", (0,0), (-1,-1), 6)
        ])
    )

    story.append(table)
    story.append(Spacer(1, 20))



    # Score Breakdown


    story.append(
        Paragraph("Score Breakdown" , heading_style)
    )

    breakdown_data = [
        ["Category" , "Earned" , "Maximum"],
        ["Email" , email_score , 5],
        ["Phone" , phone_score , 5],
        ["Skills" , skills_score , 20],
        ["Education" , education_score , 15],
        ["Experience" , experience_score , 20],
        ["Projects" , project_score , 20],
        ["Certification" , certification_score , 15]
    ]

    table = Table(breakdown_data , colWidths=[250 , 100 , 100])

    table.setStyle(
        TableStyle([
            ("GRID", (0,0), (-1,-1) , 0.5, colors.grey),
            ("BACKGROUND", (0,0), (0,-1) , colors.lightgrey),
            ("ALIGN" , (1,1) , (-1,-1) , "CENTER"),
            ("VALIGN" , (0,0) , (-1,-1) , "MIDDLE"),
            ("PADDING", (0,0), (-1,-1), 6)
        ])
    )
    
    story.append(table)
    story.append(Spacer(1, 20))



    # CV Strengths

    story.append(
        Paragraph("CV Strengths" , heading_style)
    )

    if strengths:
        for strength in strengths:
            story.append(
                Paragraph(
                    f"\u2022 {strength}", normal_style
                )
            )

            story.append(Spacer(1 , 5))
    else:
        story.append(
            Paragraph(
                "No major strengths were detected.", normal_style
            )
        )
        
    story.append(Spacer(1 , 15))


    # CV Weaknesses


    story.append(
            Paragraph("CV Weaknesses" , heading_style)
        )
    
    if weaknesses:
        for weakness in weaknesses:
            story.append(
                Paragraph(
                    f"\u2022 {weakness}", normal_style
                )
            )
    
        story.append(Spacer(1 , 5))
    else:
        story.append(
            Paragraph(
                "No major weaknesses were detected.", normal_style
            )
        )
            
    story.append(Spacer(1 , 15))


    # Recommendations

    story.append(
                Paragraph("CV Rcommendations" , heading_style)
            )
            
    if recommendations:
        for recommendation in recommendations:
            story.append(
                Paragraph(
                    f"\u2022 {recommendation}", normal_style
                )
            )
            
            story.append(Spacer(1 , 5))
    else:
        story.append(
            Paragraph(
                "No Additional Recommendations", normal_style
                )
            )
                    
    story.append(Spacer(1 , 20))


    # Condidate Skills


    story.append(
                Paragraph("Condidate Skills" , heading_style)
            )
                
    if user_skills:
        for skill in user_skills:
            story.append(
                Paragraph(
                    f"\u2022 {skill.title()}", normal_style
                )
            )
            
                
            story.append(Spacer(1 , 5))
    else:
        story.append(
            Paragraph(
                "Skills Not Found.", normal_style
                )
            )
                        
    story.append(Spacer(1 , 15))


    # Education 


    story.append(
                Paragraph("Condidate Education" , heading_style)
            )
                    
    if user_education:
        for education in user_education:
            story.append(
                Paragraph(
                    f"\u2022 {education}", normal_style
                )
            )
                
                    
            story.append(Spacer(1 , 5))
    else:
        story.append(
            Paragraph(
                "Condidate education Not Found.", normal_style
                )
            )
                            
    story.append(Spacer(1 , 15))


    # Experience

    story.append(
                Paragraph("Work Experience" , heading_style)
            )
                        
    if user_experience:
        for experience in user_experience:
            story.append(
                Paragraph(
                    f"\u2022 {experience}", normal_style
                )
            )
                    
                        
            story.append(Spacer(1 , 5))
    else:
        story.append(
            Paragraph(
                "Condidate work experience Not Found.", normal_style
                )
            )
                                
    story.append(Spacer(1 , 15))


    # Projects

    story.append(
                Paragraph("Condidate Projects" , heading_style)
                )
                            
    if user_projects:
        for projects in user_projects:
            story.append(
                Paragraph(
                    f"\u2022 {projects}", normal_style
                )
            )
                        
                            
            story.append(Spacer(1 , 5))
    else:
        story.append(
            Paragraph(
                "Condidate Projects Not Found.", normal_style
                )
            )
                                    
    story.append(Spacer(1 , 15))


    # Certifications

    story.append(
                Paragraph("Certifications and Course" , heading_style)
            )
                                
    if user_certifications:
        for certification in user_certifications:
            story.append(
                Paragraph(
                    f"\u2022 {certification}", normal_style
                )
            )
                            
                                
            story.append(Spacer(1 , 5))
    else:
        story.append(
            Paragraph(
                "Certification and course Not Found.", normal_style
                )
            )
                                        
    story.append(Spacer(1 , 15))




    doc.build(story)

    buffer.seek(0)

    return buffer



# ============================================================
# APPLICATION UI
# ============================================================

st.title("📄 CV Analyzer")

st.write(
    "Upload a CV in PDF format and extract important information "
    "such as name, email, phone, skills, education, experience, "
    "projects, and certifications."
)


# ============================================================
# UPLOAD CV
# ============================================================

uploaded_file = st.file_uploader(
    "Upload your CV (PDF)",
    type=["pdf"]
)


# ============================================================
# PROCESS CV
# ============================================================

if uploaded_file is not None:

    st.success("CV uploaded successfully! ✅")


    # ========================================================
    # READ PDF
    # ========================================================

    reader = PdfReader(uploaded_file)


    # ========================================================
    # STORE EXTRACTED CV TEXT
    # ========================================================

    cv_text = ""


    # ========================================================
    # EXTRACT TEXT FROM EVERY PAGE
    # ========================================================

    for page in reader.pages:

        text = page.extract_text()

        if text:

            cv_text += text + "\n"


    # ========================================================
    # EXTRACT CANDIDATE INFORMATION
    # ========================================================

    user_name = extract_name(cv_text)

    user_email = extract_email(cv_text)

    user_phone = extract_phone_number(cv_text)

    user_skills = extract_skills(cv_text)

    user_education = extract_education(cv_text)

    user_experience = extract_experience(cv_text)

    user_projects = extract_projects(cv_text)

    user_certifications = extract_certifications(cv_text)

    (
        Total_score,
        email_score,
        phone_score,
        skills_score,
        education_score,
        experience_score,
        project_score,
        certification_score
        ) = calculate_cv_score(
        user_email,
        user_phone,
        user_skills,
        user_education,
        user_experience,
        user_projects,
        user_certifications
    )


    # ========================================================
    # CONDIDATE CV SCORE
    # ========================================================

    st.header("CONDIDATE CV SCORE")

    

    # ========================================================
    # CV SCORE PERCENTAGE
    # ========================================================

    score_percentage = Total_score

    

    # ========================================================
    # CV SCORE GRADE
    # ========================================================

    if score_percentage >= 90:
        cv_grade = " A+ "
    elif score_percentage >= 80:
        cv_grade = " A "
    elif score_percentage >= 70:
        cv_grade = " B "
    elif score_percentage >= 60:
        cv_grade = " C "
    elif score_percentage >= 50:
        cv_grade = " D "
    else:
        cv_grade = " F "

    

    score_col1 , score_col2, score_col3 = st.columns(3)

    with score_col1:
        st.metric(
            "Overall CV Score",
            f"{Total_score}/100"
        )


    with score_col2:

        st.metric(
            "CV Score Percentage:",
            f"{score_percentage}%"
        )


    with score_col3:
        st.metric(
            "CV Grade",
            cv_grade
        )


    

    st.progress(Total_score / 100)

    # ========================================================
    # CV SCORE BREAKDOWN
    # ========================================================

    st.subheader("SCORE BREAKDOWN")

    st.write(f"📧 Email: {email_score}/5 points")
    st.progress(email_score / 5)

    st.write(f"📱 Phone: {phone_score}/5 points")
    st.progress(phone_score / 5)

    st.write(f"🛠️ Skills: {skills_score}/20 points")
    st.progress(skills_score / 20)

    st.write(f"🎓 Education {education_score}/15 points")
    st.progress(education_score / 15)

    st.write(f"💼 Experience: {experience_score}/20 points")
    st.progress(experience_score / 20)

    st.write(f"🚀 Projects {project_score}/20 points")
    st.progress(project_score / 20)

    st.write(f"🏆 Certifications: {certification_score}/15 points")
    st.progress(certification_score / 15)


    # ============================================================
    # CV IMPROVEMENT RECOMMENDATIONS
    # ============================================================

    st.subheader("CV Imporvement Recommendation")

    recommendations = []

    # Email

    if user_email == "Not found":
        recommendations.append(
            "Add a Professional email in Your CV"
        )


    # Phone
    if user_phone == "Not found":
            recommendations.append(
                "Add a Phone Number in Your CV"
            )


    # Skills

    if len(user_skills) < 3:
        recommendations.append(
            "Add more relevant technical skills"
        )
    elif len(user_skills) < 5:
        recommendations.append(
            "Consider Adding more relevant technical skills"
        )


    # Education

    if len(user_education) == 0:
        recommendations.append(
            "Add education details"
        )


    # Experience

    if len(user_experience) == 0:
        recommendations.append(
            "Add work experience, internships, or relevant practical experience."
        )
    elif len(user_experience) < 2:
        recommendations.append(
            "Add more detailed work experience and responsibilities"
        )


    # Projects

    if len(user_projects) < 3:

        recommendations.append(
                "Add more projects and include technologies used."
            )

    # Certifications

    if len(user_certifications) == 0:

        recommendations.append(
            "Add relevant certifications, courses, or training."
        )


    if recommendations:

        for recommendation in recommendations:

            st.write(recommendation)

    else:

        st.success(
            "Your CV contains the main sections required by this analyzer."
        )


    

    # ========================================================
    # JOB MATCH
    # ========================================================


    st.header("🎯 Job Match")

    st.write(
        "Compare your CV with a job description "
        "and find matching and missing skills."
    )

    job_description = st.text_area(
        "Past Job Discriptions",
        height=250,
        placeholder="Past Job Discription here....."
    )

    

    if st.button("🔍 Analyze Job Match"):
        if job_description.strip():

            # Extract Skills from Job discriptions

            job_skills = extract_skills(
                job_description
            )

            # Condidate CV Skills

            condidate_skills = [

                skill.lower()

                for skill in user_skills
            ]

            # Find Matching Skills

            matching_skills = []

            for skill in job_skills:

                if skill in condidate_skills:

                    matching_skills.append(skill)

            # Find Missing Skills

            missing_skills = []

            for skill in job_skills:

                if skill not in condidate_skills:

                    missing_skills.append(skill)

            # Calculat Match Percentage

            if job_skills:

                match_percentage = (

                    # It's Formula

                    len(matching_skills) / len(job_skills) * 100
                )
            else:
                match_percentage = 0


            # ================================================
            # MATCH RESULT
            # ================================================

            st.subheader("📊 Job Match Result")

            st.metric(
                "CV-Job Match",
                f"{match_percentage:.2f}%"
            )

            st.progress(
                match_percentage / 100
            )

            # ================================================
            # MATCHING SKILLS
            # ================================================

            st.subheader("✅ Matching Skills")

            if matching_skills:

                columns = st.columns(3)

                for index, skill in enumerate(matching_skills):

                    with columns[index % 3]:

                        st.success(
                            skill.title()
                        )
            else:
                st.warning(
                    "No Matching Found."
                )

            # ================================================
            # MISSING SKILLS
            # ================================================

            st.subheader("❌ Missing Skills")

            if missing_skills:

                columns = st.columns(3)

                for index, skill in enumerate(missing_skills):
                    with columns[index % 3]:
                        st.error(
                            skill.title()
                        )
            else:

                st.success(
                    "🎉 No Missing Skills detected"
                )

            # ================================================
            # REQUIRED JOB SKILLS
            # ================================================

            st.subheader("📋 Required Job Skills")

            if job_skills:
                st.write(
                    ", ".join(
                        skill.title()
                        for skill in job_skills
                    )
                )
            else:
                st.info(
                    "No supported skills were detected "
                    "in the job description."
                )
        else:
            st.warning(
                "Please Past Job Discription First"
            )




    # ========================================================
    # CV STRENGTHS
    # ========================================================

    st.subheader("CV STRENGTHS ")

    strengths = []

    # Email

    if email_score == 5:
        strengths.append(
            "📧 Email address is available."
        )

    # Phone

    if phone_score == 5:
        strengths.append(
            "📱 Phone number is available."
        )

    # Skills

    if skills_score == 20:
        strengths.append(
            "🛠️ Strong technical skills section."
        )
    elif skills_score == 15:
        strengths.append(
            "🛠️ Good number of technical skills detected."
        )

    # Educations

    if education_score == 15:
        strengths.append(
            "🎓 Strong education information."
        )
    elif education_score == 10:
        strengths.append(
            "🎓 Education information is available."
        )

    # Experience

    if experience_score == 20:
        strengths.append(
            "💼 Strong work experience information."
        )
    elif experience_score == 15:
        strengths.append(
            "💼 Work experience information is available."
        )

    # Projects

    if project_score == 20:
        strengths.append(
            "🚀 Strong project information."
        )
    elif project_score == 15:
        strengths.append(
            "🚀 Good number of projects detected."
        )

    # Certifications

    if certification_score == 15:
        strengths.append(
            "🏆 Multiple certifications or courses detected."
        )
    elif certification_score == 10:
        strengths.append(
            "🏆 Certification or course information is available."
        )

    # =========================================================
    # DISPLAY STRENGTHS
    # =========================================================

    if strengths:
        for strength in strengths:
            st.success(strength)
    else:
        st.info(
            "No major strengths were detected by the current scoring system."
        )

    # ========================================================
    # CV WEAKNESSES
    # ========================================================

    st.subheader("⚠️ CV Weaknesses")

    weaknesses = []

    # Email

    if email_score == 0:
        weaknesses.append(
            "📧 Email address is missing."
        )

    # Phone

    if phone_score == 0:
        weaknesses.append(
            "📱 Phone number is missing."
        )

    # Skills

    if skills_score < 20:
        weaknesses.append(
            f"🛠️ Skills section needs improvement"
            f" ({skills_score} / 20 Points)."
        )

    # Education

    if education_score < 15:
        weaknesses.append(
            f"🎓 Education section needs improvement"
            f" ({education_score} / 15 Points)."
        )

    # Experience

    if experience_score < 20:
        weaknesses.append(
            f"💼 Experience section needs improvement"
            f" ({experience_score} / 20 Points)."
        )

    # Projects

    if project_score < 20:
        weaknesses.append(
            f"🚀 Projects section needs improvement"
            f" ({project_score} / 20 Points)."
        )

    # Certification

    if certification_score < 15:
        weaknesses.append(
            f"🏆 Certifications section needs improvement"
            f" ({certification_score} / 15 Points)."
        )

    # Display Weaknesses

    if weaknesses:
        for weakness in weaknesses:
            st.warning(weakness)

    else:
        st.success("🎉 No major weaknesses were detected.")


    # ========================================================
    # CV SCORE CHART
    # ========================================================

    st.subheader("📊 CV Score Chart")

    chart_data = {
        "Category": [
            "Email",
            "Phone",
            "Skills",
            "Education",
            "Experience",
            "Projects",
            "Certification"
        ],
        "Earned Score":[
            email_score,
            phone_score,
            skills_score,
            education_score,
            experience_score,
            project_score,
            certification_score
        ],
        "Maximum Score":[
            5,
            5,
            20,
            15,
            20,
            20,
            15
        ]
    }


    # ========================================================
    # Display CV SCORE CHART
    # ========================================================

    st.bar_chart(
        chart_data,
        x="Category",
        y=["Earned Score","Maximum Score"],
        stack=False,
        sort=False
    )


    # ========================================================
    # CV SUMMARY DASHBOARD
    # ========================================================

    st.header("📊 CV Summary")


    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:

        st.metric(
            "🛠️ Skills",
            len(user_skills)
        )


    with col2:

        st.metric(
            "🎓 Education",
            len(user_education)
        )


    with col3:

        st.metric(
            "💼 Experience",
            len(user_experience)
        )


    with col4:

        st.metric(
            "🧑‍💻 Projects",
            len(user_projects)
        )


    with col5:

        st.metric(
            "🏆 Certifications",
            len(user_certifications)
        )


    # ========================================================
    # PERSONAL INFORMATION
    # ========================================================

    st.header("👤 Candidate Information")


    col1, col2, col3 = st.columns(3)


    with col1:

        st.subheader("Name")

        st.write(user_name)


    with col2:

        st.subheader("Email")

        st.write(user_email)


    with col3:

        st.subheader("Phone")

        st.write(user_phone)


    # ========================================================
    # SKILLS
    # ========================================================

    

    st.header("🛠️ Candidate Skills")

    if user_skills:

        columns = st.columns(3)

        for index, skill in enumerate(user_skills):

            with columns[index % 3]:

                st.write("✅", skill.title())

    else:

        st.write("Skills not found")


    # ========================================================
    # EDUCATION
    # ========================================================

    st.header("🎓 Candidate Education")


    if user_education:

        for education in user_education:

            st.write("✅", education)

    else:

        st.write("Education information not found")


    # ========================================================
    # EXPERIENCE
    # ========================================================

    st.header("💼 Work Experience")


    if user_experience:

        for experience in user_experience:

            st.write("✅", experience)

    else:

        st.write("Work experience not found")


    # ========================================================
    # PROJECTS
    # ========================================================

    st.header("🧑‍💻 Candidate Projects")


    if user_projects:

        for project in user_projects:

            st.write("✅", project)

    else:

        st.write("Projects not found")


    # ========================================================
    # CERTIFICATIONS
    # ========================================================

    st.header("🏆 Certifications & Courses")


    if user_certifications:

        for certification in user_certifications:

            st.write("✅", certification)

    else:

        st.write("Certifications not found")



    pdf_file = generate_pdf_report(
        user_name,
        user_email,
        user_phone,
        Total_score,
        score_percentage,
        cv_grade,
        email_score,
        phone_score,
        skills_score,
        education_score,
        experience_score,
        project_score,
        certification_score,
        strengths,
        weaknesses,
        recommendations,
        user_skills,
        user_education,
        user_experience,
        user_projects,
        user_certifications
    )

    st.download_button(
        label="📥 Download CV Report",
        data=pdf_file,
        file_name="CV_Analysis_Report.pdf",
        mime="application/pdf"
    )