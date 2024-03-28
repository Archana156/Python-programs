import pandas as pd

class DataFrame:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.data_frames = [pd.read_csv(file_path) for file_path in file_paths]

    def compare_and_print(self):
        for i, df in enumerate(self.data_frames):
            print(f"DataFrame {i + 1}:")
            print(df)

        match_results = [self.data_frames[i].apply(tuple, 1).isin(self.data_frames[i + 1].apply(tuple, 1)) for i in range(len(self.data_frames) - 1)] # len DF = 3 i = 0 and again i+1 = 1 = 1
        # so it iterate end of number
        for i, match_result in enumerate(match_results): # i=0, match_results = 3 it start from 1 but i start from 0
            print(f"\nMatch result for DataFrame {i + 1} and DataFrame {i + 2}:")  # i +1 = 1 so it take dataframe 1 compare to i+2 = 2 so dataframe 2
            print(match_result)
            print()

        difference_results = [self.data_frames[i][~self.data_frames[i].apply(tuple, 1).isin(self.data_frames[i + 1].apply(tuple, 1))] for i in range(len(self.data_frames) - 1)]

        for i, difference_result in enumerate(difference_results):
            print(f"Difference in data between DataFrame {i + 1} and DataFrame {i + 2}:")
            print(difference_result)
            print()

        merge_results = [self.data_frames[i].merge(self.data_frames[i + 1], indicator=True, how='outer').loc[lambda v: v['_merge'] != 'both'] for i in range(len(self.data_frames) - 1)]

        for i, merge_result in enumerate(merge_results):
            print(f"Merge result for DataFrame {i + 1} and DataFrame {i + 2}:")
            print(merge_result)
            print()

file_paths = [
    r'C:\Users\as4\Downloads\archive\climate_change_indicators - Bronze.csv',
    r'C:\Users\as4\Downloads\archive\climate_change_indicators - Silver.csv',
    r'C:\Users\as4\Downloads\archive\climate_change_indicators - Gold.csv'
]

data_frame = DataFrame(file_paths)

data_frame.compare_and_print()
