import os 
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRESQL = {
    'default' : {
        'ENGINE' :
        'django.db.backends.postgresql_psycopg2',
        'NAME':'SaleCold',
        'USER':'postgres',
        'PASSWORD':'password',
        'HOST':'localhost',
        'PORT':'5432'
    }
}