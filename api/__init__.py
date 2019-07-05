import connexion
import config


def create_app():
    connexion_app = connexion.App(__name__, specification_dir=config.BASE_DIR)
    app = connexion_app.app
    app.config.from_object(config)
    connexion_app.add_api(config.SWAGGER_DIR)
    return app
