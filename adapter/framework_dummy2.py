from src.routes import route2


def post_http2():
    http_message = {
        "HTTP_method": "POST",
        "HTTP_header": [
            ("token", "Bearer jioiaefi48904729kldan324"),
            ("origin", "http://something.other.org"),
        ],
        "HTTP_body": [("name", "Lhama"), ("message", "Hello Word")],
    }

    route2(http_message)
