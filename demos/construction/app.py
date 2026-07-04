"""
Construction Demo: AI Bid Estimator
Blueprint AI System — NVIDIA NIM + DeepSeek-V4-Flash

Run: streamlit run demos/construction/app.py
"""

import streamlit as st
import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from openai import OpenAI
from config import NVIDIA_API_KEY, NVIDIA_BASE_URL, MODEL

st.set_page_config(page_title="AI Construction Bid Estimator", layout="centered")
st.title("AI Bid Estimator")
st.markdown("Enter project specifications to generate an AI-powered cost estimate with line-item breakdown.")

SAMPLE_SPEC = """
Project: 3,200 sq ft custom residential home
Location: Naples, FL
Foundation: Slab on grade
Floors: 2
Bedrooms: 4
Bathrooms: 3.5
Garage: 3-car attached
Roof: Concrete tile
Exterior: Stucco with impact windows
Interior: Engineered hardwood floors, quartz countertops, custom cabinetry
HVAC: 2-zone central AC
Timeline: 9 months
Quality level: Mid-high
"""

project_spec = st.text_area("Paste project specifications", value=SAMPLE_SPEC, height=250)
st.caption("Include: square footage, location, materials, quality level, number of floors/rooms")

def generate_estimate(spec):
    client = OpenAI(base_url=NVIDIA_BASE_URL, api_key=NVIDIA_API_KEY)
    prompt = f"""You are a construction cost estimator for Southwest Florida. Based on the project spec below, generate a detailed cost estimate.

Return a JSON with:
- total_estimate: total project cost
- cost_per_sqft: cost per square foot
- line_items: array of {{
    "category": str,
    "amount": float,
    "percentage": float
  }}
- notes: array of 2-3 key assumptions or caveats

Project Specifications:
{spec}

Use current 2026 pricing for Collier County, FL. Include realistic material and labor costs.
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1, max_tokens=1200
    )
    return response.choices[0].message.content

if st.button("Generate Estimate", type="primary"):
    if not NVIDIA_API_KEY or NVIDIA_API_KEY == "nvapi-...":
        st.error("Please set your NVIDIA NIM API key in config.py")
    elif not project_spec.strip():
        st.warning("Please enter project specifications.")
    else:
        with st.spinner("Calculating estimate..."):
            result = generate_estimate(project_spec)

        st.divider()
        st.markdown("### Cost Estimate")

        try:
            data = json.loads(result.replace("```json", "").replace("```", "").strip())
            col1, col2 = st.columns(2)
            col1.metric("Total Estimate", f"${data.get('total_estimate', 0):,.0f}")
            col2.metric("Cost per Sq Ft", f"${data.get('cost_per_sqft', 0):,.0f}")

            st.markdown("### Line Item Breakdown")
            for item in data.get("line_items", []):
                st.markdown(f"- **{item.get('category')}:** ${item.get('amount', 0):,.0f} ({item.get('percentage', 0):.1f}%)")

            st.markdown("### Assumptions & Notes")
            for note in data.get("notes", []):
                st.markdown(f"- {note}")
        except:
            st.markdown(result)

        st.caption("This is a demo estimate. Verify all figures with current local supplier pricing before submitting bids.")
