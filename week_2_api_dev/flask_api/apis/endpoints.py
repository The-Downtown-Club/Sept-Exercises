from flask import current_app

def api_method():
    print(current_app.db_session)
    return "API method",500