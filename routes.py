#!/usr/bin/python3
import handlers
# import callbacks
# import orders
# import sms


def routes_setup():
    return [
        (r'/payment_app.cgi', handlers.Main),
        ]