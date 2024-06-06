# affichage des données
import pandas as pd 
path = "C:\\Users\\monte\\OneDrive\\Desktop\\Sale_data_analysis\\sale_data.csv"
sdf = pd.read_csv(path)
print(sdf)

# information sur la database

print(type(sdf))
print(len(sdf.columns))
print(len(sdf.index))
sdf.info()