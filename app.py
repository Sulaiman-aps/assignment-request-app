import streamlit as st
import pandas as pd

st.title("📄 Assignment Request Form")

# Input fields
name = st.text_input("Name")
city = st.text_input("City")
phone = st.text_input("Phone Number")
payment_status = st.selectbox("Payment Status", ["Paid", "Unpaid", "Pending"])

# Submit button
if st.button("Submit"):
    if name and city and phone:
        # Save to DataFrame (in real app, you'd store to database or file)
        data = pd.DataFrame([{
            "Name": name,
            "City": city,
            "Phone Number": phone,
            "Payment Status": payment_status
        }])
        st.success("✅ Request submitted successfully!")
        st.write("📋 Submitted Data:")
        st.dataframe(data)
    else:
        st.warning("⚠️ Please fill in all required fields.")