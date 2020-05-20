import os
import json

import sqlalchemy


def cid_stats(request):
    errors = []
    if not request.args:
        errors.append("No parameters at all")
    else:
        if "cid" not in request.args:
            errors.append("Parameter cid is required")
    if errors:
        return json.dumps(errors), 403

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

    cid = request.args["cid"]

    with db.connect() as conn:
        events_data = conn.execute(
            f"SELECT ts, cid, status FROM events WHERE cid={cid!r} ORDER BY ts DESC LIMIT 100"
        ).fetchall()

    events = []
    for event_data in events_data:
        events.append(
            {
                "ts": event_data[0].isoformat(),
                "cid": event_data[1],
                "status": event_data[2],
            }
        )
    return json.dumps(events)
