from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("message", 2) == "egass_em"
    assert encrypt_message("message", 3) == "sem_egas"
    assert encrypt_message("message", -1) == "egassem"

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 2)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", 'message')
