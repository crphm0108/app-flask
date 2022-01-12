# -*- coding: utf-8 -*-
from typing import List, Union

from flask import Blueprint, Flask


def register_blueprints(
    app: Union[Flask, Blueprint], blueprints: List[Blueprint] = []
) -> bool:
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    return bool(blueprints)
