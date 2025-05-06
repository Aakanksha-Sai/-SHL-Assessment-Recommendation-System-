from fastapi import FastAPI
from pydantic import BaseModel
from recommend import recommend
import pandas as pd

app = FastAPI()

class Query(BaseModel):
    query: str

@app.get("/health")
def health():
    # Response must be {"status": "healthy"}
    return {"status": "healthy"}

@app.post("/recommend")
def get_recommendation(q: Query):
    results = recommend(q.query)
    # Prepare the response as specified
    recs = []
    for _, row in results.iterrows():
        recs.append({
            "url": row["URL"],
            "adaptive_support": row["Adaptive/IRT Support"],
            "description": row.get("Description", row["Assessment Name"]),  # fallback if Description missing
            "duration": int(row["Duration"]),
            "remote_support": row["Remote Testing Support"],
            "test_type": [tt.strip() for tt in row["Test Type"].split(",")] if isinstance(row["Test Type"], str) else []
        })
    return {"recommended_assessments": recs}
