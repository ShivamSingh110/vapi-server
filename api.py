from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import date
import uvicorn

app = FastAPI()

class TripSchema(BaseModel):
    source: str = Field(..., description="Starting location of the journey")
    destination: str = Field(..., description="End location of the journey")
    startDate: str = Field(..., description="Trip start date")
    numberOfDays: int = Field(..., description="Total duration of the trip in days")
    stay: str = Field(..., description="Accommodation details")
    commute: str = Field(..., description="Mode of transportation")
    activity: str = Field(..., description="Planned activities during the trip")

@app.post("/submit-trip")
async def submit_trip(trip_data: TripSchema):
    return {"result": "Details of trip is sent to your mobile number"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
