# Blueprint AI System — Demo Suite

Three interactive AI demos built for live sales calls with prospects in Healthcare, Real Estate, and Construction.

Each demo runs in your browser via Streamlit and uses **NVIDIA NIM (DeepSeek-V4-Flash)** for inference — free tier, no GPU required.

---

## Demos

| Demo | Sector | What It Does | Run Command |
|------|--------|-------------|-------------|
| Clinical Note Summarizer | Healthcare | Paste a consultation transcript → get a structured SOAP note | `streamlit run demos/healthcare/app.py` |
| Lead Scorer & Response Generator | Real Estate | Paste a lead inquiry → get a score + draft reply | `streamlit run demos/realestate/app.py` |
| Bid Estimator | Construction | Paste project specs → get a cost estimate breakdown | `streamlit run demos/construction/app.py` |

A central hub is also available:

```
streamlit run demos/hub.py
```

---

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Add your NVIDIA NIM API key to demos/config.py
#    Get a free key at https://build.nvidia.com/settings/api-keys

# 3. Run any demo
streamlit run demos/healthcare/app.py
```

The API key is the only thing you need. Demos use sample data built-in so you can run them immediately.

---

## How to Use in a Sales Call

Each demo is designed to be shown during a discovery call. The flow:

1. **Ask** the prospect about their pain point (documentation time, lead response, bid turnaround)
2. **Open** the relevant demo in your browser
3. **Paste** their real data (or the sample data built in)
4. **Show** the result appear in seconds
5. **Ask** "What would it look like if we built this on your actual workflow?"

The demos are intentionally simple — no authentication, no database, no setup required on the prospect's end. Just paste and go.

---

## Tech Stack

| Component | Choice |
|-----------|--------|
| LLM Inference | NVIDIA NIM (deepseek-v4-flash) |
| UI | Streamlit |
| Language | Python 3.10+ |

---

## Files

```
demos/
├── config.py              # API key
├── requirements.txt       # Dependencies
├── hub.py                 # Central launcher
├── healthcare/app.py      # SOAP note generator
├── realestate/app.py      # Lead scorer
└── construction/app.py    # Bid estimator
```