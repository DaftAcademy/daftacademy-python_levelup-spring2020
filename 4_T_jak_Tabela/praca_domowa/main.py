from fastapi import FastAPI, HTTPException, status

import crud
from schemas import AlbumItem, CustomerItem

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Do or do not. There is no try. # Yoda"}


@app.get("/tracks")
def all_tracks(page: int = 0, per_page: int = 10):
    return crud.get_all_trucks(per_page, page)


@app.get("/tracks/composers")
def all_composer_tracks(composer_name: str):
    data = crud.get_all_composer_tracks(composer_name)
    if data:
        response = [elem["Name"] for elem in data]
        return response
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "The given composer was not found."},
        )


@app.post("/albums", status_code=status.HTTP_201_CREATED)
def post_new_album(item: AlbumItem):
    artist = crud.get_artist_by_id(item.artist_id)
    if artist:
        new_album = crud.add_new_album(item.title, item.artist_id)
        new_album_id = new_album.lastrowid
        return crud.get_album_by_id(new_album_id)

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "The given artist_id was not found."},
        )


@app.get("/albums/{album_id}")
def get_album(album_id: int):
    return crud.get_album_by_id(album_id)


@app.put("/customers/{customer_id}")
def put_customer_info(customer_id: str, item: CustomerItem):
    customer = crud.get_customer_by_id(customer_id)
    if customer:
        sql_placeholders = []
        sql_params = []
        update_data = item.dict(exclude_unset=True)
        [
            [sql_placeholders.append(f"{k} = ?"), sql_params.append(v)]
            for k, v in update_data.items()
        ]
        sql_params.append(customer_id)
        sql_placeholders = ", ".join(sql_placeholders)

        return crud.edit_customer_info(customer_id, sql_placeholders, sql_params)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "The given customer was not found."},
        )


@app.get("/sales")
def customers_expenses(category: str):
    statistics = {
        "customers": crud.get_statistic_customers,
        "genres": crud.get_statistic_genres,
    }

    if category and category in statistics:
        data = statistics[category]()
        return data

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": "The given category was not found."},
        )


"uvicorn main:app --reload"
