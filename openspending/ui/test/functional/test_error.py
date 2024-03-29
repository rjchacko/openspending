from pylons import config
from openspending.ui.test import ControllerTestCase, url, helpers as h

class TestErrorController(ControllerTestCase):

    def test_403(self):
        response = self.app.get(
            url(controller='error_test', action='not_authorised'),
            status=403
        )

        assert "403 Forbidden" in response, \
            "'403 Not Found' not in response to request that should give a 403!"

        assert "OpenSpending" in response, \
            "'OpenSpending' not in 403 page! Is this not a custom 403?"

        assert "Custom 403 error message" in response, \
            "Custom error message was not passed through to 403 error page."

    def test_404(self):
        response = self.app.get(
            url(controller='error_test', action='not_found'),
            status=404
        )
        assert "404 Not Found" in response, \
            "'404 Not Found' not in response to request that should give a 404!"

        assert "OpenSpending" in response, \
            "'OpenSpending' not in 404 page! Is this not a custom 404?"

        assert "Custom 404 error message" in response, \
            "Custom error message was not passed through to 404 error page."


    def test_500(self):
        # NB: This test will fail if the tests are run in debug mode. Add the
        # following line to your test.ini under [app:main]:
        #
        #   set debug = False

        response = self.app.get(
            url(controller='error_test', action='server_error'),
            status=500
        )
        assert "Server Error" in response, \
            "'Server Error' not in response to request that should give a 500!"

        assert "OpenSpending" in response, \
            "'OpenSpending' not in 500 page! Is this not a custom 500?"

        assert "Custom 500 error message" in response, \
            "Custom error message was not passed through to 500 error page."

        assert "The Count" in response, \
            "What have you done to The Count!? Put him back this instant!"