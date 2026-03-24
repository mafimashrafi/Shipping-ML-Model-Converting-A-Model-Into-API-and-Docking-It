from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated, Literal
from config.city_tier import tier_1_cities, tier_2_cities

class UserInput(BaseModel):
    
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the user")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the user in KG")]
    height: Annotated[float, Field(..., gt=0, description="Height of the user meters")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Anual salary in LPA")]
    smoker: Annotated[bool, Field(..., description="Is user a smoker?")]
    city: Annotated[str, Field(..., description="The city the user currently lives in.")] 
    occupation: Annotated[Literal['retired','freelancer','student','government_job',
                                'business_owner','unemployed','private_job'], Field(..., description="A general name of the occupation")]
    
    
    @field_validator('city')
    @classmethod
    def veirfy_city(cls, value: str) -> str:
        
        valid_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune","Jaipur",
                        "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
                        "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
                        "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
                        "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
                        "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
                        "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"]
        
        value = value.strip().title()
        if value not in valid_cities:
            raise ValueError(f"This city is not valid. Use one of these: {valid_cities}")
        return value
    
    @field_validator('occupation')
    @classmethod
    def normalize_occupation(cls, value: str) -> str:
        value = value.strip().lower()
        return value
    
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
        
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3