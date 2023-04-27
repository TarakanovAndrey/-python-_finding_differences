import pytest
from gendiff import generate_diff



result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')

@pytest.fixture()
def data():
    sample = open('tests/fixtures/flat_resalt.txt')
    output = sample.read()
    return output


def test_flat_generate_diff(data):
    assert result == data


def test_type_result():
    assert isinstance(result, str)
