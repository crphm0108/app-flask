# -*- coding: utf-8 -*-
from typing import Tuple

from flask import Response, jsonify
from werkzeug.exceptions import HTTPException


def payload(
    result: dict = None,
    code: int = 200,
    exception: HTTPException = None,
) -> Tuple[Response, int]:
    Exception
    params: dict = {"code": code}
    if result is not None:
        params = {**params, **result}
    if exception is not None:
        params["code"] = exception.code
        e = {"e": {"code": exception.code, "msg": exception.description}}
        params = {**params, **e}
    return jsonify(params), params["code"]
