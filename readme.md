# 🐍 Python Data Automation & Web Scraping Portfolio

This repository contains a suite of professional web scraping and data analysis tools. Each project is designed to solve specific business problems, from market research to competitive intelligence.

---

## 📂 Projects Overview

### 1. 🛒 E-Commerce Price Intelligence
**Goal:** Extract product data for competitive monitoring.
- **Features:** Scrapes titles, prices, ratings, and stock status.
- **Data Handling:** Normalizes currency and calculates average market prices.
- **Output:** Structured CSV reports.
- **Tech:** `BeautifulSoup4`, `Pandas`.

### 2. 📊 News Trend Analyzer (NYT)
**Goal:** Real-time monitoring of global news trends.
- **Features:** Automated extraction of headlines from the New York Times.
- **NLP Engine:** Filters "stop-words" and performs word frequency analysis.
- **Visualization:** Generates automated bar charts showing the day's top topics.
- **Tech:** `Requests`, `Matplotlib`, `Regex`.

### 3. 📡 Live Content Tracker
**Goal:** Monitor websites for new updates without duplicates.
- **Features:** Maintains a local history log to ensure only fresh content is captured.
- **Reliability:** Built-in error handling for network timeouts and 404s.
- **Tech:** `OS Library`, `Requests`.

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SuperMorisl/E-Commerce-scrapper-in-python
   cd E-Commerce-scrapper-in-python
   python3 scrapper.py