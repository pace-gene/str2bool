import pytest

from str2bool import str2bool, str2bool_exc


class TestStr2Bool:
    @pytest.mark.parametrize(
        "value,expected",
        [
            ("yes", True),
            ("true", True),
            ("t", True),
            ("y", True),
            ("1", True),
            ("YES", True),
            ("True", True),
            ("T", True),
            ("Y", True),
            ("no", False),
            ("false", False),
            ("f", False),
            ("n", False),
            ("0", False),
            ("NO", False),
            ("False", False),
            ("F", False),
            ("N", False),
        ],
    )
    def test_valid_inputs(self, value, expected):
        """Test str2bool with valid inputs."""
        assert str2bool(value) == expected

    @pytest.mark.parametrize(
        "value",
        [
            "invalid",
            "maybe",
            "2",
            "",
            None,
            123,  # Non-string input
            True,  # Boolean input
        ],
    )
    def test_invalid_inputs_no_exception(self, value):
        """Test str2bool with invalid inputs (no exception)."""
        assert str2bool(value) is None

    @pytest.mark.parametrize(
        "value",
        [
            "invalid",
            "maybe",
            "2",
            "",
            None,
            123,  # Non-string input
            True,  # Boolean input
        ],
    )
    def test_invalid_inputs_with_exception(self, value):
        """Test str2bool with invalid inputs (with exception)."""
        with pytest.raises(ValueError):
            str2bool(value, raise_exc=True)


class TestStr2BoolExc:
    @pytest.mark.parametrize(
        "value,expected",
        [
            ("yes", True),
            ("true", True),
            ("t", True),
            ("y", True),
            ("1", True),
            ("YES", True),
            ("True", True),
            ("T", True),
            ("Y", True),
            ("no", False),
            ("false", False),
            ("f", False),
            ("n", False),
            ("0", False),
            ("NO", False),
            ("False", False),
            ("F", False),
            ("N", False),
        ],
    )
    def test_valid_inputs(self, value, expected):
        """Test str2bool_exc with valid inputs."""
        assert str2bool_exc(value) == expected

    @pytest.mark.parametrize(
        "value",
        [
            "invalid",
            "maybe",
            "2",
            "",
            None,
            123,  # Non-string input
            True,  # Boolean input
        ],
    )
    def test_invalid_inputs(self, value):
        """Test str2bool_exc with invalid inputs."""
        with pytest.raises(ValueError):
            str2bool_exc(value)

    def test_return_type(self):
        """Test that str2bool_exc returns a bool type."""
        result = str2bool_exc("yes")
        assert isinstance(result, bool)
