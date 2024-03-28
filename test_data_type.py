import pytest
from Myproject.data_type import read_file

@pytest.fixture
def sample_file_path():
    return r'C:\Users\as4\Downloads\archive\climate_change_indicators - Bronze.csv'

@pytest.fixture
def sample_column_name():
    return 'Country'

def test_assert_data_type_check_pass(sample_file_path, sample_column_name, capsys):
    obj = read_file(sample_file_path)
    obj.check_column(sample_column_name)
    obj.assert_data()

    captured = capsys.readouterr()
    assert "Data type check passed" in captured.out

def test_assert_data_type_check_fail():
    sample_file_path = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Bronze.csv'
    sample_column_name = 'ObjectId'

    obj = read_file(sample_file_path)
    obj.check_column(sample_column_name)

    with pytest.raises(AssertionError) as excinfo:
        obj.assert_data()

    assert "Data type check failed" in str(excinfo.value)

