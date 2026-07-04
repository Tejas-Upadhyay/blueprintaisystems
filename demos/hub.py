"""
Blueprint AI System — Demo Suite
Run all 3 demos inside this single app using tabs.

Run: streamlit run demos/hub.py
"""

import streamlit as st
from openai import OpenAI
from config import NVIDIA_API_KEY, NVIDIA_BASE_URL, MODEL

st.set_page_config(page_title="Blueprint AI System — Demo Suite", layout="wide")
st.title("Blueprint AI System")
st.subheader("Interactive Demo Suite")

tab1, tab2, tab3 = st.tabs(["🏥 Healthcare", "🏠 Real Estate", "🏗️ Construction"])

with tab1:
    st.markdown("### AI Clinical Note Summarizer")
    st.markdown("Paste a consultation transcript below. The AI generates a structured SOAP note.")

    transcript = st.text_area("Paste transcript", height=200,
        value="Dr: What brings you in today?\nPatient: I've had lower back pain for two weeks.\nDr: Any numbness or tingling?\nPatient: No numbness. Just pain when I bend over.\nDr: Let me take a look.", key="hc_transcript")

    patient = st.text_input("Patient name (optional)", key="hc_patient")

    if st.button("Generate SOAP Note", key="hc_btn", type="primary"):
        if not NVIDIA_API_KEY or NVIDIA_API_KEY.startswith("nvapi-..."):
            st.error("API key not configured. Set NVIDIA_API_KEY in config.py or as an environment variable.")
        else:
            client = OpenAI(base_url=NVIDIA_BASE_URL, api_key=NVIDIA_API_KEY)
            prompt = f"""Convert this consultation transcript into a structured SOAP note.

Format:
**Subjective:**
**Objective:**
**Assessment:**
**Plan:**

Transcript:
{transcript}
Patient: {patient if patient else "Not specified"}"""
            with st.spinner("Generating..."):
                try:
                    resp = client.chat.completions.create(model=MODEL, messages=[{"role": "user", "content": prompt}], temperature=0.1, max_tokens=800)
                    st.divider()
                    st.markdown(resp.choices[0].message.content)
                except Exception as e:
                    st.error(f"API error: {e}")

with tab2:
    st.markdown("### AI Lead Scorer & Response Generator")
    st.markdown("Paste a lead inquiry. The AI scores it and drafts a personalized response.")

    inquiry = st.text_area("Paste lead inquiry", height=150,
        value="Hi, I'm relocating from Chicago and looking for a 3BR home in Naples under $800k. Moving in 60 days. Can you send me listings?", key="re_inquiry")

    if st.button("Analyze Lead", key="re_btn", type="primary"):
        if not NVIDIA_API_KEY or NVIDIA_API_KEY.startswith("nvapi-..."):
            st.error("API key not configured. Set NVIDIA_API_KEY in config.py or as an environment variable.")
        else:
            client = OpenAI(base_url=NVIDIA_BASE_URL, api_key=NVIDIA_API_KEY)
            prompt = f"""Analyze this real estate lead. Return:
- lead_score: 1-100
- sentiment: hot/warm/cold
- budget_range
- timeline
- key_needs
- draft_response

Inquiry: {inquiry}"""
            with st.spinner("Analyzing..."):
                try:
                    resp = client.chat.completions.create(model=MODEL, messages=[{"role": "user", "content": prompt}], temperature=0.2, max_tokens=600)
                    st.divider()
                    st.markdown(resp.choices[0].message.content)
                except Exception as e:
                    st.error(f"API error: {e}")

with tab3:
    st.markdown("### AI Bid Estimator")
    st.markdown("Enter project specifications to generate a cost estimate.")

    spec = st.text_area("Project specs", height=150,
        value="2,500 sq ft single family home, slab foundation, 3BR, 2BA, Naples FL, mid quality, 9 month timeline", key="con_spec")

    if st.button("Generate Estimate", key="con_btn", type="primary"):
        if not NVIDIA_API_KEY or NVIDIA_API_KEY.startswith("nvapi-..."):
            st.error("API key not configured. Set NVIDIA_API_KEY in config.py or as an environment variable.")
        else:
            client = OpenAI(base_url=NVIDIA_BASE_URL, api_key=NVIDIA_API_KEY)
            prompt = f"""You are a construction cost estimator for SW Florida.

FACTS (use these, do not contradict):
- Naples is in Collier County. It is NOT in the High-Velocity Hurricane Zone (HVHZ). HVHZ only applies to Miami-Dade and Broward counties.
- Collier County is a Wind-Borne Debris Region. Impact-resistant windows/doors are required, but NOT Miami-Dade NOA-rated products.

TASK: Using your knowledge of current construction costs in Southwest Florida, estimate this project. Return ONLY the final estimate. No analysis, no reasoning.

{spec}

**Total Estimate:** $X
**Cost per Sq Ft:** $X

**Line Items:**
**Code Notes:**
**Assumptions:**

Important: This is a rough order-of-magnitude estimate for demonstration."""
            with st.spinner("Calculating..."):
                try:
                    resp = client.chat.completions.create(model=MODEL, messages=[{"role": "user", "content": prompt}], temperature=0.1, max_tokens=1000)
                    st.divider()
                    st.markdown(resp.choices[0].message.content)
                except Exception as e:
                    st.error(f"API error: {e}")

st.divider()
st.caption("Each demo uses NVIDIA NIM (DeepSeek-V4-Flash) for inference.")
