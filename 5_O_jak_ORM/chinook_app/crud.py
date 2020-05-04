from sqlalchemy.orm import Session

from . import models, schemas


def get_artists(db: Session):
    return db.query(models.Artist).all()


def get_artist(db: Session, artist_id: int):
    return db.query(models.Artist).filter(models.Artist.artist_id == artist_id).first()