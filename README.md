## Users App for Authentication
The `users` app is THIS project's implementation of an extension of the User model created by Django and provides the basic functionality to authenticate users. Replace references to app names with `yourappname`.

The following would need to be added to your Django project in `myproject/settings.py` to get this to work.

## Step 1: Install Necessary Dependencies - you may already have some installed
`$ pip install django djangorestframework djangorestframework-simplejwt django-cors-headers`
`$ pip freeze > path/to/requirements.txt`

## Step 2: Add to settings.py
```python
from datetime import timedelta

INSTALLED_APPS = [
    ... 

    # 3rd Party Apps
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    # Local Apps
    'users', # your app name, probably not users
]

# It is important to understand that this will make all of your routes need auth creds.
# You can use AllowAny, IsAuthenticatedOrReadOnly if you want as well.
# Permissions can be overwritten on a view-by-view basis this is just the default
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

# Custom user model for your application
AUTH_USER_MODEL = "myappname.CustomUser"

CSRF_TRUSTED_ORIGINS = ['https://*.gitpod.io']
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://.*\.gitpod\.io$",
]
```

# Step 3: Add urls for authentication endpoints.
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

# Step 4: Apply newly installed apps migrations for authtoken
`python manage.py migrate`
