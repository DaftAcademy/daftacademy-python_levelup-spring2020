from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import schemas
from . import crud
from .database import get_db


router = APIRouter()


@router.get("/artists/{artist_id}", response_model=schemas.Artist)
async def get_artist(artist_id: int, db: Session = Depends(get_db)):
    db_artist = crud.get_artist(db, artist_id)
    if db_artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")
    return db_artist


@router.get("/artists", response_model=List[schemas.Artist])
async def get_artists(db: Session = Depends(get_db)):
    return crud.get_artists(db)