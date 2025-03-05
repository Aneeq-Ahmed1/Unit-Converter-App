# import streamlit as st

# st.title("🌍Unit Converter App")
# st.markdown("### Converts Length, Weight And Time Instantly")
# st.write("Welcome! Select a category, enter a value and get the converted result in real-time")

# category = st.selectbox("Choose a categoty", ["Length", "Weight", "Time"])

# def convert_units(category, value, unit):
#     if category == "Length":
#         if unit == "Kilometers to Miles":
#             return value * 0.621371
#         elif unit == "Miles to Kilometers":
#             return value / 0.621371
        
#     elif category == "Weight":
#         if unit == "Kilograms to pounds":
#             return value * 2.20462
#         elif unit == "Pounds to kilograms":
#             return value / 2.20462
#     elif category == "Time":
#         if unit == "Seconds to minutes":
#             return value / 60
#         elif unit == "Minutes to seconds":
#             return value * 60
#         elif unit == "Minutes to hours":
#             return value / 60
#         elif unit == "Hours to minutes":
#             return value * 60
#         elif unit == "Hours to days":
#             return value / 24
#         elif unit == "Days to hours":
#             return value * 24
#     return 0
        
# if category == "Length":
#     unit = st.selectbox("📏 Select Conversation", ["Miles to Kilometers","Kilometers to Miles"])
# elif category == "Weight":
#     unit = st.selectbox("⚖️ Select Conversation", ["Kilograms to pounds", "Pounds to kilograms"])
        
# elif category == "Time":
#     unit = st.selectbox("⏱️ Select Conversation", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])

# value = st.number_input("Enter the value to convert")

# if st.button("Convert"):
#     result = convert_units(category, value, unit)
#     st.success(f"The result is {result:.2f}")
    






























import streamlit as st
import time

# App Title & Description
st.title("🌍 Unit Converter App")
st.markdown("## 📏⚖️⏱️ Convert Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result with a smooth experience.")

# Select Category
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Conversion Function
def convert_units(category, value, unit):
    conversions = {
        "Length": {
            "Kilometers to Miles": value * 0.621371,
            "Miles to Kilometers": value / 0.621371
        },
        "Weight": {
            "Kilograms to Pounds": value * 2.20462,
            "Pounds to Kilograms": value / 2.20462
        },
        "Time": {
            "Seconds to Minutes": value / 60,
            "Minutes to Seconds": value * 60,
            "Minutes to Hours": value / 60,
            "Hours to Minutes": value * 60,
            "Hours to Days": value / 24,
            "Days to Hours": value * 24
        }
    }
    return conversions.get(category, {}).get(unit, 0)

# Select Conversion Unit
unit_options = {
    "Length": ["Miles to Kilometers", "Kilometers to Miles"],
    "Weight": ["Kilograms to Pounds", "Pounds to Kilograms"],
    "Time": ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"]
}
unit = st.selectbox("Select Conversion", unit_options[category])

# Input Value
value = st.number_input("Enter the value to convert", min_value=0.0, format="%.2f")

# Convert Button with Animation
if st.button("Convert"):
    with st.spinner("Converting..."):
        time.sleep(1)
        result = convert_units(category, value, unit)
        st.success(f"The result is {result:.2f}")
        st.balloons()
