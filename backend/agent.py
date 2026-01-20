from pydantic_ai import Agent
from models import DecisionAnalysis
import os

_agent = None

def get_agent():
    global _agent

    if _agent is None:
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise RuntimeError("OPENROUTER_API_KEY not set")

        _agent = Agent(
            model="openrouter:meta-llama/llama-3-8b-instruct",
            output_type=DecisionAnalysis,
            system_prompt="""
You are an expert decision analyst for students and early professionals.

Analyze the user's situation carefully.
Compare Option A and Option B logically.
Highlight risks and trade-offs.
Give a clear final recommendation.
"""
        )

    return _agent
