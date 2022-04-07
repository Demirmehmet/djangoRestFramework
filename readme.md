Docker'a postgresql kurulumu için;  
    
    docker run --name postgresql -e POSTGRES_USER=myusername -e POSTGRES_PASSWORD=mypassword -p 5432:5432 -v /data:/var/lib/postgresql/data -d postgres


Database'i dockerda yer alan postgresql e set etmek için;

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'myusername',
            'PASSWORD': 'mypassword',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

Rest framework için;

    pip install djangorestframework
    pip install markdown       # Markdown support for the browsable API.
    pip install django-filter  # Filtering support

Add 'rest_framework' to your INSTALLED_APPS setting.

    INSTALLED_APPS = [
        ...
        'rest_framework',
    ]

urls.py file

    urlpatterns = [
        ...
        path('api-auth/', include('rest_framework.urls'))
    ]

settings.py module

    REST_FRAMEWORK = {
        # Use Django's standard `django.contrib.auth` permissions,
        # or allow read-only access for unauthenticated users.
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        ]
    }

migration için ;
    
    python manage.py migrate
    python manage.py createsuperuser
# djangoRestFramework
