## Changing the Django PROJECT name
1. The current project name is `api`. If you would like to change that name you will need to change the directory name as well as all the references to that project throughout the files in the project. That might be worth the time.

## Users App for Authentication
The `users` app is THIS project's implementation of an extension of the User model created by Django and provides the basic functionality to authenticate users. Replace references to app names with `yourappname`.

The following would need to be added to your Django project in `myproject/settings.py` to get this to work.

Be sure to `pip install django djangorestframework djangorestframework-simplejwt django-cors-headers`

```python
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

CSRF_TRUSTED_ORIGINS = ['https://*.gitpod.io']
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://.*\.gitpod\.io$",
]
```

You will need to add urls to your app that utilize jwt for authentication.

```python
# yourproject/yourappname/urls.py
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    ...,
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
```
