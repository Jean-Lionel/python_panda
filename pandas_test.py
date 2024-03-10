
import pandas as pd

if __name__ == '__main__':
    file_2023 = pd.read_excel("excel/test.xlsx", usecols="A:C,D", sheet_name="2023")
    print(file_2023)
    file_2024 = pd.read_excel("excel/test.xlsx", sheet_name="2024")
    print("==============================================================")
    print(file_2024)
    # accider a une ligne specifique
    print("================NOm du collone===========================")
    print(file_2024.Age)
    print("================NOm du collone avec les crochets================")
    print(file_2024["Date de naissance"])
    
    #Modification d'une valeur
    file_2024.at[1, "Age"] = 80
    print(file_2024)
    # Miltuplier des valueur dans une colonne
    file_2024["Age"] = file_2024["Age"] * 2
    print(file_2024)
    # additionner des valeurs dans les deux fichiers 
    print("Addition des deux tableaux ")
    file_2023["Age"] = file_2023["Age"] + file_2024["Age"]
    print(file_2023)
    # concatener deux tableau 
    print("Concatenation des tableaux ");
    print(pd.concat([file_2023, file_2024]))