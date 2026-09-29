# Currency Exchange Agent

A small Google ADK agent that answers currency conversion and exchange-rate
questions. The Gemini-powered agent calls a `get_exchange_rate` tool, which
fetches rates from the free [Frankfurter API](https://www.frankfurter.app/)
(European Central Bank data, no API key needed), and explains the result.

## Features

- Latest exchange rate between any two currencies supported by Frankfurter
- Historical rates for a given date (`YYYY-MM-DD`)

## Tech stack

- Python 3.10+
- Google ADK (`google-adk`) with Gemini (model `gemini-3.1-flash`, set in `agent.py`)
- `requests` + Frankfurter API

## Project structure

```
money/
├── agent.py          # root_agent (currency_exchange_agent)
├── tools.py          # get_exchange_rate tool (Frankfurter API)
├── requirements.txt
└── .env.example
```

## Prerequisites

- Python 3.10 or newer
- A Gemini API key from Google AI Studio

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt

copy .env.example .env          # cp .env.example .env on macOS / Linux
```

| Variable | Required | Where to get it |
|----------|----------|-----------------|
| `GOOGLE_API_KEY` | Yes | [Google AI Studio](https://aistudio.google.com/apikey) |
| `GOOGLE_GENAI_USE_VERTEXAI` | No | Keep `FALSE` to use the AI Studio key |

## Run

ADK discovers agents as sub-folders of the directory you run it from, so run it
from the **parent** of this folder. Because `agent.py` uses `from tools import ...`,
this folder must also be on `PYTHONPATH`:

```bash
cd ..
# Windows (PowerShell)
$env:PYTHONPATH = "money"; adk web
# macOS / Linux
PYTHONPATH=money adk web
```

Open http://localhost:8000 and select the `money` agent. Use `adk run money`
instead of `adk web` for a terminal chat.

## Usage

Example prompts:

- "What is the USD to EUR rate today?"
- "Convert 250 GBP to JPY."
- "What was the EUR to USD rate on 2024-01-15?"

Note: Frankfurter only covers the currencies published by the ECB (for example,
PKR is not included).
