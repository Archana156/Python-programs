import pandas as pd
'''file_path = 'C:\\Users\\as4\\OneDrive - Gainwell Technologies\\Documents\\emp_details.csv'
df = pd.read_csv(file_path)
print(df)'''
class data_check:
    def __init__(self,file_path):
        self.file_pathh = file_path
        df = pd.read_csv(self.file_pathh)
        if df.empty:
            print("no data found inside the CVS file")
        else:
            print("data is aavailable in the CSV file")
            print("print some rows ", "\t",df.head())
ob = data_check('C:\\Users\\as4\\OneDrive - Gainwell Technologies\\Documents\\emp_details.csv')
'''import pandas as pd

class DataCheck:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        try:
            df = pd.read_csv(self.file_path)
            print(df.head())  # Check if data is read successfully
        except Exception as e:
            print(f"Error reading data: {e}")

if __name__ == "__main__":
    file_path = 'C:\\Users\\as4\\OneDrive - Gainwell Technologies\\Documents\\Student_inormation.csv'
    ob = DataCheck(file_path)
    ob.read_data()'''

