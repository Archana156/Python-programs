import pandas as pd

def increased_data(bronze_df, silver_df):
    # Find increased data in bronze table
    increased_bronze = pd.concat([bronze_df, silver_df]).drop_duplicates(keep=False)
    
    # Find increased data in silver table
    increased_silver = pd.concat([silver_df, bronze_df]).drop_duplicates(keep=False)
    
    # Find duplicates in bronze table
    duplicate_bronze = find_duplicates(bronze_df)
    
    # Find duplicates in silver table
    duplicate_silver = find_duplicates(silver_df)
    
    return increased_bronze, duplicate_bronze, increased_silver, duplicate_silver

def find_duplicates(df):
    duplicate_indices = []
    seen = set()
    for index, row in df.iterrows():
        if tuple(row) in seen:
            duplicate_indices.append(index)
        else:
            seen.add(tuple(row))
    return df.iloc[duplicate_indices]

def main():
    try:
        bronze_file_path = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Bronze.csv'
        silver_file_path = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Silver.csv'

        bronze_df = pd.read_csv(bronze_file_path)
        silver_df = pd.read_csv(silver_file_path)

        increased_bronze, duplicate_bronze, increased_silver, duplicate_silver = increased_data(bronze_df, silver_df)

        if not increased_bronze.empty:
            print("Increased data in bronze table:")
            print(increased_bronze)
        else:
            print("No data increase detected in bronze table.")
        
        if not duplicate_bronze.empty:
            print("Duplicate entries in bronze table:")
            print(duplicate_bronze)
        else:
            print("No duplicate entries found in bronze table.")

        if not increased_silver.empty:
            print("Increased data in silver table:")
            print(increased_silver)
        else:
            print("No data increase detected in silver table.")
        
        if not duplicate_silver.empty:
            print("Duplicate entries in silver table:")
            print(duplicate_silver)
        else:
            print("No duplicate entries found in silver table.")
            
    except Exception as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    main()
