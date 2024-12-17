# How to Start a Django Project

## Before you begin, ensure you have the following installed:

`Python (version 3.6 or above)`
`pip (Python package installer)`

## Step 1: Install Django:
`pip install django`

## Step 2: Create a New Django Project
`python -m django startproject`
  
Navigate into the project directory:
`cd myproject`
  
Step 3: Run the Development Server
`python manage.py runserver`
  
Access the application by going to: `http://127.0.0.1:8000/` You should see the Django welcome page.

Step 4: Create a Django App
In Django, a project can contain multiple apps. Here's how to create an app:
Register the app by opening settings.py in your project directory (myproject/myproject/settings.py) and adding myapp to the INSTALLED_APPS list:

INSTALLED_APPS = [
    ...
    'myapp',
]
Step 5: Create Views and Templates
You can now define views and create templates for your app.
Define a view by editing views.py in myapp:
```pyhton
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```
Map the view to a URL by creating a file named urls.py in your app directory (myapp/urls.py) and defining your URLs:

```pyhon
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```
Include the app URLs in the project by editing the main urls.py in your project directory (myproject/urls.py):

Step 6: Explore and Build

Congratulations! You have successfully created a basic Django project and app. You can now explore Django's features, such as models, templates, forms, and more.

Happy coding!
