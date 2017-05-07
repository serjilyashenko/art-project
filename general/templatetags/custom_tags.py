# ~*~ coding: utf-8 ~*~
from __future__ import unicode_literals

import os
from django.contrib.humanize.templatetags.humanize import intcomma
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
    contents = 'static \'' + 'build/' + file_name + '\''
    new_token = Token(token_type=token.token_type, contents=contents)

    return StaticFilesNode.handle_token(parser, new_token)


@register.filter
def p(value, arg):
    args_array = arg.split(',')
    base = '' if len(args_array) == 3 else args_array.pop(0)
    number = abs(int(value))
    a = number % 10
    b = number % 100
    try:
        if (a == 1) and (b != 11):
            return base + args_array[0]
        elif 2 <= a <= 4 and (b < 10 or b >= 20):
            return base + args_array[1]
        else:
            return base + args_array[2]
    except:
        return base


@register.filter
def wp(value, args_string):
    string = intcomma(value) if value else 'нет'
    return string + ' ' + p(value, args_string)
