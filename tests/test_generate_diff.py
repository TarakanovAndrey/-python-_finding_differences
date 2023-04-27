import pytest
from fixtures.flat_resalt import data
from gendiff import generate_diff


result = generate_diff('fixtures/file1.json', 'fixtures/file2.json')


def test_flat_generate_diff(data):
    assert result == data


def test_type_result():
    assert isinstance(result, str)
