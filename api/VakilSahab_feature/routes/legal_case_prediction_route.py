import fastapi
from pydantic import BaseModel
import pickle
import numpy as np
import os
import logging

router = fastapi.APIRouter()

# Determine the absolute path to the models
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
MODEL_PATH = os.path.join(BASE_DIR, "data", "models", "legal_case_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "data", "models", "scaler.pkl")

# Load model globally on startup (or you can use lifespan events if preferred)
try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)
    logging.info("Legal Case Predictor models loaded successfully.")
except Exception as e:
    logging.error(f"Failed to load predictive models: {e}")
    model = None
    scaler = None


class CaseInput(BaseModel):
    case_type: int
    lawyer_exp: float
    judge_exp: float
    judge_count: int


def get_case_strength(win: float) -> str:
    if win > 70:
        return "Strong"
    elif win > 50:
        return "Moderate"
    else:
        return "Weak"


@router.post("/predict", operation_id="legal_case_prediction")
async def predict_case(case_input: CaseInput):
    """
    Predict the win probability and strength of a legal case based on specific features.
    
    Features:
    - case_type (int): Type of the case encoded as integer
    - lawyer_exp (float): Years of experience of the lawyer
    - judge_exp (float): Years of experience of the judge
    - judge_count (int): Number of judges presiding
    """
    if model is None or scaler is None:
        return fastapi.responses.JSONResponse(
            status_code=500, 
            content={"error": "Prediction models are not loaded. Please check the server logs."}
        )

    try:
        sample = np.array([[
            case_input.case_type,
            case_input.lawyer_exp,
            case_input.judge_exp,
            case_input.judge_count
        ]])

        sample_scaled = scaler.transform(sample)
        prob = model.predict_proba(sample_scaled)
        win = prob[0][1] * 100

        return {
            "win_probability": round(win, 2),
            "case_strength": get_case_strength(win)
        }
    except Exception as e:
        logging.error(f"Error during prediction: {str(e)}")
        return fastapi.responses.JSONResponse(status_code=500, content={"error": str(e)})
