
import streamlit as st
import json
import numpy as np

# Load the question data
with open("magnetic_questions_answers.json", "r") as f:
    questions = json.load(f)

# Title and description
st.title("PHY 132 – Magnetic Field Answer Checker")
st.markdown("Check your final numerical answer below (within 1% tolerance). Enter only the number — no units.")

# Dropdown to select a question
question_ids = list(questions.keys())
selected_id = st.selectbox("Choose a question:", question_ids)

# Retrieve selected question
q = questions[selected_id]
st.markdown(f"**{q['text']}**")

# Input field for student answer
student_answer = st.number_input(f"Enter your answer in {q['unit']}:", format="%.6f")

# Check button
if st.button("Check Answer"):
    correct = float(q['answer'])
    tolerance = 0.01 * abs(correct)  # 1% tolerance
    
    if abs(student_answer - correct) <= tolerance:
        st.success("✅ Correct! Your answer is within 1% of the expected value.")
    else:
    st.error(f"❌ Not quite. Try again.\nExpected value is between {correct - tolerance:.6g} and {correct + tolerance:.6g}.")
Expected value is between {correct - tolerance:.6f} and {correct + tolerance:.6f}.")
