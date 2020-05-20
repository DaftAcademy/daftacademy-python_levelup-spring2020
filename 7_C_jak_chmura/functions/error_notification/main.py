import base64
import os
import json
import requests


def error_notification(event, context):
    incoming_event = json.loads(base64.b64decode(event["data"]))
    print(f"Incoming event {incoming_event!r}")
    if incoming_event["status"] == "ERROR":
        url = "https://api.pushover.net/1/messages.json"
        pushover_token = os.environ.get("PUSHOVER_TOKEN")
        pushover_user = os.environ.get("PUSHOVER_USER")
        requests.post(
            url,
            {
                "token": pushover_token,
                "user": pushover_user,
                "message": f"Error!: {incoming_event!r}",
            },
        )
        print(f'Pushed error message: {incoming_event!r}')
