## Users App for Authentication
The `users` app is THIS project's implementation of an extension of the User model created by Django and provides the basic functionality to authenticate users. Replace references to app names with `yourappname`.

The following would need to be added to your Django project in `myproject/settings.py` to get this to work.

# Step 1: Install Necessary Dependencies - you may already have some installed
`$ pip install django djangorestframework djangorestframework-simplejwt django-cors-headers django-environ google-cloud-secret-manager`  
`$ pip freeze > path/to/requirements.txt`

### NOTE: Please start your django project with this command to make the project structure the way we will need it to deploy.
`$ django-admin startproject api .`
### NOTE 2: DON'T MIGRATE ANYTHING BEFORE GETTING TO AT LEAST STEP 7!

# Step 2: Use the gist below to create, add, and update all necessary files in the Django project. Most should tell you where to put each file.
https://gist.github.com/JMStewart00/7f890693c48b15417457429d50a689f0  

# Step 3: Install your APP
`$ python manage.py startapp appnamegoeshere`

# Step 4: Add app to INSTALLED_APPS in settings.py  
# Step 5: Watch [this video](https://youtu.be/SYn1Cq5LJcM) and create a custom user and hook that up BEFORE DOING ANYTHING ELSE. 

# Step 6: Add urls for authentication endpoints.
You will need to add urls to your app that utilize jwt for authentication.

```python
# yourappname/urls.py
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    ...,
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
```

# Step 7: Apply newly installed apps migrations for authtoken
`python manage.py migrate`
