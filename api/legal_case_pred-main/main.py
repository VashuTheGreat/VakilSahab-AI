from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import pickle
import numpy as np

app = FastAPI()

# Load model
model = pickle.load(open("legal_case_model.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))

FEATURES=['case_type','lawyer_exp','judge_exp','judge_count']

def case_strength(win):

    if win>70:
        return "Strong"

    elif win>50:
        return "Moderate"

    else:
        return "Weak"


@app.get("/")
def home():

    return {"message":"Legal Case Predictor API running"}


@app.post("/predict")

def predict(case_type:int,
            lawyer_exp:float,
            judge_exp:float,
            judge_count:int):

    sample=np.array([[case_type,
                      lawyer_exp,
                      judge_exp,
                      judge_count]])

    sample=scaler.transform(sample)

    prob=model.predict_proba(sample)

    win=prob[0][1]*100

    return {

        "win_probability":round(win,2),

        "case_strength":case_strength(win)

    }
    
    from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from pydantic import BaseModel

class CaseInput(BaseModel):
    case_type:int
    lawyer_exp:float
    judge_exp:float
    judge_count:int