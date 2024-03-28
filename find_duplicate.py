import pandas as pd

def find_duplicates(df):
    duplicates = df[df.duplicated()]
    return duplicates

def main():
    try:
        bronze_file_path = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Bronze.csv'
        silver_file_path = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Silver.csv'

        bronze_df = pd.read_csv(bronze_file_path)
        silver_df = pd.read_csv(silver_file_path)

        duplicate_bronze = find_duplicates(bronze_df)
        
        if not duplicate_bronze.empty:
            print("Duplicate entries in bronze table:")
            print(duplicate_bronze)
        else:
            print("No duplicate entries found in bronze table.")

        duplicate_silver = find_duplicates(silver_df)
        
        if not duplicate_silver.empty:
            print("Duplicate entries in silver table:")
            print(duplicate_silver)
        else:
            print("No duplicate entries found in silver table.")
            
    except Exception as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    main()
