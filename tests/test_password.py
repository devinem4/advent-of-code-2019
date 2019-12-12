import pytest

from password.password import Password


class TestValidator:
    def test_password_validator_1(self):
        assert Password.validator_1("111111")
        assert not Password.validator_1("223450")
        assert not Password.validator_1("123789")

    def test_password_validator_2(self):
        assert Password.validator_2("112233")
        assert not Password.validator_2("123444")
        assert Password.validator_2("111122")
