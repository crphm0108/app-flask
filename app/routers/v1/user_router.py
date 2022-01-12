# -*- coding: utf-8 -*-
from app.common.response import payload
from app.decorators.authenticate_decorator import Authorities, authorized
from flask import Blueprint

_user = Blueprint("user", __name__, url_prefix="/user")


@_user.route("/", methods=["GET"])
@authorized(Authorities.ANONYMOUS)
def _get():
    return payload({"msg": "success"})


blueprints = [_user]
