# To run: $ python run.py

import os
from flask import Flask, jsonify, request
# from flask_cors import CORS

class Config(object):
    SECRET_KEY = 'you-will-never-guess'


APP_DATA = {
    'opmode': 'GSM'
}


# cors = CORS()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # cors.init_app(app)

    @app.route('/ping')
    def pingpong():
        return 'pong!'

    # @app.route('/mobile/config/opmode', methods=['GET', 'POST'])
    # def mobile_config_opmode():
    #     if request.method == 'POST':
    #         data = request.get_json()
    #         APP_DATA['opmode'] = data.get('opmode')
    #     return jsonify(APP_DATA['opmode'])

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8080)
