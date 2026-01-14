from pydantic import BaseModel


class Pizzeria(BaseModel):
    id: int
    name: str
    address: str
    rating: float | None = None
    google_maps_url: str | None = None
