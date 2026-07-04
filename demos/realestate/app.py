"""
Real Estate Demo: AI Lead Scorer & Response Generator
Blueprint AI System — NVIDIA NIM + DeepSeek-V4-Flash

Run: streamlit run demos/realestate/app.py
"""

import streamlit as st
import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from openai import OpenAI
from config import NVIDIA_API_KEY, NVIDIA_BASE_URL, MODEL

st.set_page_config(page_title="RE Lead Intelligence Engine", layout="centered")
st.title("AI Lead Scorer & Response Generator")
st.markdown("Paste an inquiry to see AI-powered lead scoring, sentiment analysis, and a personalized draft response.")

SAMPLE_INQUIRIES = {
    "Hot Lead": "Hi, I'm a relocation buyer from Chicago with a pre-approval for $1.2M. I'm flying to Naples next week and want to see 3-4 bedroom homes with a pool and Gulf access. My timeline is 60 days. Can you send me your best current listings in Pelican Bay?",
    "Warm Lead": "Hello, my wife and I are thinking about moving to Florida in the next 6-12 months. We've been looking online at homes in Estero. Could you send me some information about the area and what's available in the $500k-$700k range?",
    "Cold Lead": "Just looking around on Zillow. Not ready to buy anything right now but wanted to see what's out there. What's the cheapest house you have listed?",
}

inquiry_type = st.selectbox("Try a sample inquiry", list(SAMPLE_INQUIRIES.keys()))
inquiry = st.text_area("Or paste a custom inquiry", value=SAMPLE_INQUIRIES[inquiry_type], height=150)

def analyze_lead(inquiry_text):
    client = OpenAI(base_url=NVIDIA_BASE_URL, api_key=NVIDIA_API_KEY)
    prompt = f"""Analyze this real estate lead inquiry. Return a JSON with:
- lead_score: integer 1-100
- sentiment: one of "hot", "warm", "cold"
- budget_range: estimated budget or "unknown"
- timeline: estimated buying timeline
- key_needs: list of 3-5 key requirements
- recommended_action: one sentence on next step
- draft_response: a 3-4 sentence personalized response

Inquiry: {inquiry_text}
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2, max_tokens=800
    )
    return response.choices[0].message.content

if st.button("Analyze Lead", type="primary"):
    if not NVIDIA_API_KEY or NVIDIA_API_KEY == "nvapi-...":
        st.error("Please set your NVIDIA NIM API key in config.py")
    elif not inquiry.strip():
        st.warning("Please enter an inquiry.")
    else:
        with st.spinner("Analyzing lead..."):
            result = analyze_lead(inquiry)

        st.divider()
        st.markdown("### Lead Analysis")

        try:
            data = json.loads(result.replace("```json", "").replace("```", "").strip())
            col1, col2, col3 = st.columns(3)
            score = data.get("lead_score", 0)
            color = "green" if score > 70 else "orange" if score > 30 else "red"
            col1.metric("Lead Score", f"{score}/100")
            col2.metric("Sentiment", data.get("sentiment", "unknown").title())
            col3.metric("Timeline", data.get("timeline", "unknown"))
            st.markdown(f"**Budget Range:** {data.get('budget_range', 'unknown')}")
            st.markdown("**Key Needs:**")
            for need in data.get("key_needs", []):
                st.markdown(f"- {need}")
            st.markdown(f"**Recommended Action:** {data.get('recommended_action', '')}")
            st.divider()
            st.markdown("### Draft Response to Lead")
            st.info(data.get("draft_response", ""))
        except:
            st.markdown(result)
