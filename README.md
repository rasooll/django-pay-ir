# Django payment module for Pay.ir

![PyPI](https://img.shields.io/pypi/v/django-payment-payir.svg) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-payment-payir.svg) ![PyPI - Django Version](https://img.shields.io/pypi/djversions/django-payment-payir.svg)

## Installation

First install package.

```bash
pip install django-payment-payir
```

Add 'pay_ir' to your INSTALLED_APPS setting.

```python
INSTALLED_APPS = (
    ...
    'pay_ir',
)
```

And add `PAY_IR_CONFIG` in to setting file.

```python
PAY_IR_CONFIG = {
    "api_key": "YOUR_API_KEY"
}
```

For test without api key enter a `test` as api key.

Add the following to your root `urls.py` file.

```python
urlpatterns = [
    ...
    url(r'^payment/', include('pay_ir.urls'))
]
```

Note that the URL path can be whatever you want.

Run `python manage.py migrate` to create the payments models.

### Tested on

- Python (3.6.6)
- Django (2.1)
- requests (2.19.1)