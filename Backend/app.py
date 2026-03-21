from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import pickle
import pandas as pd 
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import traceback

with open('../Model/model.pkl', 'rb') as f:
    model = pickle.load(f)
    
app = FastAPI()

class UserInput(BaseModel):
    
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the user")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the user in KG")]
    height: Annotated[float, Field(..., gt=0, description="Height of the user meters")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Anual salary in LPA")]
    smoker: Annotated[bool, Field(..., description="Is user a smoker?")]
    city: Annotated[str, Field(..., description="The city the user currently lives in.")] 
    occupation: Annotated[Literal['retired','freelancer','student','government_job',
                                'business_owner','unemployed','private_job'], Field(..., description="A general name of the occupation")]
    
    
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age<45:
            return "adult"
        elif self.age<60:
            return "middleaged"
        else:
            return "senior"
        
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker and self.bmi >25:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def city_tier(self) -> int:
        
        tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
        tier_2_cities = ["Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
            "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
            "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
            "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
            "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
            "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"]
        
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        
@app.post('/predict')
def predict_premium(data: UserInput):
    try:
        # Debug: Log the input data
        print(f"Received data: {data}")
        
        user_data_df = pd.DataFrame({
            'income_lpa': [data.income_lpa],
            'occupation': [data.occupation],
            'bmi': [data.bmi],
            'age_group': [data.age_group],
            'lifestyle_risk': [data.lifestyle_risk],
            'city_tier': [data.city_tier]
        })
        
        print(f"DataFrame for prediction: {user_data_df}")
        print(f"DataFrame columns: {user_data_df.columns.tolist()}")
        
        prediction = model.predict(user_data_df)[0]
        
        return JSONResponse(status_code=200, content={'message': f"Predicted category is {prediction}"})
    
    except Exception as e:
        error_msg = f"Prediction error: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)