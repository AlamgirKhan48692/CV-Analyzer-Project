# CV Analyzer

An AI-powered CV Analyzer built with **Python** and **Streamlit**. The
application analyzes an uploaded CV in PDF format, extracts important
candidate information, calculates a CV score, provides improvement
recommendations, compares the CV with a job description, and generates a
downloadable PDF report.


## 🚀 Live Demo

Try the CV Analyzer online:

👉 [**CV Analyzer – Live Demo**](https://cv-analyzer-project-e9jviivzsrpg7feecenzpj.streamlit.app/)

Upload your CV, analyze your CV score, view strengths and weaknesses, generate a PDF report, and test the Job Match feature.

## 🚀 Features

-   Upload CV in PDF format
-   Extract candidate name
-   Extract email address
-   Extract phone number
-   Extract technical skills
-   Extract education details
-   Extract work experience
-   Extract projects
-   Extract certifications
-   Calculate overall CV score
-   Calculate CV percentage and grade
-   Display score breakdown
-   Identify CV strengths
-   Identify CV weaknesses
-   Provide CV improvement recommendations
-   Job Match feature
-   Extract required skills from a job description
-   Find matching skills
-   Find missing skills
-   Calculate CV--Job Match percentage
-   Generate CV analysis PDF report
-   Download the generated PDF report

## 🛠️ Technologies Used

-   Python
-   Streamlit
-   PyPDF
-   ReportLab
-   Regular Expressions
-   Python Lists
-   Loops
-   Conditional Statements
-   Functions

## 📂 Project Structure

``` text
CV-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── other project files
```

> Replace `app.py` with your actual Python filename if your main
> application uses a different filename.

## ⚙️ Installation

### 1. Clone the repository

``` bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

``` bash
cd CV-Analyzer
```

### 3. Create a virtual environment

``` bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

``` bash
venv\Scripts\activate
```

**Linux/macOS:**

``` bash
source venv/bin/activate
```

### 5. Install dependencies

``` bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Run the Streamlit application with:

``` bash
streamlit run app.py
```

Then open the local Streamlit URL shown in your terminal.

## 📄 How to Use

1.  Open the CV Analyzer.
2.  Upload a CV in PDF format.
3.  The application extracts candidate information.
4.  Review the extracted skills, education, experience, projects, and
    certifications.
5.  Review the CV score and score breakdown.
6.  Check the strengths and weaknesses.
7.  Read the improvement recommendations.
8.  Paste a job description into the **Job Match** section.
9.  Analyze the matching and missing skills.
10. Review the CV--Job Match percentage.
11. Generate the PDF report.
12. Download the CV analysis report.

## 🎯 Job Match

The Job Match feature compares the skills extracted from the candidate's
CV with the skills detected in a job description.

### Workflow

``` text
CV
 ↓
Extract CV Skills
 ↓
Job Description
 ↓
Extract Job Skills
 ↓
Compare Skills
 ↓
Matching Skills
 ↓
Missing Skills
 ↓
Match Percentage
```

The project reuses the same `extract_skills()` function for both the CV
text and the job description.

## 📊 CV Scoring

The analyzer evaluates several CV categories, including:

-   Email
-   Phone
-   Skills
-   Education
-   Experience
-   Projects
-   Certifications

The application displays the earned score, maximum score, percentage,
and grade.

## 📄 PDF Report

The application can generate a PDF report containing the CV analysis
results and provide a download button for the generated report.

## ☁️ Deployment

The application can be deployed online using **Streamlit Community
Cloud**.

General deployment workflow:

``` text
Complete Project
      ↓
Create requirements.txt
      ↓
Push Project to GitHub
      ↓
Open Streamlit Community Cloud
      ↓
Connect GitHub Repository
      ↓
Select app.py
      ↓
Deploy
      ↓
Test Live Application
```

Before deployment, test the application locally:

``` bash
streamlit run app.py
```

## 🎓 Learning Goals

This project demonstrates practical use of:

-   Python programming
-   Functions
-   Lists
-   Loops
-   Conditional statements
-   String processing
-   Regular expressions
-   PDF text extraction
-   Streamlit UI development
-   Data processing
-   Basic AI-assisted CV analysis
-   Skill matching
-   PDF report generation
-   Application deployment

## 📺 Project Tutorial Series

This project was developed step by step as a tutorial series.

### Final Lessons

-   **Lesson 23:** Job Match Feature
-   **Lesson 24:** Deploy CV Analyzer Project

The complete series covers the development of the CV Analyzer from the
initial setup through analysis, scoring, reporting, job matching, and
deployment.

## 👨‍💻 Author

**Alamgir Khan**

Software Engineer \| Python \| Machine Learning \| Data Science \| Web
Development

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on
GitHub and sharing it with other learners.

------------------------------------------------------------------------

**Built with Python and Streamlit.**
