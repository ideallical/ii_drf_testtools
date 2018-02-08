class ListModelMixin(object):

    def setup_list_data(self):
        raise NotImplementedError('Please implement setup_list_data')

    def assert_list_response_anonymous(self):
        raise NotImplementedError(
            'Please implement assert_list_response_anonymous')

    def assert_list_response_authenticated(self):
        raise NotImplementedError(
            'Please implement assert_list_response_authenticated')

    def test_data_on_anonymous_get(self):
        if not self.only_custom:
            expected_status_code = self.get_expected_status_code(
                self.status_codes_anonymous, 'GET')

            if expected_status_code == 200:
                self.setup_list_data()
                response = self.get_anonymous_client().get(
                    path=self.get_api_url(), format=self.return_format)
                self.assert_list_response_anonymous(response)

    def test_data_on_authenticated_get(self):
        if not self.only_custom:
            expected_status_code = self.get_expected_status_code(
                self.status_codes_authenticated, 'GET')

            if expected_status_code == 200:
                self.setup_list_data()
                response = self.get_authenticated_client().get(
                    path=self.get_api_url(), format=self.return_format)
                self.assert_list_response_authenticated(response)
