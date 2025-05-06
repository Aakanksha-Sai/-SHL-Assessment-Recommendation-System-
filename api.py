from fastapi import FastAPI
from pydantic import BaseModel
from recommend import recommend

app = FastAPI()

class Query(BaseModel):
    query: str

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/recommend")
def get_recommendation(q: Query):
    results = recommend(q.query)
    recs = []
    for _, row in results.iterrows():
        recs.append({
            "url": row["URL"],
            "adaptive_support": row["Adaptive/IRT Support"],
            "description": row["Assessment Name"],  # Or add a Description column if you want
            "duration": int(row["Duration"]),
            "remote_support": row["Remote Testing Support"],
            "test_type": [tt.strip() for tt in row["Test Type"].split(",")] if isinstance(row["Test Type"], str) else []
        })
    return {"recommended_assessments": recs}
