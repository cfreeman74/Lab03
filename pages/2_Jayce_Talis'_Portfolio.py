import streamlit as st
import jayceinfo
import pandas as pd

##AboutMe

def about_me_section():
    st.header("⚙️About Me")
    st.image(jayceinfo.profile_picture, width = 200)
    st.write(jayceinfo.about_me)
    st.write("---")
about_me_section()

##Sidebar Links

def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link = f'<a href="{jayceinfo.my_linkedin_url}"><img src="{jayceinfo.linkedin_image_url}" alt="LinkedIn" width = "75" height = "75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Checkout my work")
    github_link = f'<a href="{jayceinfo.my_github_url}"><img src="{jayceinfo.github_image_url}" alt="Github" width = "65" height = "65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html = f'<a href="mailto:{jayceinfo.my_email_address}"><img src="{jayceinfo.email_image_url}" alt="Email" width = "75" height = "75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)
links_section()

##Education

def education_section(education_data,course_data):
    st.header("🎓Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Location:** {education_data['Location']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")
    st.write(f"**Relevant Coursework:** {education_data['Relevant Coursework']}")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"},
        hide_index=True,
                 )
    st.write("---")
education_section(jayceinfo.education_data,jayceinfo.course_data )    

##Professional Experience
def experience_section(experience_data):
    st.header("👨🏻‍🏭Professional Experience")
    for job_title,(job_description,image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image,width=250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")
experience_section(jayceinfo.experience_data)

##Projects
def project_section(projects_data):
    st.header("⚗️Projects")
    for project_name,project_description in projects_data.items():
        expander=st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")
project_section(jayceinfo.projects_data)

##Skills
def skills_section(programming_data, spoken_data):
    st.header("🧙🏻Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{jayceinfo.programming_icons.get(skill,'')}")
        st.progress(percentage)
        
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken}{jayceinfo.spoken_icons.get(spoken,'')}:{proficiency}")
    st.write("---")
skills_section(jayceinfo.programming_data,jayceinfo.spoken_data)

##Activities
def activities_section(leadership_data,activity_data):
    st.header("🏙 Activities")
    tab1,tab2 = st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("Leadership")
        for title,(details,image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image,width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
    st.write("---")
activities_section(jayceinfo.leadership_data, jayceinfo.activity_data)

