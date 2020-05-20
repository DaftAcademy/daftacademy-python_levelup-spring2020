import base64
import os
import json

import sqlalchemy


def save_event(event, context):
    incoming_event = json.loads(base64.b64decode(event["data"]))
    print(f"Incoming event {incoming_event!r}")
    db_user = os.environ.get("DB_USER")
    db_pass = os.environ.get("DB_PASS")
    db_name = os.environ.get("DB_NAME")
    cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")
    db = sqlalchemy.create_engine(
        # Equivalent URL:
        # postgres+pg8000://<db_user>:<db_pass>@/<db_name>?unix_sock=/cloudsql/<cloud_sql_instance_name>/.s.PGSQL.5432
        sqlalchemy.engine.url.URL(
            drivername="postgres+pg8000",
            username=db_user,
            password=db_pass,
            database=db_name,
            query={
                "unix_sock": "/cloudsql/{}/.s.PGSQL.5432".format(
                    cloud_sql_connection_name
                )
            },
        ),
        pool_size=5,
        max_overflow=2,
        pool_timeout=30,  # 30 seconds
        pool_recycle=1800,  # 30 minutes
    )
    with db.connect() as conn:
        conn.execute(
            "INSERT INTO events (ts, cid, status) VALUES ({ts!r}, {cid!r}, {status!r})".format(
                **incoming_event
            )
        )
