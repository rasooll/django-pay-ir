from .settings import *

INSTALLED_APPS += ["pay_ir"]
ROOT_URLCONF = 'django_payir.travis_urls'
PAY_IR_CONFIG = {
    "api_key": "test"
}
