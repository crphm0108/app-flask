# -*- coding: utf-8 -*-
from app.common.response import payload
from app.decorators.authenticate_decorator import Authorities, authorized
from flask import Blueprint

_admin = Blueprint("admin", __name__, url_prefix="/admin")


@_admin.route("/", methods=["GET"])
@authorized(Authorities.ADMIN)
def _get():
    return payload({"msg": "success"})


blueprints = [_admin]
