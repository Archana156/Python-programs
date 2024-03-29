import pandas as pd

def duplicate_data_in_column(df, column_name):
    duplicate_data = df[df[column_name].duplicated(keep=False)]
    return duplicate_data

def duplicate_data_in_row(df):
    duplicate_rows = df[df.duplicated(keep=False)]
    return duplicate_rows

def main():
    try:
        file_path = r'C:\Users\as4\Downloads\archive\climate_change_indicators - Bronze.csv'
        df = pd.read_csv(file_path)
        
        column_name = 'ISO2'
        duplicate_data = duplicate_data_in_column(df, column_name)
        if not duplicate_data.empty:
            print(f"Duplicate data in column '{column_name}':")
            print(duplicate_data)
        else:
            print(f"No duplicate data found in column '{column_name}'.")

        duplicate_data_in_rows = duplicate_data_in_row(df)
        if not duplicate_data_in_rows.empty:
            print("\nDuplicate data in rows:")
            print(duplicate_data_in_rows)
        else:
            print("\nNo duplicate data found in rows.")

    except Exception as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    main()
