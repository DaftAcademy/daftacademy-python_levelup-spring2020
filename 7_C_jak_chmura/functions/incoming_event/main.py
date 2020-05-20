import json
from datetime import datetime

from google.cloud import pubsub_v1


STATUS_CHOICES = [
    "LOGIN",
    "IDLE",
    "TAKE",
    "MOVING",
    "DELIVERED",
    "PAUSE",
    "LOGOUT",
    "ERROR",
]

PROJECT_ID = "daftacademy-test"
TOPIC_NAME = "incoming-events"


def incoming_event(request):
    event = {}
    errors = []
    if not request.args:
        errors.append("No parameters at all")
    else:
        if "status" not in request.args:
            errors.append("Status is required")
        else:
            status = request.args["status"]
            if status not in STATUS_CHOICES:
                errors.append(
                    f"Parameter status {status!r} is not in: {STATUS_CHOICES!r}"
                )
            else:
                event["status"] = status
        if "cid" not in request.args:
            errors.append("Parameter cid is required")
        else:
            event["cid"] = request.args["cid"]

    if errors:
        return json.dumps(errors), 403

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(PROJECT_ID, TOPIC_NAME)

    event["ts"] = datetime.now().isoformat()

    event_data = json.dumps(event)
    publisher.publish(topic_path, data=event_data.encode("utf-8"))
    return event_data
