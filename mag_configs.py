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
    
    st.header("Magnetic Field Formulas and Explanations")
    st.markdown(r"""**Vacuum Permeability ($\mu_0$)** $\mu_0$ is the vacuum permeability, which characterizes the ability of free space to support a magnetic field. Its standard value is:""")

    st.markdown(
        '<div style="text-align: center;">'
        r'$\mu_0 = 1.25663706127 \times 10^{-6}\, \text{N/A}^2$'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown(r"""  
    $
    \mu_0 = 1.25663706127 \times 10^{-6}\, \text{N/A}^2.
    $

**Long Straight Wire**  
A long straight wire carrying a current $I$ produces a magnetic field that encircles the wire and decreases with distance. The magnetic field at a distance $r$ is given by:

 st.image("data/figs/B_field_wire.jpg", caption="Magnetic Field Orientation: Long Straight Wire", use_column_width=True)
    
$
B = \frac{\mu_0 I}{2 \pi r}
$

where:  
- $I$ is the current in amperes (A).  
- $r$ is the distance from the wire in meters (m).  

This formula shows that the magnetic field is inversely proportional to the distance from the wire.

**Circular Loop**  
A circular loop of wire carrying a current $I$ produces a magnetic field at its center given by:

$
B = \frac{\mu_0 I}{2R}
$

where:  
- $R$ is the radius of the loop in meters (m).

This expression is valid when measuring the field at the center of the loop.

**Solenoid**  
For a solenoid with $N$ turns, a length $L$, and carrying a current $I$, the magnetic field inside (assuming an ideal, long solenoid) is approximately uniform and given by:

$$
B = \mu_0 \left(\frac{N}{L}\right) I
$$

where:  
- $\frac{N}{L}$ represents the number of turns per unit length (turns per meter).

This formula demonstrates that the field inside the solenoid increases with both the current and the turn density.
    """, unsafe_allow_html=True)
    
    st.header("Units")
    st.markdown(r"""
Magnetic field strength is commonly measured in **Gauss (G)** in the CGS system.  
$$
1\,\text{Gauss} = 10^{-4}\,\text{Tesla (T)}
$$  
The Tesla (T) is the SI unit for magnetic field strength.
    """, unsafe_allow_html=True)
    
    st.header("Particle Properties")
    st.markdown(r"""
- **Electron:**  
  - Mass: $9.11 \times 10^{-31}\,\text{kg}$  
  - Charge: $-1.6 \times 10^{-19}\,\text{C}$
  
- **Proton:**  
  - Mass: $1.67 \times 10^{-27}\,\text{kg}$  
  - Charge: $+1.6 \times 10^{-19}\,\text{C}$
    """, unsafe_allow_html=True)
    
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
