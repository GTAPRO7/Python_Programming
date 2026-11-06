import streamlit as st
import datetime

with st.form("Student Registrtion Form"):
    
    name = st.text_input("Student Name")
    reg_num = st.text_input("Register Number")
    prgm = st.selectbox(
        "Please select the programme",
        ["BCA","BSc AI/ML","MCA","MSc AI/ML",]
    )
    sem = st.radio(
        "Please select your semester",
        ["I","II","III","IV","V","VI","VII","VIII"]
    )
    sub = st.multiselect(
        "Please select your subjects",
        ["Python","Java","C","DSA","Maths","Statistics","FSD","AI/ML","ADT"]
    )
    
    today = datetime.date.today()
    dob = st.date_input("Please select your date of birth",
                     value=datetime.date(2000, 1, 1),
                     max_value=today )
    st.write("DOB:", dob)
    
    meet_time = st.time_input("Please choose your preferred time")
    
    age = st.number_input("Please enter your age")
    
    photo = st.file_uploader("Upload your recent photo", type = "jpg")
    
    if photo is not None:
        st.write("File Uploaded!", photo.name)
        
    agree = st.checkbox("I agree to the terms and conditions")
    if agree:
        st.success("Thank You for confirming!")
        
    submit = st.form_submit_button("Submit")
        
    if submit:
        st.success("Student details submitted!")
        st.write(name, reg_num, prgm, sem, sub, dob, meet_time, age)