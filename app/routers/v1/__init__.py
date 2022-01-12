# -*- coding: utf-8 -*-]
from app.common.blueprints import register_blueprints
from app.routers.v1 import admin_router, developer_router, user_router
from flask import Blueprint

_v1 = Blueprint("v1", __name__, url_prefix="/v1")

register_blueprints(_v1, admin_router.blueprints)
register_blueprints(_v1, developer_router.blueprints)
register_blueprints(_v1, user_router.blueprints)

blueprints = [_v1]
