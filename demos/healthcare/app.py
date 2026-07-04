"""
Healthcare Demo: Clinical Note Summarizer
Blueprint AI System — NVIDIA NIM + DeepSeek-V4-Flash

Run: streamlit run demos/healthcare/app.py
"""

import streamlit as st
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from openai import OpenAI
from config import NVIDIA_API_KEY, NVIDIA_BASE_URL, MODEL

st.set_page_config(page_title="AI Clinical Note Summarizer", layout="centered")
st.title("AI Scribe — Clinical Note Generator")
st.markdown("Paste a consultation transcript below. The AI generates a structured SOAP note in seconds.")

SAMPLE_TRANSCRIPT = """
Dr. Smith: Good morning Mrs. Johnson, what brings you in today?
Patient: Hi doctor, I've been having this sharp pain in my lower back for about two weeks now. It started after I lifted some heavy boxes at home.
Dr. Smith: On a scale of 1 to 10, how would you rate the pain?
Patient: It's about a 6 or 7 most days, but sometimes it gets up to an 8 when I bend over.
Dr. Smith: Any numbness or tingling in your legs?
Patient: No, no numbness. But I do feel some stiffness in the morning that lasts about 30 minutes.
Dr. Smith: Have you tried anything for the pain?
Patient: I've been taking ibuprofen 400mg twice a day. It helps a little but not completely.
Dr. Smith: Let me do a quick exam. Can you stand up and bend forward for me?
Patient: Okay... ouch, that's painful right there.
Dr. Smith: Okay, I can see there's some muscle spasm in your lower lumbar region. Range of motion is limited by about 50%. No signs of nerve compression. I'm going to prescribe a muscle relaxant — cyclobenzaprine 5mg at bedtime. I also want you to apply heat to the area for 15 minutes twice a day. Let's follow up in two weeks if it doesn't improve.
Patient: Should I stop the ibuprofen?
Dr. Smith: No, you can continue the ibuprofen with food. But switch to 600mg three times a day for better anti-inflammatory effect. If the pain hasn't improved in two weeks, we'll order an MRI.
Patient: Okay, thank you doctor.
"""

patient_info = st.text_area("Patient Name / ID (optional)", placeholder="e.g., Mrs. Johnson / ID: 38472")
transcript = st.text_area("Paste consultation transcript", height=300, value=SAMPLE_TRANSCRIPT)

def generate_soap_note(transcript, patient):
    client = OpenAI(base_url=NVIDIA_BASE_URL, api_key=NVIDIA_API_KEY)
    prompt = f"""You are a medical scribe. Convert the following consultation transcript into a structured SOAP note.
Use this exact format:

**Subjective:** [Chief complaint, history of present illness]
**Objective:** [Vitals, physical exam findings if mentioned]
**Assessment:** [Diagnosis, clinical impressions]
**Plan:** [Medications, referrals, follow-up, imaging ordered]
**Patient Instructions:** [Specific directions given to patient]

Transcript:
{transcript}

Patient: {patient if patient else "Not specified"}
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1, max_tokens=1000
    )
    return response.choices[0].message.content

if st.button("Generate SOAP Note", type="primary"):
    if not NVIDIA_API_KEY or NVIDIA_API_KEY == "nvapi-...":
        st.error("Please set your NVIDIA NIM API key in config.py")
    elif not transcript.strip():
        st.warning("Please enter a transcript.")
    else:
        with st.spinner("Generating structured clinical note..."):
            result = generate_soap_note(transcript, patient_info)
        st.divider()
        st.markdown("### Generated SOAP Note")
        st.markdown(result)
        st.caption("Note: This is a demo. Always verify AI-generated clinical notes before use.")
