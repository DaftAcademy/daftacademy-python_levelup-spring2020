from pydantic import BaseModel


class AlbumItem(BaseModel):
    title: str
    artist_id: int


class CustomerItem(BaseModel):
    company: str = None
    address: str = None
    city: str = None
    state: str = None
    country: str = None
    postalcode: str = None
    fax: str = None
