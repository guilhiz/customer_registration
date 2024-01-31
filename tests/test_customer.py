# pylint: disable=E0401
import pytest
from fastapi import HTTPException
from src.utils.cpf_validator import validate_cpf
def test_validate_cpf_valid():
    assert validate_cpf('123.456.789-09') == '12345678909'

def test_validate_cpf_invalid_characters():
    with pytest.raises(HTTPException) as exc_info:
        validate_cpf('abc.def.ghi-jkl')
    assert exc_info.value.status_code == 400
def test_validate_cpf_invalid_length():
    with pytest.raises(HTTPException) as exc_info:
        validate_cpf('123.456.789-0123')
    assert exc_info.value.status_code == 400
def test_validate_cpf_invalid_digits():
    with pytest.raises(HTTPException) as exc_info:
        validate_cpf('123.456.789-00')
    assert exc_info.value.status_code == 422
