# PHY 132 Magnetic Field Configurations Answer Checker

This repository contains a Streamlit application developed for **PHY 132 – College Physics II** at Eastern Kentucky University. The app is designed to help students check their final numerical answers for a series of questions on magnetic field configurations. It also provides background information—including detailed explanations, centered formulas, and illustrative figures—to support learning.

## Overview

The application is divided into two main pages accessible via the sidebar:

- **Answer Checker:**  
  Students can select a question, enter their answer (with a 1% tolerance), and receive immediate feedback on their correctness.

- **Background Information:**  
  This page offers detailed explanations of magnetic field formulas for:
  - A long straight wire,
  - A circular loop, and
  - A solenoid.
  
  It also includes:
  - An explanation of vacuum permeability (\\(\\mu_0\\)) and its standard value,
  - A short discussion of magnetic field units (Gauss and Tesla),
  - Particle properties (mass and charge of the electron and proton), and
  - Illustrative figures (to be placed in the `/data/figs/` folder) showing the magnetic field orientations for each configuration.

## Features

- **Interactive Answer Checker:**  
  Check your final numerical answers for a variety of magnetic field configuration questions. Only numerical inputs are required (units are handled separately).

- **Background Information with Centered Formulas:**  
  Formulas are center-justified for readability. Explanations include all key parameters and concepts such as current, distance, and turn density, along with the definition and value of \\(\\mu_0\\).

- **Sidebar Navigation:**  
  Easily switch between the Answer Checker and Background Information pages using the sidebar.

- **Figures:**  
  Placeholder images for the magnetic field orientations (for the long straight wire, circular loop, and solenoid) are displayed on the Background Information page. Place your figure files (e.g., `long_wire.png`, `circular_loop.png`, and `solenoid.png`) inside the `/data/figs/` folder.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/phy132-magnetic-field-checker.git
