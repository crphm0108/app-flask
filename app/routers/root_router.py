# -*- coding: utf-8 -*-
from app.common.response import payload
from app.decorators.authenticate_decorator import Authorities, authorized
from flask import Blueprint

_health_check = Blueprint("root", __name__, url_prefix="/")


@_health_check.route("/", methods=["GET"])
@authorized(Authorities.ANONYMOUS)
def _get():
    return payload({"msg": "success"})


blueprints = [_health_check]
