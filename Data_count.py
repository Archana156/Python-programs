import pandas as pd

class DataCount:
    def __init__(self, file_path1, file_path2):
        self.file_path1 = file_path1
        self.file_path2 = file_path2
        self.df1 = pd.read_csv(self.file_path1)
        self.df2 = pd.read_csv(self.file_path2)

    def data_count_validation(self):
        
        print(f"Number of rows in Bronze Table: {len(self.df1)}")
        print(f"Number of rows in Silver Table: {len(self.df2)}")
    
        if len(self.df1) != len(self.df2):
            raise ValueError("Data count validation failed. The number of rows in the two CSV files is not equal.")
        else:
            print("Data count validation passed. The number of rows in the two CSV files is equal.")
            

def main():
    
    file_path1 = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Bronze.csv'
    file_path2 = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Silver.csv'


    data_counter = DataCount(file_path1, file_path2)
    
    try:

        data_counter.data_count_validation()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
