---
title: Business Setup Playbook
date: 2026-07-03
status: active
tags: [playbook, setup, legal, sales]
---

# Blueprint AI System — Setup Playbook
## From Zero to First Paid Client

> [!tip] Current Status
> - **Website:** `blueprintaisystems.vercel.app` (free — get the domain later)
> - **Email:** Use this during demos: `tejas@blueprintaisystems.vercel.app`
> - **Domain:** Defer buying `blueprintaisystems.com` until first retainer hits

---

## Step 1: Legal & Admin Foundation (Week 1)

### 1.1 Register Your LLC
- **Go to:** https://sunbiz.org
- **Cost:** ~$125 filing fee
- **Name:** Blueprint AI System LLC (or your chosen name)
- **What you need:** EIN from IRS (free, takes 10 minutes at https://irs.gov/ein)
- **Tip:** Fund this from your first audit payment if cash is tight — operate as a sole proprietor until then

### 1.2 Open Business Bank Account
> [!tip] Recommended Banks in SW Florida
> - **FineMark National Bank & Trust** (Fort Myers/Naples) — small business friendly
> - **Bank of America** — free business checking with low minimum
> - **Community Banks** (CenTrust, First Florida) — local relationship matters

### 1.3 Get Business Insurance
> [!warning] Required before signing enterprise clients
> - **Professional Liability (Errors & Omissions):** ~$500–$1,000/yr
> - **Cyber Liability:** Bundled with E&O often
> - **Quote from:** Hiscox, Next Insurance, or local SW FL broker

---

## Step 2: Tech Infrastructure (Week 1–2)

### 2.1 API Keys
| Key | Sign Up | Cost |
|-----|---------|------|
| **NVIDIA NIM** | https://build.nvidia.com/settings/api-keys | Free (40 RPM) |
| **OpenRouter** | https://openrouter.ai/keys | Free (backup) |
| **GitHub** | Already have it | Free |
| **Streamlit Cloud** | https://streamlit.io/cloud | Free tier |

### 2.2 Domain & Email
- **Domain:** $12/yr at Namecheap or Cloudflare
- **Email:** Free via Zoho Mail (5GB free) or upgrade to Google Workspace ($6/mo)
- **Suggestions:** `blueprintaisystem.com`, `blueprint-ai.com`, `tejasai.com`

### 2.3 Demo Setup
```bash
# From the demos directory:
pip install -r requirements.txt
# Edit config.py with your NVIDIA NIM API key
streamlit run hub.py
```

---

## Step 3: Target Account List — SW Florida

### Sector A: Healthcare
> [!info] Focus on multi-specialty groups with 5+ providers

| Company | Location | Contact Approach |
|---------|----------|------------------|
| **Millennium Physician Group** | Fort Myers (HQ) | LinkedIn VP of Ops — pitch AI scribe for their 400+ providers |
| **Florida Cancer Specialists** | Fort Myers | Cold email — focus on clinical documentation efficiency |
| **Naples Comprehensive Health** | Naples | Attend their networking events |
| **VIPcare** | Multiple SW FL locations | Primary care focus — high documentation burden |
| **Pediatric Healthcare** | Cape Coral | Smaller group, easier sell, good case study |
| **Lee Health** | Fort Myers | Major system — long sales cycle, start with a department pilot |

**Healthcare Outreach Strategy:**
1. Find the Practice Administrator or Operations Director on LinkedIn
2. Send: "I'm a local AI engineer who built an AI clinical note system. Can I show you a 10-minute demo?"
3. Offer: Free pilot for 2 weeks on 1 provider's transcripts

### Sector B: Real Estate

| Company | Location | Contact Approach |
|---------|----------|------------------|
| **John R. Wood Properties** | Naples | Largest independent — pitch lead response automation |
| **Premier Sotheby's International** | Naples | Luxury market — multilingual response is a pain point |
| **Downing-Frye Realty** | Naples | High volume inbound |
| **Gulf Coast Realty** | Fort Myers | Local leader |
| **Realty Executives** | Fort Myers | Mid-size, easier to reach decision makers |
| **Rent Naples** | Naples | Property management — 500+ units, huge pain point |

**Real Estate Outreach Strategy:**
1. Target: Broker/Owner or Director of Operations
2. Message: "I can show you a working system that responds to every inbound lead in <90 seconds with personalized property recommendations. Free to demo."
3. Demo: Use the RE Lead Scorer app with their actual listing data

### Sector C: Construction

| Company | Location | Contact Approach |
|---------|----------|------------------|
| **DeAngelis Diamond Construction** | Naples | High-end commercial — bid estimation pain point |
| **Kraft Construction** | Naples | Large contractor |
| **AJAX Building Corporation** | Fort Myers | Commercial + residential |
| **Waterside Builders** | Fort Myers | Custom homes — smaller, easier first client |
| **Florida Construction Connection** | Estero | Growing firm |
| **ABC Southwest Florida Chapter** | Fort Myers | Attend events — meet 50+ contractors at once |

**Construction Outreach Strategy:**
1. Join ABC SW FL chapter (https://abcswfl.org) — attend their breakfast meetings
2. Use the "free workflow audit" offer in person
3. Demo: Enter their actual project specs into the Bid Estimator

### Sector D: MSP Partners (Channel)

| Company | Focus | Partnership Angle |
|---------|-------|-------------------|
| **Nexus IT Group** | Fort Myers | They handle infra, you handle AI layer |
| **Tech Solutions SWFL** | Naples | Referral partnership — they keep client, you deliver AI |
| **Integrity Technology Solutions** | Fort Myers | Potential channel partner |
| **CMIT Solutions** | Fort Myers | National franchise, local presence |

**MSP Outreach Strategy:**
1. "Your clients need AI, but you don't have ML engineers. I handle delivery, you keep the relationship. We split the revenue."
2. Offer: 15-20% referral fee on every engagement they bring in

---

## Step 4: LinkedIn & Online Presence

### 4.1 Profile Optimization
```
Headline: AI Implementation Engineer | Building Production AI Systems for 
         Southwest Florida Healthcare, Real Estate & Construction

About (first 3 lines):
I build working AI systems for SW Florida businesses — not slide decks or 
strategy documents. I specialize in custom LLM applications (RAG pipelines, 
automated documentation, intelligent lead response) that go from audit to 
working prototype in 30 days or less.

Based in Fort Myers. Willing to drive anywhere in Lee/Collier County.
```

### 4.2 Content Cadence (3x/week)
| Day | Content |
|-----|---------|
| Monday | Industry insight (e.g., "How AI cuts clinical documentation by 78%") |
| Wednesday | Demo clip — screen record one of your apps |
| Friday | Local angle — "Why SW Florida businesses need local AI expertise" |

### 4.3 Join These Groups
- **Naples Chamber of Commerce** — https://napleschamber.org
- **Greater Fort Myers Chamber** — https://fortmyers.org
- **Estero Chamber** — https://esterochamber.org
- **ABC Southwest Florida** — https://abcswfl.org
- **SWFL Tech Hub** (LinkedIn group)

---

## Step 5: Sales Cadence (Weekly)

### Monday — Research & List Building
- Find 5 new prospects per sector (healthcare, real estate, construction)
- Add to tracking sheet with LinkedIn URL and any mutual connections

### Tuesday — Outreach
- Send 5 LinkedIn connection requests + messages
- Send 3 cold emails to companies with public contact info

### Wednesday — Follow-ups
- Follow up on any responses from earlier in the week
- Attend any local Chamber/networking events

### Thursday — Demos
- Run live demos for interested prospects
- Offer free "30-minute workflow audit" to all demos

### Friday — Pipeline Review
- Review what's working, adjust scripts
- Update tracking sheet

---

## Step 6: Pricing & Closing

### First Client Pricing Strategy
> [!important] Don't compete on price. Compete on speed and being local.

| Engagement | Your Price | Deloitte/Accenture Equivalent | Advantage |
|------------|------------|-------------------------------|-----------|
| Audit | $5k–$10k | $25k–$50k | 70% cheaper, delivered in 2 weeks |
| Pilot | $25k–$50k (discounted for first 2 clients) | $100k–$200k | 75% cheaper, delivered in 30 days |
| Retainer | $5k–$12k/mo | $20k–$50k/mo | Fraction of cost, direct access to engineer |

### Closing Script
```
"I've shown you the working system. You've seen it process your data. 
Here's what I propose:

1. One-week paid pilot: $X to run on your actual workflow
2. If it works to your satisfaction, we move to a monthly retainer of $Y
3. If it doesn't, you owe nothing beyond the pilot fee

No long-term contract required. The technology speaks for itself."
```

---

## Quick Reference: One-Page Checklist

- [ ] Get NVIDIA NIM API key
- [ ] Test all 3 demos locally (`streamlit run demos/hub.py`)
- [ ] Register domain ($12)
- [ ] Set up professional email
- [ ] Optimize LinkedIn profile
- [ ] Join 2 Chamber of Commerce groups
- [ ] Build target list of 20 companies (healthcare + real estate + construction)
- [ ] Send 10 LinkedIn messages this week
- [ ] Attend 1 local business networking event
- [ ] Land first paid audit ($5k–$10k)
- [ ] Use that revenue to file LLC ($125)
- [ ] Deliver audit → convert to pilot
- [ ] Deliver pilot → convert to retainer
