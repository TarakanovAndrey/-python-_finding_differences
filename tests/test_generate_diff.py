from gendiff import generate_diff


# def test_generate_diff_flat_json_to_stylish():
#     path_file1 = 'gendiff/files/file1_flat.json'
#     path_file2 = 'gendiff/files/file2_flat.json'
#     sample = open('tests/fixtures/flat_to_stylish.txt')
#     output = sample.read()
#     assert generate_diff(path_file1, path_file2) == output
#
#
# def test_generate_diff_flat_yml_to_stylish():
#     path_file1 = 'gendiff/files/file1_flat.yml'
#     path_file2 = 'gendiff/files/file2_flat.yaml'
#     sample = open('tests/fixtures/flat_to_stylish.txt')
#     output = sample.read()
#     assert generate_diff(path_file1, path_file2) == output
#
#
# def test_generate_diff_flat_json_to_plain():
#     path_file1 = 'gendiff/files/file1_flat.json'
#     path_file2 = 'gendiff/files/file2_flat.json'
#     sample = open('tests/fixtures/flat_to_plain.txt')
#     output = sample.read()
#     assert generate_diff(path_file1, path_file2, 'plain') == output
#
#
# def test_generate_diff_flat_yml_to_plain():
#     path_file1 = 'gendiff/files/file1_flat.yml'
#     path_file2 = 'gendiff/files/file2_flat.yaml'
#     sample = open('tests/fixtures/flat_to_plain.txt')
#     output = sample.read()
#     assert generate_diff(path_file1, path_file2, 'plain') == output
#
#
# def test_generate_diff_flat_json_to_json():
#     path_file1 = 'gendiff/files/file1_flat.json'
#     path_file2 = 'gendiff/files/file2_flat.json'
#     sample = open('tests/fixtures/flat_to_json.txt')
#     output = sample.read()
#     assert generate_diff(path_file1, path_file2, 'json') == output
#
#
# def test_generate_diff_flat_yml_to_json():
#     path_file1 = 'gendiff/files/file1_flat.yml'
#     path_file2 = 'gendiff/files/file2_flat.yaml'
#     sample = open('tests/fixtures/flat_to_json.txt')
#     output = sample.read()
#     assert generate_diff(path_file1, path_file2, 'json') == output
#
#
def test_generate_diff_nested_json_to_stylish():
    path_file1 = 'gendiff/files/file1_nested.json'
    path_file2 = 'gendiff/files/file2_nested.json'
    sample = open('tests/fixtures/nested_to_stylish.txt')
    output = sample.read()
    assert generate_diff(path_file1, path_file2) == output


def test_generate_diff_nested_yml_to_stylish():
    path_file1 = 'gendiff/files/file1_nested.yml'
    path_file2 = 'gendiff/files/file2_nested.yaml'
    sample = open('tests/fixtures/nested_to_stylish.txt')
    output = sample.read()
    assert generate_diff(path_file1, path_file2) == output


def test_generate_diff_nested_json_to_plain():
    path_file1 = 'gendiff/files/file1_nested.json'
    path_file2 = 'gendiff/files/file2_nested.json'
    sample = open('tests/fixtures/nested_to_plain.txt')
    output = sample.read()
    assert generate_diff(path_file1, path_file2, 'plain') == output


def test_generate_diff_nested_yml_to_plain():
    path_file1 = 'gendiff/files/file1_nested.yml'
    path_file2 = 'gendiff/files/file2_nested.yaml'
    sample = open('tests/fixtures/nested_to_plain.txt')
    output = sample.read()
    assert generate_diff(path_file1, path_file2, 'plain') == output


def test_generate_diff_nested_json_to_json():
    path_file1 = 'gendiff/files/file1_nested.json'
    path_file2 = 'gendiff/files/file2_nested.json'
    sample = open('tests/fixtures/nested_to_json.txt')
    output = sample.read()
    assert generate_diff(path_file1, path_file2, 'json') == output


def test_generate_diff_nested_yml_to_json():
    path_file1 = 'gendiff/files/file1_nested.yml'
    path_file2 = 'gendiff/files/file2_nested.yaml'
    sample = open('tests/fixtures/nested_to_json.txt')
    output = sample.read()
    assert generate_diff(path_file1, path_file2, 'json') == output
