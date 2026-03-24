from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model
import traceback
    
app = FastAPI()

Model_Version = "1.0.0"
        
@app.get('/')
def home():
    return "Wlcome to the home page!!!"

@app.get('/health')
def health_check():
    return {
        "status": "OK",
        "version": Model_Version,
        "model_loaded": model is not None
    }
        
@app.post('/predict', response_model = PredictionResponse)
def predict_premium(data: UserInput):
    try:
        # Debug: Log the input data
        print(f"Received data: {data}")
        
        user_input = {
            'income_lpa': [data.income_lpa],
            'occupation': [data.occupation],
            'bmi': [data.bmi],
            'age_group': [data.age_group],
            'lifestyle_risk': [data.lifestyle_risk],
            'city_tier': [data.city_tier]
        }
        
        prediction = predict_output(user_input)
        
        return JSONResponse(status_code=200, content={'message': f"Response: {prediction}"})
    
    except Exception as e:
        error_msg = f"Prediction error: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)
        raise HTTPException(status_code=500, detail=error_msg)