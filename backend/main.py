from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import agent

app = FastAPI(
    title="DecideWise AI",
    description="An explainable AI decision analysis agent",
    version="1.0"
)

# Input schema for API
class DecisionRequest(BaseModel):
    background: str
    goal: str
    option_a: str
    option_b: str
    risk_tolerance: str


@app.post("/analyze-decision")
async def analyze_decision(request: DecisionRequest):
    try:
        # Combine user inputs into a single prompt
        user_prompt = f"""
Background:
{request.background}

Goal:
{request.goal}

Option A:
{request.option_a}

Option B:
{request.option_b}

Risk Tolerance:
{request.risk_tolerance}
"""

        result = await agent.run(user_prompt)
        return result.data

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Decision analysis failed. Please try again later."
        )
