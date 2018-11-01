import unittest
from mock import Mock, patch
from service import Service

class TestOperations(unittest.TestCase):

    @patch("test_service.Service")
    def test_bad_random(self, mock_service):
        # mock_service now becomes Service
        # when we .bad_random = 10, we set Service to call bad_random and returns a 10

        mock_service.bad_random = 10

        # assert that Service is called and returns a value
        value = Service.bad_random
        assert value == 10
        return

    @patch("test_service.Service")
    def test_divide(self, mock_service):
        mock_service.bad_random = 10
        mock_service.divide = mock_service.bad_random / 2
        assert Service.divide == 5
        return

    def test_abs_plus(self):
        negative_value = Service.abs_plus(self, -5)
        positive_value = Service.abs_plus(self, 1)
        zero = Service.abs_plus(self, 0)
        assert negative_value == 6
        assert positive_value == 2
        assert zero == 1
        return

    @patch("test_service.Service")
    def test_complicated_function(self, mock_service):
        # mock the broken random function and previous divide function
        mock_service.bad_random = 10
        mock_service.divide = mock_service.bad_random / 2

        mock_service.complicated_function = mock_service.divide, mock_service.bad_random % 2
        # mock the complicated function
        return

TestOperations()
