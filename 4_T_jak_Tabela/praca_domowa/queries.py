GET_TRACKS = """SELECT Name FROM tracks WHERE Composer == ? ORDER BY Name ASC"""

ALL_TRACKS = """SELECT * FROM tracks LIMIT ? OFFSET ?"""

ADD_ALBUM = """INSERT INTO albums (Title, ArtistId) VALUES(?, ?)"""

SELECT_ALBUM_BY_ID = """SELECT * FROM albums WHERE AlbumId == ?"""

SELECT_ARTIST_BY_ID = """SELECT * FROM artists WHERE ArtistId == ?"""

SELECT_CUSTOMER_BY_ID = """SELECT * FROM customers WHERE CustomerId == ?"""

SELECT_NAME_COMPOSER = "SELECT name, composer FROM tracks WHERE trackid = ?"

PUT_CUSTOMER_INFO = """UPDATE customers SET {} WHERE CustomerId == ?"""

SUM_ALL_EXPENSES = """
SELECT customers.CustomerId, Email, Phone, ROUND(SUM(total), 2) AS Sum
FROM customers
INNER JOIN invoices ON customers.CustomerId = invoices.CustomerId
GROUP BY customers.CustomerId, Email, Phone
ORDER BY Sum DESC, customers.CustomerId"""

GET_GENRES_SALES = """
SELECT genres.Name, SUM(Quantity) AS Sum
FROM invoice_items
INNER JOIN tracks ON invoice_items.TrackId = tracks.TrackId
INNER JOIN genres ON tracks.GenreId = genres.GenreId
GROUP BY tracks.GenreId
ORDER BY Sum DESC, genres.Name
"""
