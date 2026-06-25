# SEO-Analyzer
A full-stack SEO auditing tool built with FastAPI, BeautifulSoup, and JavaScript for website analysis and automated recommendations.

## Overview

SEO Analyzer is a Python-based website auditing tool built with FastAPI and BeautifulSoup.

The application analyzes technical SEO factors, evaluates website performance, checks accessibility issues, and provides keyword insights.

## Features

- Automated SEO score calculation
- Title tag analysis
- Meta description analysis
- Heading structure analysis (H1, H2, H3)
- Image ALT attribute checking
- Website loading time measurement
- Broken link detection
- Keyword analysis
- Word count analysis
- Top keyword extraction
- Keyword placement analysis (title, description, headings)
- Interactive web dashboard

## Tech Stack

### Backend

- Python
- FastAPI
- BeautifulSoup4
- Requests
- Uvicorn

### Frontend

- HTML
- CSS
- JavaScript



## How to Run on MacOS

### 1. Clone the repository

```bash
git clone https://github.com/samintghz/SEO-Analyzer.git
2. Install dependencies

Navigate to the backend folder:

cd backend

Install required packages:

pip install -r requirements.txt
3. Start the backend server

Run:

uvicorn main:app --reload

The API will run at:

http://127.0.0.1:8000
API Usage

Endpoint:

POST /analyze

Example request:

{
  "url": "https://github.com",
  "keyword": "developer"
}

The API returns:

SEO score
Technical SEO score
Performance score
Accessibility score
Keyword analysis
Recommendations
Future Improvements
PDF report generation
Advanced SEO metrics
Database integration
User authentication
Author

Samin Taghizadeh
