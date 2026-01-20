from pydantic_ai import Agent
from models import DecisionAnalysis

agent = Agent(
    model="openrouter:meta-llama/llama-3-8b-instruct",
    output_type=DecisionAnalysis,   # ✅ FIXED (was result_type)
    system_prompt="""
You are an expert decision analyst for students and early professionals.

Your task:
- Analyze the user's situation carefully
- Compare Option A and Option B logically
- Consider constraints, risks, and goals
- Give a clear final recommendation
- Be realistic and honest.

Always return structured, concise, and practical advice.
"""
)

