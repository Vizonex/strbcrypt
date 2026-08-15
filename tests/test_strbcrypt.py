import pytest

from strbcrypt import StrBcrypt


@pytest.fixture
def sb() -> StrBcrypt:
    return StrBcrypt()


def test_hash_generation(pass_and_salt: tuple[str, bytes, str], sb: StrBcrypt) -> None:
    password, salt, _hash = pass_and_salt
    assert _hash == sb.hashpw(password, salt)


def test_password_check(pass_and_salt, sb: StrBcrypt) -> None:
    assert sb.checkpw(pass_and_salt[0], pass_and_salt[2])
