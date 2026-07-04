"""
Blueprint AI System — Demo Hub
Launcher for all 3 interactive demos

Run: streamlit run demos/hub.py
"""

import streamlit as st
import subprocess, sys

st.set_page_config(page_title="Blueprint AI System — Demo Suite", layout="centered")
st.title("Blueprint AI System")
st.subheader("Interactive Demo Suite")
st.markdown("Select a demo below to see AI capability in your industry.")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🏥 Healthcare")
    st.markdown("**AI Clinical Note Summarizer**")
    st.markdown("Turns raw consultation transcripts into structured SOAP notes in seconds.")
    if st.button("Launch Healthcare Demo", key="hc"):
        subprocess.Popen(["streamlit", "run", "demos/healthcare/app.py"])
        st.success("Launching... check your terminal or new browser tab.")

with col2:
    st.markdown("### 🏠 Real Estate")
    st.markdown("**AI Lead Scorer & Response Generator**")
    st.markdown("Scores inquiries, identifies intent, and drafts personalized responses automatically.")
    if st.button("Launch Real Estate Demo", key="re"):
        subprocess.Popen(["streamlit", "run", "demos/realestate/app.py"])
        st.success("Launching... check your terminal or new browser tab.")

with col3:
    st.markdown("### 🏗️ Construction")
    st.markdown("**AI Bid Estimator**")
    st.markdown("Generates detailed cost estimates from project specs with line-item breakdown.")
    if st.button("Launch Construction Demo", key="con"):
        subprocess.Popen(["streamlit", "run", "demos/construction/app.py"])
        st.success("Launching... check your terminal or new browser tab.")

st.divider()
st.markdown("### How to Run")
st.code("""
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set your API key in config.py
# Get free key: https://build.nvidia.com/settings/api-keys

# 3. Run individual demo
streamlit run demos/healthcare/app.py

# Or run the hub
streamlit run demos/hub.py
""")
