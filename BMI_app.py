import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    return bmi

# Streamlit app title
st.title("Body Mass Index (BMI) Calculator")

# Display the BMI Categories
st.subheader("BMI Categories")
st.write("""
- **Underweight:** BMI < 18.5
- **Normal weight:** 18.5 ≤ BMI < 24.9
- **Overweight:** 25 ≤ BMI < 29.9
- **Obesity:** BMI ≥ 30
""")

# Input fields for weight and height
weight = st.number_input("Enter your weight (in kg):", min_value=0.0, format="%.2f")
height_cm = st.number_input("Enter your height (in cm):", min_value=0.0, format="%.2f")

# Calculate BMI when the button is clicked
if st.button("Calculate BMI"):
    if weight > 0 and height_cm > 0:
        bmi = calculate_bmi(weight, height_cm)
        st.write(f"Your BMI is **{bmi:.2f}**")
        
        # Display BMI category based on the calculated BMI
        if bmi < 18.5:
            st.write("Category: **Underweight**")
        elif 18.5 <= bmi < 24.9:
            st.write("Category: **Normal weight**")
        elif 25 <= bmi < 29.9:
            st.write("Category: **Overweight**")
        else:
            st.write("Category: **Obesity**")
    else:
        st.write("Please enter valid weight and height values.")
