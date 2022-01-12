# -*- coding: utf-8 -*-
from enum import Enum, auto
from typing import Any

from werkzeug.exceptions import Forbidden, InternalServerError


class Authorities(Enum):
    ANONYMOUS = auto()
    ADMIN = auto()
    USER = auto()
    DEVELOPER = auto()


def authorized(authority: Authorities) -> Any:
    def _f(f):
        def _w(*args, **kwargs):
            _authority = AuthorizedFactory.getInstance(authority)
            if not _authority.authorized():
                raise Forbidden
            return f(*args, **kwargs)

        return _w

    return _f


class AuthorizedFactory:
    class Base:
        @classmethod
        def authorized(self, *args):
            return self(*args)

    class Anonymous(Base):
        def authorized(self):
            return True

    class Admin(Base):
        def authorized(self):
            # TODO: 認証処理を追記
            return False

    class User(Base):
        def authorized(self):
            # TODO: 認証処理を追記
            return False

    class Developer(Base):
        def authorized(self):
            # TODO: 認証処理を追記
            return False

    @staticmethod
    def getInstance(
        authority: Authorities,
    ):
        if Authorities.ANONYMOUS is authority:
            return AuthorizedFactory.Anonymous()
        elif Authorities.ADMIN is authority:
            return AuthorizedFactory.Admin()
        elif Authorities.USER is authority:
            return AuthorizedFactory.User()
        elif Authorities.DEVELOPER is authority:
            return AuthorizedFactory.Developer()
        else:
            raise InternalServerError
