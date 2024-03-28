import pandas as pd
class read:
    def __init__(self,file_path):
        self.file_pathh = file_path
        df = pd.read_csv(self.file_pathh)

        if df.empty:
            print("no data found inside the CVS file")
        else:
            print("data is aavailable in the CSV file")
            print("print some rows ", "\t",df.head())
            
ob = read(r'C:\Users\as4\Downloads\archive\climate_change_indicators - Bronze.csv')


