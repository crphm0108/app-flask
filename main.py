# -*- coding: utf-8 -*-
from os import getenv

from flask import Flask

from app.common.blueprints import register_blueprints
from app.common.logger import getLogger
from app.routers import exception_router, root_router, v1, v2

log = getLogger(__name__)

app_name = getenv("APP_NAME", __name__)
log.info("START ${app_name}")

app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False

register_blueprints(app, exception_router.blueprints)
register_blueprints(app, root_router.blueprints)
register_blueprints(app, v1.blueprints)
register_blueprints(app, v2.blueprints)

if __name__ == "__main__":
    app.run()
