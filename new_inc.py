import pandas as pd

class DataFrames:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.data_frames = [pd.read_csv(file_path) for file_path in file_paths]

    def DataFram_print(self):
        for i, df in enumerate(self.data_frames):
            print(f"DataFrame {i + 1}:")
            print(df)

file_paths = [
    r'C:\Users\as4\Downloads\archive\climate_change_indicators - Bronze.csv',
    r'C:\Users\as4\Downloads\archive\climate_change_indicators - Silver.csv',
    r'C:\Users\as4\Downloads\archive\climate_change_indicators - Gold.csv'
]

data_frame_comparator = DataFrames(file_paths)

data_frame_comparator.DataFram_print()
