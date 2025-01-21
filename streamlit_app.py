import pandas as pd
import streamlit as st

# Load the dataset
@st.cache
def load_data(Black Screen Tool - 2024-10-23.xlsx):
    data = pd.read_excel(Black Screen Tool - 2024-10-23.xlsx)
    return data

# Function to determine action
def check_sn_status(sn, data):
    result = data[data['SN'] == sn]
    if not result.empty:
        return result.iloc[0]['Action']  # Assuming 'Action' column has "Repair" or "Replace"
    return "SN not found."

# Streamlit App
def main():
    st.title("Repair or Replace Tool")
    st.write("Enter the Serial Number (SN) below to check if it requires repair or replacement.")

    # File upload and data load
    uploaded_file = st.file_uploader("Upload your data file", type=["xlsx"])
    if uploaded_file:
        data = load_data(uploaded_file)

        # Input from user
        sn = st.text_input("Enter Serial Number (SN):")
        
        if sn:
            action = check_sn_status(sn, data)
            st.write(f"The SN `{sn}` requires: {action}")

# Run the app
if __name__ == "__main__":
    main()
