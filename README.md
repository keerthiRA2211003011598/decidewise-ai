# DecideWise – AI Decision Explainer Agent

DecideWise is a full-stack Generative AI application that helps students and early professionals make better career and academic decisions using structured, explainable AI reasoning.

## 🚀 Live Application
(Will be added after deployment)

## 🧠 What Problem It Solves
Many students struggle to make important decisions like:
- Placements vs higher studies
- Switching domains
- Choosing between multiple career options

DecideWise analyzes these decisions logically and provides a clear, explainable recommendation.

## ✨ Features
- Structured decision analysis
- Pros & cons comparison
- Risk identification
- Final recommendation with confidence score
- Clean and simple UI

## 🛠️ Tech Stack
- Frontend: Streamlit
- Backend: FastAPI
- AI Agent: Pydantic AI
- Model Provider: OpenRouter (LLaMA-3)
- Deployment: Streamlit Cloud + Render

## ⚙️ How It Works
1. User enters background, goal, and options
2. Backend sends input to AI agent
3. AI returns validated structured output
4. Frontend displays explainable results

## 📦 Setup (Local)
```bash
pip install -r backend/requirements.txt
python -m uvicorn backend.main:app
python -m streamlit run frontend/app.py
