## Users App for Authentication
The `users` app is THIS project's implementation of an extension of the User model created by Django and provides the basic functionality to authenticate users. Replace references to app names with `yourappname`.

The following would need to be added to your Django project in `myproject/settings.py` to get this to work.

# Step 1: Install Necessary Dependencies - you may already have some installed
`$ pip install django djangorestframework djangorestframework-simplejwt django-cors-headers django-environ google-cloud-secret-manager`  
`$ pip freeze > path/to/requirements.txt`

# NOTE: Please start your django project with this command to make the project structure the way we will need it to deploy.
`$ django-admin startproject api .`

# Step 2: Use the gist below to create, add, and update all necessary files in the Django project.

https://gist.github.com/JMStewart00/7f890693c48b15417457429d50a689f0

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
