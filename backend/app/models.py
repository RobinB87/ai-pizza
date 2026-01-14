from datetime import datetime

from sqlmodel import Field, SQLModel


class PizzeriaBase(SQLModel):
    name: str
    address: str
    rating: float | None = None
    google_maps_url: str | None = None
    review: str | None = None


class Pizzeria(PizzeriaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class PizzeriaCreate(PizzeriaBase):
    pass


class PizzeriaRead(PizzeriaBase):
    id: int
    created_at: datetime
    updated_at: datetime
