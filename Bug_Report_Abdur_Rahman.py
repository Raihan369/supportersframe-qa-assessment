import pandas as pd
import os

def main():
    print("=======================================")
    print("   SupportersFrame Website Bug Report  ")
    print("=======================================\n")

    file_name = "Bug_Report_Abdur_Rahman.xlsx"

    # Check if file exists
    if not os.path.exists(file_name):
        print("Error: Excel file not found!")
        print("Make sure 'Bug_Report_Abdur_Rahman.xlsx' is in the same folder as this script.")
        input("\nPress Enter to exit...")
        return

    try:
        # Load Excel file
        df = pd.read_excel(file_name)

        print("Bug Report Loaded Successfully!\n")
        print("Total Bugs Found:", len(df))
        print("\nBug Summary:\n")
        
        # Show table
        print(df.to_string(index=False))

    except Exception as e:
        print("Error reading Excel file:", e)

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()