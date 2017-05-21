# ~*~ coding: utf-8 ~*~
import sys

IS_LOCAL = sys.platform.startswith('win') or sys.platform.startswith('darwin')

HOST = 'art24.my:8000' if IS_LOCAL else 'art24.info'
