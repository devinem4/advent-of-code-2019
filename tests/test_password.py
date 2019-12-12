import pytest

from password.password import Password


class TestValidator:
    def test_password_validator_1(self):
        assert Password.validator_1("111111")
        assert not Password.validator_1("223450")
        assert not Password.validator_1("123789")
