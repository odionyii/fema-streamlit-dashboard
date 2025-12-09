import os
import sys
import subprocess

# Make sure streamlit is installed
try:
    import streamlit as st
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
    import streamlit as st

# Make sure plotly is installed
try:
    import plotly.express as px
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "plotly"])
    import plotly.express as px

import pandas as pd


# Title + Description

st.title("FEMA Disaster Relief Dashboard")
st.write("This dashboard explores repair amounts and TSA eligibility using a sample of FEMA data.")

# Load Data

df = pd.read_csv("fema_small.csv")

st.subheader("Dataset Preview")
st.write(df.head())

# Histogram of Repair Amount

st.subheader("Histogram of Repair Amount")
fig_hist = px.histogram(df, x="repairAmount", nbins=40,
                        title="Distribution of Repair Amounts",
                        color_discrete_sequence=["#4C72B0"])
st.plotly_chart(fig_hist)

# Boxplot of Repair Amount by TSA Eligibility

st.subheader("Repair Amount by TSA Eligibility")
fig_box = px.box(df,
                 x="tsaEligible",
                 y="repairAmount",
                 color="tsaEligible",
                 title="Repair Amounts: TSA Eligible vs. Not Eligible",
                 labels={"tsaEligible": "TSA Eligible", "repairAmount": "Repair Amount"})
st.plotly_chart(fig_box)

# Student summary / insights area

st.subheader("Insights")
st.markdown("""
- The histogram helps reveal the central tendency and spread of repair amounts.
- The boxplot compares distributions between TSA-eligible and non-eligible households.
- These visualizations support understanding how financial need and disaster severity relate to TSA assistance.
""")
