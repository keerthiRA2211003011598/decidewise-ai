from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import get_agent

app = FastAPI()


class DecisionRequest(BaseModel):
    background: str
    goal: str
    option_a: str
    option_b: str
    risk_tolerance: str


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/analyze-decision")
def analyze_decision(data: DecisionRequest):
    try:
        agent = get_agent()

        prompt = f"""
Background:
{data.background}

Goal:
{data.goal}

Option A:
{data.option_a}

Option B:
{data.option_b}

Risk Tolerance:
{data.risk_tolerance}
"""

        result = agent.run(prompt)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
