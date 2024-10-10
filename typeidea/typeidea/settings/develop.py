from .base import *  # NOQA


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
ALLOWED_HOSTS = []

"""
    生产环境中，我们应该根据自己的网站域名来设置ALLOWED_HOSTS，而不是ALLOWED_HOSTS = []（DEBUG=TRUE时只能访问127.0.0.1：8000）（DEBUG=FALSE时什么都不能访问）。
    例如，如果我们的网站域名是example.com和www.example.com，那么我们应该在settings.py(develop.py)文件中这样设置：
ALLOWED_HOSTS = ['example.com', 'www.example.com']
"""
