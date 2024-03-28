import pandas as pd

def read_csv(file_path):
    return pd.read_csv(file_path)

def main():
    
    file_path1 = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Bronze.csv'
    file_path2 = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Silver.csv'
    file_path3 = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Gold.csv'
    
  
    df1 = read_csv(file_path1)
    df2 = read_csv(file_path2)
    df3 = read_csv(file_path3)

   
    print("DataFrame 1:")
    print(df1)
    print("\nDataFrame 2:")
    print(df2)
    print("\nDataFrame 3:")
    print(df3)

   
    match1 = df1.apply(tuple, 1).isin(df2.apply(tuple, 1))
    print("\nMatch result between DataFrame 1 and DataFrame 2:")
    print(match1)
    print()

    match2 = df3.apply(tuple, 1).isin(df2.apply(tuple, 1))
    print("Match result between DataFrame 3 and DataFrame 2:")
    print(match2)

    
    result2 = df3[~df3.apply(tuple, 1).isin(df2.apply(tuple, 1))]
    print("\nDifference in data between DataFrame 3 and DataFrame 2:")
    print(result2)

  
    result3 = df1.merge(df3, indicator=True, how='outer').loc[lambda v: v['_merge'] != 'both']
    print("\nRows in DataFrame 1 or DataFrame 3 but not in both:")
    print(result3)

    result4 = df1.merge(df2, indicator=True, how='outer').loc[lambda v: v['_merge'] != 'both']
    print("\nRows in DataFrame 1 or DataFrame 2 but not in both:")
    print(result4)

if __name__ == "__main__":
    main()
