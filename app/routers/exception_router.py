# -*- coding: utf-8 -*-
from app.common.response import payload
from app.decorators.authenticate_decorator import Authorities, authorized
from flask import Blueprint
from werkzeug.exceptions import (
    BadRequest,
    Forbidden,
    InternalServerError,
    NotFound,
)

_error_handler = Blueprint("exception", __name__)


@_error_handler.app_errorhandler(BadRequest)
@authorized(Authorities.ANONYMOUS)
def _bad_request(e):
    return payload(exception=e)


@_error_handler.app_errorhandler(Forbidden)
@authorized(Authorities.ANONYMOUS)
def _forbidden(e):
    return payload(exception=e)


@_error_handler.app_errorhandler(InternalServerError)
@authorized(Authorities.ANONYMOUS)
def _internal_server_error(e):
    return payload(exception=e)


@_error_handler.app_errorhandler(NotFound)
@authorized(Authorities.ANONYMOUS)
def _not_found(e):
    return payload(exception=e)


blueprints = [_error_handler]
