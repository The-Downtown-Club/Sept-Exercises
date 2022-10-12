from flask import Blueprint
from flask.views import View
from apis.videos_api.views import api_method, catch_bad_requests

video_ns = Blueprint('videos', __name__, url_prefix='/')

class MyView(View):
    @video_ns.route('/')
    def get():
        return api_method()

    @video_ns.route('/<x>')
    def catch_all(x):
        return catch_bad_requests(x)