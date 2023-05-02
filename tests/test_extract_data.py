from gendiff.auxiliary.extract_data import extract_data_from_file


def test_type_datas_from_extract_data():
    path_file1 = 'gendiff/files/file1_flat.json'
    path_file2 = 'gendiff/files/file2_flat.json'
    data1, data2 = extract_data_from_file(path_file1, path_file2)
    assert type(data1) is dict
    assert type(data2) is dict
