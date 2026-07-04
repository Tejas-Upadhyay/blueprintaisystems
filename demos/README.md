# Blueprint AI System — Demo Suite

Three interactive AI demos built for live sales calls with prospects in Healthcare, Real Estate, and Construction — all in a single tabbed app.

Uses **NVIDIA NIM (DeepSeek-V4-Flash)** for inference — free tier, no GPU required.

---

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set your NVIDIA NIM API key
export NVIDIA_API_KEY="nvapi-..."
# Or edit demos/config.py directly (not recommended — will be git-visible)

# 3. Run the hub
streamlit run demos/hub.py
```

## Demos

| Tab | Sector | What It Does |
|-----|--------|-------------|
| Healthcare | Clinical Note Summarizer | Paste a consultation transcript → get a structured SOAP note |
| Real Estate | Lead Scorer & Response Generator | Paste a lead inquiry → get a score + draft reply |
| Construction | Bid Estimator | Paste project specs → get a cost estimate breakdown |

## How to Use in a Sales Call

1. **Ask** the prospect about their pain point (documentation time, lead response, bid turnaround)
2. **Open** the relevant tab in your browser
3. **Paste** their real data (or the sample data built in)
4. **Show** the result appear in seconds
5. **Ask** "What would it look like if we built this on your actual workflow?"

No authentication, no database, no setup on the prospect's end. Just paste and go.

## Files

```
demos/
├── config.py           # API key configuration
├── requirements.txt    # Dependencies
├── hub.py              # Single tabbed demo app (run this)
└── README.md           # This file
```
