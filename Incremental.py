import pandas as pd

def increased_data(bronze_df, silver_df):
    
    increased_bronze = pd.concat([bronze_df, silver_df]).drop_duplicates(keep=False)
   # increased_data(bronze_df, bronze_df)
   
    increased_silver = pd.concat([silver_df, bronze_df]).drop_duplicates(keep=False)
    return increased_bronze, increased_silver

def main():
    try:
        bronze_file_path = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Bronze.csv'
        silver_file_path = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Silver.csv'

        bronze_df = pd.read_csv(bronze_file_path)
        silver_df = pd.read_csv(silver_file_path)

        
        increased_bronze, increased_silver = increased_data(bronze_df, silver_df)

        if not increased_bronze.empty:
            print("Increased data in bronze table:")
            print(increased_bronze)
        else:
            print("No data increase detected in bronze table.")

        if not increased_silver.empty:
            print("Increased data in silver table:")
            print(increased_silver)
        else:
            print("No data increase detected in silver table.")
    except Exception as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    main()
