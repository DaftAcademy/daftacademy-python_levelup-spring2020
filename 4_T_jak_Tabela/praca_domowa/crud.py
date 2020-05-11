import queries
from database import query


def get_all_trucks(per_page, page):
    return query(queries.ALL_TRACKS, (per_page, page * per_page)).fetchall()


def get_all_composer_tracks(composer_name):
    return query(queries.GET_TRACKS, (composer_name,)).fetchall()


def get_album_by_id(album_id):
    return query(queries.SELECT_ALBUM_BY_ID, (album_id,)).fetchone()


def get_artist_by_id(artist_id):
    return query(queries.SELECT_ARTIST_BY_ID, (artist_id,)).fetchone()


def add_new_album(title, artist_id):
    return query(queries.ADD_ALBUM, (title, artist_id))


def get_customer_by_id(customer_id):
    return query(queries.SELECT_CUSTOMER_BY_ID, (customer_id,)).fetchone()


def edit_customer_info(customer_id, query_sub_string, query_params):
    query_string = queries.PUT_CUSTOMER_INFO.format(query_sub_string)
    query(query_string, query_params)
    return get_customer_by_id(customer_id)


def get_statistic_customers():
    return query(queries.SUM_ALL_EXPENSES).fetchall()


def get_statistic_genres():
    return query(queries.GET_GENRES_SALES).fetchall()
