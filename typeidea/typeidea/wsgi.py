"""
WSGI config for typeidea project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

profile = os.environ.get('TYPEIDEA_PROFILE', 'develop')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typeidea.settings.%s' % profile)
'''
setdefault(key, default)方法检查字典中是否存在键key。如果不存在，则将key设置为default指定的值，并返回该值。如果键已存在，则返回key这个键对应的值（键值对）。
'typeidea.settings.%s' % profile是一个字符串格式化表达式，它将profile变量的值插入到字符串中，替换掉%s占位符。
'''


application = get_wsgi_application()
