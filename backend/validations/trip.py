from pydantic import BaseModel


class TripRequest(BaseModel):
    destination: str
    days: int
    budget: float
    travel_style: str


class TripUpdateBudget(BaseModel):
    budget: float
