import streamlit as st
import datetime

st.title("Student Information System")
st.header("Student Details")
st.subheader("Personal Information")
st.text("Department of Computer Science")
st.write("Programme: MCA")
st.caption("Academic Year: 2026-2027")
st.code("print('Hello Students')", language="python")
st.latex(r"E = mc^2")

st.success("Registration completed successfully!")
st.info("Your examination is scheduled for today!")
st.warning("Last day of registrations")
st.error("Registartion not successfull")
st.exception(NameError("name is not defined!"))

st.markdown("# Python Programming")
st.markdown("## Learning Objectives")
st.markdown("**Welcome to the class!**")
st.markdown("*Learn python thorugh practical examples.*")
st.markdown("""
### Topics Covered
- Python Fundamentals
- NumPy
- Pandas
= Data Visualization
- Streamlit
""")
st.markdown("Visit Streamlit Webpage : https://streamlit.io !")

name = st.text_input("Please enter your name")
if name:
    st.write("Welcome", name)
    
feedback = st.text_area("Please enter your feedback")
if feedback:
    st.write("Your feedback:", feedback)
    
age = st.number_input(
    "Please ente your age",
    min_value=18,
    max_value=100,
    value=25
)
st.write("Your age is:", age)

marks = st.slider(
    "Please select your marks",
    min_value=0,
    max_value=100,
    value=50
)
st.write("Selected Marks:", marks)

course = st.selectbox(
    "Please select your programme",
    ["BCA", "BSc Computer Science", "MCA", "MSc AI & ML"]
)
st.write("Selected Programme:", course)

subjects = st.multiselect(
    "Please select your subjects",
    ["Python", "Java", "Machine Learning", "Data Analytics"]
)
st.write("Selected Subjects:", subjects)

gender = st.radio(
    "Please select your gender",
    ["Male", "Female", "Prefer not to say"]
)
st.write("Selected:", gender)

agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.success("Thank You for confirming!")
    
if st.button("Click Me"):
    st.success("Button Clicked Successfully!")

today = datetime.date.today()

date = st.date_input("Please select your date of birth",
                     value=datetime.date(2000, 1, 1),
                     max_value=today )
st.write("DOB:", date)

file  = st.file_uploader("Upload a CSV File", type = "csv")

if file is not None:
    st.write("File Uploaded!", file.name)

col1, col2, col3 = st.columns(3)
col1.metric("BTC Price", 7193887,-1578)
col1.metric("SOL Price", 8528,+67.33)

st.subheader("Pandas")

import pandas as pd

data = {
    "Student": ["Arun", "Bala", "Hari", "Gok"],
    "Python": [22, 30, 45, 50],
    "Statistics": [29, 31, 35, 39],
    "ML": [30, 25, 50, 45],
}

df = pd.DataFrame(data)

st.dataframe(df)

st.table(df)

st.line_chart(df.set_index("Student")[["Python", "Statistics", "ML"]])

st.bar_chart(df.set_index("Student")[["Python","Statistics", "ML"]])

st.subheader("Matplotlib")

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot(df["Student"], df["Python"])
ax.set_title("Python Marks of Students")
ax.set_xlabel("Students")
ax.set_ylabel("Marks")
st.pyplot(fig)

st.subheader("Media")

st.image(
    "images.jpg",
    caption="Sample Image",
    use_container_width=True
)

st.audio("sample-3s.mp3")

st.video("sample-5s-720p.mp4")

student={
    "Name": "Arun",
    "Programme": "MCA",
    "Marks":85,
    "Grade":"A"
}
st.json(student)

st.subheader("Forms")

with st.form("Student Form"):
     
    name = st.text_input("Student Name")
    rollno = st.text_input("Register Number")

    marks = st.number_input(
        "Please enter your marks",
        min_value=0,
        max_value=100
    )
    
    submit = st.form_submit_button("Submit")
    
    if submit:
        st.success("Studenmt details submitted!")
        st.write(name, rollno, marks)
        st.snow()
        st.balloons()
        
st.subheader("Columns, tabs and layouts")

col1, col2 = st.columns(2)

with col1:
    st.header("Student Details")
    st.write("Name: Arun")
    st.write("Programme: MCA")

with col2:
    st.header("Academic Details")
    st.write("Python: 95")
    st.write("Statistics: 85")
    
tab1, tab2, tab3 =st.tabs([
    "Student Details",
    "Marks",
    "Results"
])
    
with tab1:
    st.write("Stduent Name:  Arun")

with tab2:
    st.write("Python:  95")
    st.write("Statistics: 85")
    
with tab3:
    st.success("Result:  PASS")
    
st.sidebar.title("Settings")

st.sidebar.header("Filter Options")

course = st.sidebar.selectbox(
    "Please select the course",
    ["MCA", "MSc AI/ML", "MDS"]
)

year = st.sidebar.selectbox(
    "Please select the academic year",
    ["First Year", "Second Year"]
)

semester = st.sidebar.selectbox(
    "Please select the semester",
    ["First", "Second", "Third", "Fourth", "Fifth", "Sixth"]
)

st.subheader("Filtered data from sidebar")

filter = st.sidebar.button("Filter")
    
if filter:
    st.sidebar.success("Data filtered Successfully!")
    st.write("Selected Course:", course)
    st.write("Selected Year:", year)
    st.write("Selected Semester:", semester)

