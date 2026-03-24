import pickle
import pandas as pd 
import os

# Build path relative to this file's location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'model.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)
    
class_labels = model.classes_.tolist()
    
def predict_output(user_input: dict):
    
    input_df = pd.DataFrame(user_input)
    predicted_class = model.predict(input_df)[0]
    
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)
    
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))
    
    return {
        "Predicted Catgory": predicted_class,
        "Confidence": confidence,
        "All Class Probabilites": class_probs
    }