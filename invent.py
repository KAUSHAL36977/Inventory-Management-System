# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',  # Default JSON responses
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
}

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'inventory',
        'ENFORCE_SCHEMA': True,
        'CLIENT': {
            'host': 'your_mongo_host',  # Add your MongoDB connection URL
            'username': 'your_username',
            'password': 'your_password',
            'authSource': 'admin',
        }
    }
}
