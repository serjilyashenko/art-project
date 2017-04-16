from __future__ import unicode_literals

import os
from django.contrib.staticfiles.templatetags.staticfiles import StaticFilesNode
from django.template.base import Token
from django import template

from settings import HOME

register = template.Library()


@register.tag('static_build')
def do_static_build(parser, token):

    file_name = token.split_contents()[1][1:-1]
    with open(os.path.join(HOME, 'assets.json')) as data_file:
        import json as json_lib
        file_name = json_lib.load(data_file)[file_name]
    contents = "static \"" + "build/" + file_name + "\""
    new_token = Token(token_type=token.token_type, contents=contents)

    return StaticFilesNode.handle_token(parser, new_token)
