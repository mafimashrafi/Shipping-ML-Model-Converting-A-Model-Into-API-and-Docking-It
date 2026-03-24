import pickle
import pandas as pd 
import os

# Build path relative to this file's location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'model.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)
    
def predict_output(user_input: dict):
    
    input_df = pd.DataFrame(user_input)
    output = model.predict(input_df)
    
    return output