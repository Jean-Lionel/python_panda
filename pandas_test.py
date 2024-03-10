
import pandas as pd

if __name__ == '__main__':
    file_2023 = pd.read_excel("excel/test.xlsx")
    print(file_2023)
    file_2024 = pd.read_excel("excel/test.xlsx", sheet_name="2024")
    print("==============================================================")
    print(file_2024)