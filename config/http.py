from flask import Flask
from flask_cors import CORS
from flask_compress import Compress

import routes
cors = CORS()
compress = Compress()

def create_app(configuration):
    app = Flask(
        __name__.split(',')[0])
    
    app.register_blueprint(routes.UserRoutes.user_route)
    # load configuration
    app.config.from_object(configuration)

    # init app
    cors.init_app(app, resources={r"/*": {"origins": "*"}})
    return app