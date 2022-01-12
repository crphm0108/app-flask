# -*- coding: utf-8 -*-
from app.common.response import payload
from app.decorators.authenticate_decorator import Authorities, authorized
from flask import Blueprint

_developer = Blueprint("developer", __name__, url_prefix="/developer")


@_developer.route("/", methods=["GET"])
@authorized(Authorities.DEVELOPER)
def _get():
    return payload({"msg": "success"})


blueprints = [_developer]
