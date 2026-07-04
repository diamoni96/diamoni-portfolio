# Dia Moni Portfolio

A modern Flask portfolio website for Dia Moni, presenting her as an AI/ML Enthusiast, Python Developer, and Computer Science and Engineering student. The content is organized from the provided CV details and shaped into a polished, responsive personal brand site.

## Features

- Premium glassmorphism interface with layered gradients, blur, soft shadows, and responsive spacing.
- Strong hero section with resume, projects, and contact calls to action.
- CV-based sections for About, Education, Skills, Projects, Leadership, Achievements, Certificates, and Contact.
- Resume preview route at `/resume` and downloadable CV route at `/download-cv`.
- Clean Flask routing with Jinja templates and organized static assets.
- Vercel-ready configuration for Python serverless deployment.

## Portfolio Sections

- Hero: Dia Moni, AI/ML Enthusiast | Python Developer.
- About: AI/ML, Python, backend development, automation, and reliable systems.
- Education: Southeast University, 11/2023 - Present, Dhaka, Bangladesh.
- Skills: Programming, backend, core CS, AI/data, tools, cybersecurity, and soft skills.
- Projects: QueueStorm, Student Management System, and University Complaint Analyzer.
- Leadership: IEEE Computer Society Southeast University Student Branch Chapter volunteer work.
- Achievements: SUST CSE Carnival 2026 Hackathon finalist and DUET CSE Carnival 2026 ICT Olympiad participant.
- Certificates: Structuring Machine Learning Projects, Maximize Productivity With AI Tools, and C)PTE.
- Contact: Email, LinkedIn, GitHub, and resume access.

## Tech Stack

- Python
- Flask
- Jinja templates
- HTML
- CSS
- JavaScript
- Python 3.12

## Local Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## GitHub Upload

```bash
git init
git add .
git commit -m "Build Dia Moni portfolio"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

Replace the remote URL with the target GitHub repository.

## Vercel Deployment

1. Push the project to GitHub.
2. Import the repository in Vercel.
3. Keep the framework preset as Other if Vercel does not auto-detect Flask.
4. Vercel will detect the top-level Flask `app` instance in `app.py` and install dependencies from `requirements.txt`.
5. After deployment, verify the home page and `/resume` route.

The included `vercel.json` only adds schema validation and a function duration setting.

## Playwright Smoke Test

After starting Flask locally, run the included Playwright test from a Node.js environment:

```bash
npm install
npx playwright install chromium
npm test
```

The test expects the Flask app to be running at `http://127.0.0.1:5000`.
