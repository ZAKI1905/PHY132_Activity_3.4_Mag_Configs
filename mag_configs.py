import streamlit as st
import json
import numpy as np

# Load the question data
with open("data/qs.json", "r") as f:
    questions = json.load(f)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Answer Checker", "Background Information"])

if page == "Background Information":
    st.title("Background Information")
    
    st.header("Magnetic Field Formulas")
    st.markdown(r"""
- **Long Straight Wire:** 
  \[
  B = \frac{\mu_0 I}{2\pi r}
  \]
- **Circular Loop (at center):**
  \[
  B = \frac{\mu_0 I}{2R}
  \]
- **Solenoid (inside):**
  \[
  B = \mu_0 \left(\frac{N}{L}\right) I
  \]
    """)
    
    st.header("Units")
    st.markdown(r"""
- The magnetic field is measured in **Gauss (G)** in CGS units.
- \(1\,\text{Gauss} = 10^{-4}\,\text{Tesla (T)}\).
    """)
    
    st.header("Particle Properties")
    st.markdown(r"""
- **Electron:**  
  Mass = \(9.11 \times 10^{-31}\,\text{kg}\)  
  Charge = \(-1.6 \times 10^{-19}\,\text{C}\)
  
- **Proton:**  
  Mass = \(1.67 \times 10^{-27}\,\text{kg}\)  
  Charge = \(+1.6 \times 10^{-19}\,\text{C}\)
    """)
    
else:
    st.title("PHY 132 –  Activity 3.4 - Magnetic Field Configurations")
    st.write("This tool is intended for checking final numerical answers to some parts of the questions.")
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
            st.error("❌ Not quite. Try again.")
    
# Footer with contact info and right-aligned EKU logo
footer = '''
---
<div style="display: flex; justify-content: space-between; align-items: center;">
    <div>
        This tool was developed for <b>PHY 132 - College Physics II</b> at Eastern Kentucky University.<br>
        For questions, contact: <b>Professor Zakeri</b> (m.zakeri@eku.edu)
    </div>
    <div>
        <img src="https://raw.githubusercontent.com/ZAKI1905/phy132-kirchhoff-checker/main/img/PrimaryLogo_Maroon.png" width="150">
    </div>
</div>
'''
st.markdown(footer, unsafe_allow_html=True)
