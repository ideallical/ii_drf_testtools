# ideallical django-restframework testtools

## Requirements

* Python (3.5)

## Installation

Install using `pip`...

    pip install ii_drf_testtools

## Example

Let's take a look at a quick example of using ii_drf_testtools.

```python
import pytest

from ii_drf_testtools.utils import ListAPITest
from news.tests.factories import NewsItemFactory


@pytest.mark.django_db(transaction=True)
class TestNewsList(ListAPITest):
    api_url = reverse('rest_api:news:list', kwargs={'version': '1.0'})
    only_custom = False
    status_codes_anonymous = {'ALL': 403}
    status_codes_authenticated = {'ALL': 405, 'GET': 200}

    def setup_list_data(self):
        current_user = self.get_user()

        self.active_newsitem = NewsItemFactory(
            name='Active newsitem', is_active=True, user=current_user)
        self.active_newsitem2 = NewsItemFactory(
            name='Active newsitem2', is_active=True, user=current_user)
        self.inactive_newsitem = NewsItemFactory(
            name='Inactive newsitem', is_active=False, user=current_user)
        self.other_newsteam = NewsItemFactory(
            name='Other newsitem', is_active=True)

    def assert_list_response_authenticated(self, response):
        assert response.json() == [
            {
                'id': self.active_newsitem.id,
                'name': 'Active newsitem',
            },
            {
                'id': self.active_newsitem2.id,
                'name': 'Active newsitem2',
            }]
```

This test will do the following 10 tests:

    - Assert an anonymous GET request on /api/1.0/news/ equals status 403
    - Assert an anonymous DELETE request on /api/1.0/news/ equals status 403
    - Assert an anonymous POST request on /api/1.0/news/ equals status 403
    - Assert an anonymous PATCH request on /api/1.0/news/ equals status 403
    - Assert an anonymous PUT request on /api/1.0/news/ equals status 403

    - Assert an authenticated GET request on /api/1.0/news/ equals status 200
    - Assert an authenticated DELETE request on /api/1.0/news/ equals status 405
    - Assert an authenticated POST request on /api/1.0/news/ equals status 405
    - Assert an authenticated PATCH request on /api/1.0/news/ equals status 405
    - Assert an authenticated PUT request on /api/1.0/news/ equals status 405

Plus one additional test, namely:

    To test that a GET request on /api/1.0/news/ only shows active NewsItems
    that are created by the current loggedin user.
