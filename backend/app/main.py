from fastapi import FastAPI

from app.models import Pizzeria

app = FastAPI(
    title="AI Pizza API",
    description="API for tracking pizzerias visited in Berlin",
    version="0.1.0",
)

# In-memory storage for pizzerias (will be replaced with a database later)
pizzerias_db: list[Pizzeria] = [
    Pizzeria(
        id=1,
        name="Standard Serious Pizza",
        address="Skalitzer Str. 42, 10999 Berlin",
        rating=4.5,
        google_maps_url="https://maps.google.com/?q=Standard+Serious+Pizza+Berlin",
    ),
    Pizzeria(
        id=2,
        name="Gazzo",
        address="Hobrechtstraße 57, 12047 Berlin",
        rating=4.7,
        google_maps_url="https://maps.google.com/?q=Gazzo+Berlin",
    ),
]


@app.get("/")
def read_root():
    return {"message": "Welcome to AI Pizza API"}


@app.get("/pizzerias", response_model=list[Pizzeria])
def get_all_pizzerias():
    """Get all pizzerias."""
    return pizzerias_db
