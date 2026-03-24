from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    
    predicted_class: str = Field(
        ...,
        description = "The predicted premium category",
        example = 'High'
    )
    confidence: float = Field(
        ...,
        description = "The model is this much confidence about it's prediction",
        example = 0.9000
    )
    class_probs: Dict[str, float] = Field(
        ...,
        description = "Model's confidence on predicting all the categories",
        example = {"Low": 0.33, "Medium": 0.33, "High": 0.34}
    )