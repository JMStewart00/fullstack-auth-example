# A Python Django Example

This repo is intended for use with [Gitpod](httpsL//gitpod.io).

## Basics
When opening a new gitpod with this repo the initial setup should mostly be taken care of for you to get moving with a Django app immediately.

Processes that should run:
1. Automatically get a docker container that creates a PostgresQL database (port 5432) and starts pgAdmin (database tool) on the port 7000. (Credentials for the database can be found in the pgadmin.json file.)
1. After port 7000 starts up, pip should be upgraded and all requirements in the requirements.txt should be installed, including `psycopg2` and `Django` among other packages.

## Changing the Django PROJECT name
1. The current project name is `api`. If you would like to change that name you will need to change the directory name as well as all the references to that project throughout the files in the project. That might be worth the time.

## Django Admin
The CSRF_TRUSTED_ORIGINS setting in settings.py should be set to allow `https://*.gitpod.io` for a trusted CSRF token.

## Users App for Authentication
The `users` app is an extension of the User model created by Django and provides the basic functionality to authenticate users. 

The following would need to be added to your Django project in `myproject/settings.py` to get this to work.

Be sure to `pip install django djangorestframework djangorestframework-simplejwt django-cors-headers`

Part 1 of [this hackernoon](https://hackernoon.com/110percent-complete-jwt-authentication-with-django-and-react-2020-iejq34ta) article was the basis for this.

```python
CSRF_TRUSTED_ORIGINS = ['https://*.gitpod.io']
CORS_ALLOW_ALL_ORIGINS = True # insecure but necessary for now.
INSTALLED_APPS = [
    ... 

    # 3rd Party Apps
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.sites',
    'corsheaders',

    # Local Apps
    'users', # your app name
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ), 
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

# Custom user model
AUTH_USER_MODEL = "users.CustomUser"


CORS_ALLOWED_ORIGINS = [    
    'http://localhost:8000',
    'https://*.gitpod.io'
]
```

### Deploying to Heroku steps
- `curl https://cli-assets.heroku.com/install.sh | sh`
- `heroku login --interactive`
- `heroku create`
- `pip install django-heroku django-environ`
- `echo 'SECRET_KEY=your-secret-key' > .env`
- Update settings file
- `heroku config:set SECRET_KEY=your-secret-key`
- `pip freeze > requirements.txt`
- `echo python-3.8.12 > runtime.txt`
- `echo "web: python manage.py runserver 0.0.0.0:\$PORT" > Procfile`
- `git push heroku main`


```python
import environ
import os

env = environ.Env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')


DATABASES = {
  "default": env.db("DATABASE_URL", default='postgres://postgres:postgres@127.0.0.1:5432/postgres')
}
```

- `heroku run python manage.py migrate`
https://realpython.com/django-hosting-on-heroku/#populate-the-database