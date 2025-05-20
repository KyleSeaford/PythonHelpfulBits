# Expanding Your Django Project with Multiple Templates

## Template Organization Best Practice:

Inside templates (e.g., myproject/templates/)
```
myproject/
├── templates/
│     ├── base.html
│     ├── index.html
│     ├── about.html
│     └── contact.html
```

## Step 1: Create a Base Template (base.html)
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="{% url 'home' %}">Home</a>
        <a href="{% url 'about' %}">About</a>
        <a href="{% url 'contact' %}">Contact</a>
    </nav>
    
    {% block content %}
    <!-- Content will be injected here -->
    {% endblock %}
</body>
</html>
```

## Step 2: Create Additional Templates
about.html:
```html
{% extends "myproject/base.html" %}

{% block title %}About Us{% endblock %}

{% block content %}
  <h1>About Our Company</h1>
  <p>Learn more about what we do.</p>
{% endblock %}
```
contact.html:
```html
{% extends "myproject/base.html" %}

{% block title %}Contact Us{% endblock %}

{% block content %}
<h1>Get in Touch</h1>
  <form>
      <!-- Contact form elements -->
  </form>
{% endblock %}
```
  
Navigate into the project directory:
`cd myproject`
  
## Step 3: Update Views (views.py):
```python
from django.shortcuts import render

def home(request):
    return render(request, 'myproject/index.html')

def about(request):
    return render(request, 'myproject/about.html')

def contact(request):
    return render(request, 'myproject/contact.html')
```

## Step 4: Configure URLs (urls.py):
```python
# myproject/urls.py
from django.urls import path
from .views import home, about, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
```

## Step 5: Update Existing Templates:
```html
{% extends "myproject/base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
  <h1>Welcome to Our Site</h1>
  <p>This is the homepage content.</p>
{% endblock %}
```

## Step 6: Key Concepts to Remember:
### Template Inheritance:
Use {% extends %} to inherit from base templates
Define replaceable blocks with {% block block_name %}

### URL Naming:
Use name= in URL patterns for easy reference
Reverse URLs with {% url 'name' %} in templates

### View-Template Connection:
Each view function maps to a template
Use render() to combine templates with context (data)

### Project Structure:
Keep app-specific templates in app's templates directory
Use subdirectories matching app names for better organization

## Testing Your Pages
Access your new pages at:

- Home: `http://127.0.0.1:8000/`
- About: `http://127.0.0.1:8000/about/`
- Contact: `http://127.0.0.1:8000/contact/`
