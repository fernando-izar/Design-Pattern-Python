from src.routes import route1


def post_http1():
    http_message = {
        "method": "POST",
        "header": {
            "token": "Bearer jioiaefi48904729kldan324",
            "origin": "http://something.other.org",
        },
        "body": {"name": "Lhama", "message": "Hello Word"},
    }

    route1(http_message)
