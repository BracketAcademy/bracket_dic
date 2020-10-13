DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_mydic',
        'USER': 'backend',
        'PASSWORD': '27013004',
        'HOST': '',
        'PORT': '',
        'OPIONS': {
            'init_command': "SET sql_mode = 'STRICT_TRANS_TABLES'",
        }
    }
}