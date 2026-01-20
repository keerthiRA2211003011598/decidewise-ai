from pydantic import BaseModel, Field
from typing import List

class DecisionAnalysis(BaseModel):
    key_factors: List[str] = Field(
        description="Important factors considered while making the decision"
    )

    option_a_analysis: List[str] = Field(
        description="Pros and cons of option A"
    )

    option_b_analysis: List[str] = Field(
        description="Pros and cons of option B"
    )

    risks: List[str] = Field(
        description="Possible risks involved in the recommended decision"
    )

    final_recommendation: str = Field(
        description="Clear final recommendation with reasoning"
    )

    confidence_score: int = Field(
        ge=0,
        le=100,
        description="Confidence level of the recommendation from 0 to 100"
    )
