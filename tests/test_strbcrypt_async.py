import pytest

from strbcrypt.anyio import AsyncStrBcrypt


@pytest.fixture
def asb() -> AsyncStrBcrypt:
    return AsyncStrBcrypt()


@pytest.mark.anyio
async def test_hash_generation(
    pass_and_salt: tuple[str, bytes, str], asb: AsyncStrBcrypt
) -> None:
    password, salt, _hash = pass_and_salt
    assert _hash == await asb.hashpw(password, salt)


@pytest.mark.anyio
async def test_password_check(pass_and_salt, asb: AsyncStrBcrypt) -> None:
    assert await asb.checkpw(pass_and_salt[0], pass_and_salt[2])
