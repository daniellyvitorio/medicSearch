from .settings import *
DEBUG = True
#chave secreta
SECRET_KEY = 'sjndui3h98dgj'
DATABASES = {
    'default':{
        'ENGINE': 'django.db.bacends.sqlite3',
        'NAME': os.path.join(BASE DIR, 'db.sqlite3'),
    }
}

#conectar no banco mysql
# DATABASES = {
#     'default':{
#         'ENGINE':'django.db.backend.mysql',
#         'NAME': 'medicdb',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#         'PORT': '3306'
#     }
# }
ALLOWED_HOSTS = ['localhost','127.0.0.1']