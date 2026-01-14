import json

def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "content-type": "application/json",
            "access-control-allow-origin": "*",
        },
        "body": json.dumps({"ok": True}),
    }
