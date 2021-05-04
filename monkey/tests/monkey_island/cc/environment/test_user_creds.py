import bcrypt

from monkey_island.cc.environment.user_creds import UserCreds

TEST_USER = "Test"
TEST_HASH = "abc1231234"
TEST_SALT = b"$2b$12$JA7GdT1iyfIsquF2cTZv2."


def test_bool_true():
    assert UserCreds(TEST_USER, TEST_HASH)


def test_bool_false_empty_password_hash():
    assert not UserCreds(TEST_USER, "")


def test_bool_false_empty_user():
    assert not UserCreds("", TEST_HASH)


def test_bool_false_empty_user_and_password_hash():
    assert not UserCreds("", "")


def test_to_dict_empty_creds():
    user_creds = UserCreds("", "")
    assert user_creds.to_dict() == {}


def test_to_dict_full_creds():
    user_creds = UserCreds(username=TEST_USER, password_hash=TEST_HASH)
    assert user_creds.to_dict() == {"user": TEST_USER, "password_hash": TEST_HASH}


def test_to_auth_user_full_credentials():
    user_creds = UserCreds(username=TEST_USER, password_hash=TEST_HASH)
    auth_user = user_creds.to_auth_user()
    assert auth_user.id == 1
    assert auth_user.username == TEST_USER
    assert auth_user.secret == TEST_HASH


def test_get_from_cleartext(monkeypatch):
    monkeypatch.setattr(bcrypt, "gensalt", lambda: TEST_SALT)

    creds = UserCreds.from_cleartext(TEST_USER, "Test_Password")
    assert creds.password_hash == "$2b$12$JA7GdT1iyfIsquF2cTZv2.NdGFuYbX1WGfQAOyHlpEsgDTNGZ0TXG"


def test_member_values(monkeypatch):
    monkeypatch.setattr(bcrypt, "gensalt", lambda: TEST_SALT)

    creds = UserCreds(TEST_USER, TEST_HASH)
    assert creds.username == TEST_USER
    assert creds.password_hash == TEST_HASH
