CREATE TABLE events (
    ts timestamp not null,
    cid varchar(255) not null,
    status varchar(255) not null
);
CREATE INDEX events_ts ON events (ts);
CREATE INDEX events_cid ON events (cid, ts);
