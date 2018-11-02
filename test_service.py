import unittest
from mock import Mock, patch
from service import Service

class TestOperations(unittest.TestCase):

    # path the Service class of the test_service
    @patch("test_service.Service.bad_random")
    def test_bad_random(self, mock_service):
        mock_service.return_value = 10
        assert Service.bad_random() == 10
        mock_service.return_value = 99
        assert Service.bad_random() == 99
        mock_service.return_value = 0
        assert Service.bad_random() == 0
        return

    @patch("test_service.Service.bad_random")
    def test_divide(self, mock_service):
        mock_service.return_value = 12
        # call the divide fun, iton in service
        assert Service().divide(2) == 6
        assert Service().divide(4) == 3
        assert Service().divide(-2) == -6
        assert Service().divide(12) == 1
        return

    def test_abs_plus(self):
        assert Service.abs_plus(self, -5) == 6

        assert Service.abs_plus(self, 1) == 2
        assert Service.abs_plus(self, 0) == 1
        return

    @patch("test_service.Service")
    def test_complicated_function(self, mock_service):
        # mock the broken random function and previous divide function
        y = 2
        mock_service.bad_random.return_value = 10
        mock_service.divide.return_value = mock_service.bad_random() / y
        mock_service.complicated_function.return_value = Service.divide(y), Service.bad_random() % 2
        values = Service.complicated_function(2)
        assert values[0] == 5.0
        assert values[1] == 0

        y = -2
        mock_service.divide.return_value = mock_service.bad_random() / y
        mock_service.complicated_function.return_value = Service.divide(y), Service.bad_random() % 2
        print(Service.complicated_function(2))
        assert Service.complicated_function(2)[0] == -5.0
        assert Service.complicated_function(2)[1] == 0
        return

TestOperations()
