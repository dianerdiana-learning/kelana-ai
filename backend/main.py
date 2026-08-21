from services.trip_service import (
    calculate_daily_budget,
    get_trip_category,
    get_travel_season,
    get_recommended_transportation,
    get_recommended_places,
)

from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session

from database import init_db, SessionLocal, get_db
from models.trip import Trip
from configs.env import env

from validations.trip import TripRequest, TripUpdateBudget


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    init_db()
    yield
    # Shutdown logic (jika ada)


app = FastAPI(lifespan=lifespan)


@app.get("/")
def home():
    return {"message": "Welcome to KelanaAI"}


@app.get("/health", tags=["Health Check"])
def health_check():
    return {"status": "ok"}


@app.post("/api/v1/trips")
def create_trip(request: TripRequest, db: Session = Depends(get_db)):
    daily_budget = calculate_daily_budget(request.budget, request.days)
    category = get_trip_category(request.budget)
    recommendation_transport = get_recommended_transportation(category)

    trip = Trip(
        destination=request.destination,
        budget=request.budget,
        days=request.days,
        category=category,
        daily_budget=daily_budget,
    )

    db.add(trip)
    db.commit()
    db.refresh(trip)

    return trip


@app.get("/api/v1/trips")
def get_trips(db: Session = Depends(get_db)):
    trips = db.query(Trip).all()

    return trips


@app.get("/api/v1/trips/{trip_id}")
def get_trip_by_id(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(Trip).filter(Trip.id == trip_id).first()

    if not trip:
        raise HTTPException(status_code=404, detail="Data is not found")

    return trip


@app.put("/api/v1/trips/{trip_id}")
def update_trip_by_id(
    trip_id: int, request: TripUpdateBudget, db: Session = Depends(get_db)
):
    trip = db.query(Trip).where(Trip.id == trip_id).first()

    if not trip:
        raise HTTPException(status_code=404, detail="Data is not found")

    daily_budget = calculate_daily_budget(request.budget, trip.days)
    category = get_trip_category(request.budget)

    trip.budget = request.budget
    trip.daily_budget = daily_budget
    trip.category = category

    db.commit()
    db.refresh(trip)

    return trip


@app.delete("/api/v1/trips/{trip_id}")
def delete_trip_by_id(trip_id: int, db: Session = Depends(get_db)):
    trip = db.query(Trip).where(Trip.id == trip_id).first()

    if not trip:
        raise HTTPException(status_code=404, detail="Data is not found")

    db.delete(trip)
    db.commit()

    return "Data deleted successfuly"


@app.get("/api/v1/trip-categories")
def trip_categories():
    return ["Backpacker", "Standard", "Luxury"]


@app.get("/api/v1/recommendations")
def recommendations():
    return ["Tokyo Tower", "Mount Fuji", "Shibuya"]


@app.get("/api/v1/transportations")
def transportations():
    return ["Bus", "Train", "Flight"]
