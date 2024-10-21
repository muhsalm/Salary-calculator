#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import streamlit as st

file_path = "payrate.xlsx"

# Load the Excel file
df = pd.read_excel(file_path)

# Streamlit app title
st.title("Total Pay Calculator")

# Sidebar Section for Input
st.sidebar.header("Select Day, Type, Overtime, and Paid Leave")

# Available days and types
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "PH", "PH Night1", "PH Night2", "Overtime"]
types = ["Day", "Night"]

# Creating 11 combination selectors in the sidebar
combinations = []
for i in range(1, 9):  # Up to 9 combinations
    day = st.sidebar.selectbox(f"Select Day {i}", [""] + days, index=0)
    typ = st.sidebar.selectbox(f"Select Type {i}", [""] + types, index=0)
    if day and typ:
        combinations.append((day, typ))

# Overtime Hours Input
overtime_hours = st.sidebar.number_input("Overtime Hours", min_value=0.0, step=0.5, value=0.0)
overtime_rate = 54.84
overtime_pay = overtime_hours * overtime_rate

# Paid Leave Hours Input
paid_leave_hours = st.sidebar.number_input("Paid Leave Hours", min_value=0.0, step=0.5, value=0.0)
paid_leave_rate = 27.42
paid_leave_pay = paid_leave_hours * paid_leave_rate

# Input for First Aid Amount
first_aid_amount = st.sidebar.number_input("First Aid Amount (in $)", min_value=0.0, step=0.01, value=0.0)

# Calculating Total Pay from Selected Combinations
total_combination_pay = 0
breakdown = []

for day, typ in combinations:
    # Filter rows matching the selected day and type (assuming columns named 'Day' and 'Type')
    filtered = df[(df['Day'] == day) & (df['Type'] == typ)]
    pay = filtered['Pay'].sum() if not filtered.empty else 0
    total_combination_pay += pay
    breakdown.append(f"{day} - {typ}: ${pay:.2f}")

# Total Pay Calculation
total_pay = total_combination_pay + overtime_pay + paid_leave_pay + first_aid_amount

# Displaying the Pay Slip on the Main Page
st.header("Pay Slip")
st.write("### Pay Breakdown:")
for entry in breakdown:
    st.write(f"- {entry}")

st.write(f"- **Overtime Pay:** ${overtime_pay:.2f}")
st.write(f"- **Paid Leave Pay:** ${paid_leave_pay:.2f}")
st.write(f"- **Firs Aid:** ${first_aid_amount:.2f}")

st.write("### Total Pay:")
st.write(f"**${total_pay:.2f}**")
