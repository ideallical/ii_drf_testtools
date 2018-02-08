"""
Settings for ideallical drf testtools are all namespaced in the
II_DRF_TESTTOOLS setting.
For example your project's `settings.py` file might look like this:

II_DRF_TESTTOOLS = {
    'RETURN_FORMAT': 'json',
    'USER_FACTORY': 'account.tests.factories.UserFactory',
    # base
    'DEFAULT_STATUS_BASE_ANONYMOUS': {'ALL': 403, },
    'DEFAULT_STATUS_BASE_AUTHENTICATED': {'ALL': 405, },
    # list
    'DEFAULT_STATUS_LIST_ANONYMOUS': {'ALL': 403, },
    'DEFAULT_STATUS_LIST_AUTHENTICATED': {'ALL': 405, 'GET': 200},
    # create
    'DEFAULT_STATUS_CREATE_ANONYMOUS': {'ALL': 403, },
    'DEFAULT_STATUS_CREATE_AUTHENTICATED': {'ALL': 405, 'POST': 400},
}


This module provides the `testtool_setting` object, that is used to access
ideallical DRF testtools settings, checking for user settings first, then
falling back to the defaults.
"""
from ii_django_package_settings.settings import PackageSettings


class TestToolsSettings(PackageSettings):
    NAME = 'II_DRF_TESTTOOLS'
    DOC = 'https://github.com/ideallical/ii_drf_testtools/'
    DEFAULTS = {
        'RETURN_FORMAT': 'json',
        'USER_FACTORY': 'accounts.tests.factories.UserFactory',
        # base
        'DEFAULT_STATUS_BASE_ANONYMOUS': {'ALL': 403, },
        'DEFAULT_STATUS_BASE_AUTHENTICATED': {'ALL': 405, },
        # list
        'DEFAULT_STATUS_LIST_ANONYMOUS': {'ALL': 403, },
        'DEFAULT_STATUS_LIST_AUTHENTICATED': {'ALL': 405, 'GET': 200},
        # create
        'DEFAULT_STATUS_CREATE_ANONYMOUS': {'ALL': 403, },
        'DEFAULT_STATUS_CREATE_AUTHENTICATED': {'ALL': 405, 'POST': 400},
    }
    IMPORT_STRINGS = ('USER_FACTORY', )


testtools_settings = TestToolsSettings(None)
