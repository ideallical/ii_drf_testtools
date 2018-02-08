from ii_drf_testtools import mixins
from ii_drf_testtools.settings import testtools_settings
from rest_framework.test import APIClient

UserFactory = testtools_settings.USER_FACTORY


class GenericAPITest(object):

    # public variables
    api_url = None
    only_custom = False  # only test the custom methods (set to True to speed up testing)  # noqa
    return_format = testtools_settings.RETURN_FORMAT
    status_codes_anonymous = testtools_settings.DEFAULT_STATUS_BASE_ANONYMOUS
    status_codes_authenticated = (
        testtools_settings.DEFAULT_STATUS_BASE_AUTHENTICATED)

    # internal variables
    _anonymous_client = None
    _authenticated_client = None
    _user = None

    def get_api_url(self):
        if self.api_url is None:  # pragma: no cover
            raise NotImplemented('Please provide url')
        return self.api_url

    def get_user(self):
        """
        Returns user object
        """
        if self._user is None:
            self._user = UserFactory()
        return self._user

    def get_expected_status_code(self, status_dict, method, status_code=None):
        if status_code:
            return status_code
        try:
            return status_dict[method]
        except KeyError:
            try:
                return status_dict['ALL']
            except KeyError:
                raise NotImplementedError('Please implement status in dict {} '
                                          'using method {}'.format(
                                              status_dict, method))

    def assert_status_code(self, response, status_dict, method,
                           status_code=None):

        expected_status_code = self.get_expected_status_code(
            status_dict, method, status_code)

        assert response.status_code == expected_status_code, (
            'A {method} request on {api_url} returned {status_code} but should'
            ' be {expected_status_code}.'.format(
                method=method,
                api_url=self.get_api_url(),
                status_code=response.status_code,
                expected_status_code=expected_status_code))

    def get_anonymous_client(self):
        """
        Returns non authenticated client
        """
        if self._anonymous_client is None:  # pragma: no cover
            self._anonymous_client = APIClient()
        return self._anonymous_client

    def get_authenticated_client(self):
        """
        Returns authenticated client with a normal user
        """
        if self._authenticated_client is None:
            self._authenticated_client = APIClient()
            self._authenticated_client.force_authenticate(user=self.get_user())
        return self._authenticated_client

    def test_status_on_anonymous_get(self, status_code=None):
        """
        Test the correct response status_code for a GET request
        that is not authenticated
        """
        if not self.only_custom:
            response = self.get_anonymous_client().get(
                path=self.get_api_url(), format=self.return_format)
            self.assert_status_code(
                response, self.status_codes_anonymous, 'GET', status_code)

    def test_status_on_anonymous_delete(self, status_code=None):
        """
        Test the correct response status_code for a DELETE request
        that is not authenticated
        """
        if not self.only_custom:
            response = self.get_anonymous_client().delete(
                path=self.get_api_url(), format=self.return_format)
            self.assert_status_code(
                response, self.status_codes_anonymous, 'DELETE', status_code)

    def test_status_on_anonymous_post(self, status_code=None):
        """
        Test the correct response status_code for a POST request
        that is not authenticated
        """
        if not self.only_custom:
            response = self.get_anonymous_client().post(
                path=self.get_api_url(), format=self.return_format)
            self.assert_status_code(
                response, self.status_codes_anonymous, 'POST', status_code)

    def test_status_on_anonymous_patch(self, status_code=None):
        """
        Test the correct response status_code for a PATCH request
        that is not authenticated
        """
        if not self.only_custom:
            response = self.get_anonymous_client().patch(
                path=self.get_api_url(), format=self.return_format)
            self.assert_status_code(
                response, self.status_codes_anonymous, 'PATCH', status_code)

    def test_status_on_anonymous_put(self, status_code=None):
        """
        Test the correct response status_code for a PUT request
        that is not authenticated
        """
        if not self.only_custom:
            response = self.get_anonymous_client().put(
                path=self.get_api_url(), format=self.return_format)
            self.assert_status_code(
                response, self.status_codes_anonymous, 'PUT', status_code)

    def test_status_on_authenticated_get(self, status_code=None):
        """
        Test the correct response status_code for a GET request
        that is authenticated
        """
        if not self.only_custom:
            response = self.get_authenticated_client().get(
                path=self.get_api_url(), format=self.return_format)
            self.assert_status_code(
                response, self.status_codes_authenticated, 'GET', status_code)

    def test_status_on_authenticated_delete(self, status_code=None):
        """
        Test the correct response status_code for a DELETE request
        that is authenticated
        """
        if not self.only_custom:
            response = self.get_authenticated_client().delete(
                path=self.get_api_url(), format=self.return_format)
            self.assert_status_code(
                response, self.status_codes_authenticated, 'DELETE',
                status_code)

    def test_status_on_authenticated_post(self, status_code=None,
                                          data=None):
        """
        Test the correct response status_code for a POST request
        that is authenticated
        """
        if not self.only_custom:
            response = self.get_authenticated_client().post(
                path=self.get_api_url(), data=data, format=self.return_format)
            self.assert_status_code(
                response, self.status_codes_authenticated, 'POST', status_code)

    def test_status_on_authenticated_patch(self, status_code=None, data=None):
        """
        Test the correct response status_code for a PATCH request
        that is authenticated
        """
        if not self.only_custom:
            response = self.get_authenticated_client().patch(
                path=self.get_api_url(), data=data, format=self.return_format)
            self.assert_status_code(
                response, self.status_codes_authenticated, 'PATCH',
                status_code)

    def test_status_on_authenticated_put(self, status_code=None, data=None):
        """Test the correct response status_code for a PUT request
           that is authenticated.
        """
        if not self.only_custom:
            response = self.get_authenticated_client().put(
                path=self.get_api_url(), data=data, format=self.return_format)
            self.assert_status_code(
                response, self.status_codes_authenticated, 'PUT', status_code)


class ListAPITest(mixins.ListModelMixin, GenericAPITest):
    status_codes_anonymous = testtools_settings.DEFAULT_STATUS_LIST_ANONYMOUS
    status_codes_authenticated = (
        testtools_settings.DEFAULT_STATUS_LIST_AUTHENTICATED)


class CreateAPITest(GenericAPITest):
    status_codes_anonymous = testtools_settings.DEFAULT_STATUS_CREATE_ANONYMOUS
    status_codes_authenticated = (
        testtools_settings.DEFAULT_STATUS_CREATE_AUTHENTICATED)
