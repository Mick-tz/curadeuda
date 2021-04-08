# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dasfda!"/&sfpijkr7&-l=f#mfdas$tjnfbjo/(asdf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sepomex',
        'USER': 'cupc4ke',
        'PASSWORD': 'qwerty7890',
        'HOST': 'localhost'
    }
}

# SMTP CONFIGURATION 
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'correo'
# EMAIL_HOST_PASSWORD = 'contraseña'