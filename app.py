import streamlit as st
import pandas as pd

from database import Database
from student import Student 

st.set_page_config(
    page_title="student managment system",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student managment system")

# Sidebar

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Add Student",
        "View Student",
        "Search Student",
        "Update Student",
        "Delete Student"
    ]
)


Database.create_table()


# ADD STUDENT

if menu == "Add Student":
    st.header("➕ Add Student")

    with st.form("student_form"):

        name = st.text_input("Student Name")

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=100

        )

        course = st.text_input("Course")

        submit = st.form_submit_button(
            "Add Student"
        )

        if submit:
            if name.strip() == "" or course.strip() == "":
                st.error(
                    "All Fields Are Required"
                )
            else:
                student = Student(
                    name,
                    age,
                    course
                )

                Database.add_student(
                    student.name,
                    student.age,
                    student.course
                )

                st.success(
                    "Student Added Succesfully"
                )





