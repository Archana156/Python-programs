import pandas as pd
class read_file:
    def __init__(self,file_path):
        self.file_pathh = file_path
        self.df = pd.read_csv(self.file_pathh)
        
    def check_column(self,column_data):
        self.column_data = column_data
        self.column = self.df[self.column_data]
        
    def assert_data(self):
        assert all(isinstance(value, str)for value in self.column),f"Data type check failed for column '{self.column_data}'"
        print(f"Data type check passed for column '{self.column_data}'")
        
file_path = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Bronze.csv'
column_name_to_check = 'Country'

obj = read_file(file_path)
obj.check_column(column_name_to_check)
obj.assert_data()