from flask import Flask
from apis.videos_api.endpoints import video_ns

app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Server Running'

app.register_blueprint(video_ns)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)