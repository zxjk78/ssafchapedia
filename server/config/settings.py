"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=+qp#2311g(1k268ob_mzh9vz9fdtacd613s1ol5qkm!=*4a^n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []




# Application definition

INSTALLED_APPS = [
    # Custom Apps
    'articles',
    'accounts',
    'reviews',
    'movies',
    'people',

    # Third-party packages
    'django_seed',
    'corsheaders',

    'rest_framework',
    'rest_framework.authtoken',

    'dj_rest_auth',
    'dj_rest_auth.registration',

    # allauth
    'allauth', 
    'allauth.account',
    'allauth.socialaccount',
    # allauth Oauth2.0 service providers
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.kakao',
    
    # Django cores
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # cors headers
    "corsheaders.middleware.CorsMiddleware",

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'accounts.User'

# CORS WHITELIST
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8080', # 로컬 vue 서버
    'http://localhost:8080', # 로컬 vue 서버
    
    #'https://jaehozzang.com', # 프로덕션 vue 서버
]

# Allauth 설정 (registration)
ACCOUNT_EMAIL_VERIFICATION = None

SITE_ID = 1
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

SOCIALACCOUNT_LOGIN_ON_GET = True
# ACCOUNT_LOGOUT_ON_GET = True
# ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'

AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
]
SITE_ID = 1
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# 이렇게 됨으로써 api로 통신만 한다는 서버의 역할에서 좀 어긋나게 됨 
LOGIN_REDIRECT_URL = 'http://localhost:8080/' # 로그인 후 리디렉션할 페이지

# ACCOUNT_LOGOUT_REDIRECT_URL = "index"  # 로그아웃 후 리디렉션 할 페이지
# ACCOUNT_LOGOUT_ON_GET = True # 로그아웃 버튼 클릭 시 자동 로그아웃
