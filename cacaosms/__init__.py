# -*- coding: utf-8 -*-
__version__ = '0.1.0'
__version_info__ = tuple([int(num) if num.isdigit() else num for num in __version__.replace('-', '.', 1).split('.')])

# __init__.py
default_app_config = 'cacaosms.apps.CacaoSMSAppConfig'
