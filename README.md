# ideallical django-restframework testtools

## Requirements

* Python (3.5)

## Installation

Install using `pip`...

    pip install ii_drf_testtools

## Example

Let's take a look at a quick example of using ii_drf_testtools.

    import pytest
    from ii_drf_testtools.utils import BaseListAPITest


    @pytest.mark.django_db(transaction=True)
    class TestUserList(BaseListAPITest):
        api_url = reverse('rest_api:users:list', kwargs={'version': '1.0'})

        status_codes_anonymous = {'ALL': 403}
        status_codes_authenticated = {'ALL': 405, 'GET': 200}
        # is the same as:
        # status_codes_authenticated = {'GET': 200, 'DELETE': 405, 'POST': 405,
        #                               'PATCH': 405, 'PUT': 405}

This test will do the following 10 tests:

    - Assert an anonymous GET request on /api/1.0/users/ equals status 403
    - Assert an anonymous DELETE request on /api/1.0/users/ equals status 403
    - Assert an anonymous POST request on /api/1.0/users/ equals status 403
    - Assert an anonymous PATCH request on /api/1.0/users/ equals status 403
    - Assert an anonymous PUT request on /api/1.0/users/ equals status 403

    - Assert an authenticated GET request on /api/1.0/users/ equals status 200
    - Assert an authenticated DELETE request on /api/1.0/users/ equals status 405
    - Assert an authenticated POST request on /api/1.0/users/ equals status 405
    - Assert an authenticated PATCH request on /api/1.0/users/ equals status 405
    - Assert an authenticated PUT request on /api/1.0/users/ equals status 405
