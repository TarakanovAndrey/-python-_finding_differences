from gendiff import generate_diff
import pytest


@pytest.fixture()
def path_json_files():
    path_file1 = 'tests/files/file1_nested.json'
    path_file2 = 'tests/files/file2_nested.json'
    return path_file1, path_file2


@pytest.fixture()
def path_yml_files():
    path_file1 = 'tests/files/file1_nested.yml'
    path_file2 = 'tests/files/file2_nested.yaml'
    return path_file1, path_file2


@pytest.fixture()
def sample_stylish_format():
    sample = open('tests/fixtures/nested_to_stylish')
    output = sample.read()
    return output


@pytest.fixture()
def sample_plain_format():
    sample = open('tests/fixtures/nested_to_plain')
    output = sample.read()
    return output


def test_generate_diff_nested_json_to_stylish(path_json_files, sample_stylish_format):
    assert generate_diff(*path_json_files) == sample_stylish_format


def test_generate_diff_nested_yml_to_stylish(path_yml_files, sample_stylish_format):
    assert generate_diff(*path_yml_files) == sample_stylish_format


def test_generate_diff_nested_json_to_plain(path_json_files, sample_plain_format):
    assert generate_diff(*path_json_files, 'plain') == sample_plain_format


def test_generate_diff_nested_yml_to_plain(path_yml_files, sample_plain_format):
    assert generate_diff(*path_yml_files, 'plain') == sample_plain_format


def test_generate_diff_nested_json_to_json(path_json_files):
    assert isinstance(generate_diff(*path_json_files, 'json'), str)


def test_generate_diff_nested_yaml_to_json(path_yml_files):
    assert isinstance(generate_diff(*path_yml_files, 'json'), str)
