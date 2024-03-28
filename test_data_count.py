import pytest
from Data_count import DataCount

@pytest.fixture
def sample_data_count_instance():
    csv_file_path1 = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Bronze.csv'
    csv_file_path2 = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Silver.csv'
    return DataCount(csv_file_path1, csv_file_path2)

def test_data_count_validation_pass(capsys, sample_data_count_instance):
    sample_data_count_instance.data_count_validation()
    
    captured = capsys.readouterr()
    assert "Data count validation passed." in captured.out

'''def test_data_count_validation_fail():
    with pytest.raises(ValueError, match="Data count validation failed. The number of rows in the two CSV files is not equal.") as exc_info:
        invalid_instance = DataCount('/path/to/first/file.csv', '/path/to/second/file.csv')
        invalid_instance.data_count_validation()


    assert str(exc_info.value) == "Data count validation failed. The number of rows in the two CSV files is not equal."'''