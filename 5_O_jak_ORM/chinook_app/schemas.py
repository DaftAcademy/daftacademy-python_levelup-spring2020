from pydantic import BaseModel

class Artist(BaseModel):
    artist_id: int
    name: str

    class Config:
        orm_mode = True