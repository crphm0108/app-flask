# -*- coding: utf-8 -*-]
from app.common.blueprints import register_blueprints
from app.routers.v2 import admin_router, developer_router, user_router
from flask import Blueprint

_v2 = Blueprint("v2", __name__, url_prefix="/v2")

register_blueprints(_v2, admin_router.blueprints)
register_blueprints(_v2, developer_router.blueprints)
register_blueprints(_v2, user_router.blueprints)

blueprints = [_v2]
