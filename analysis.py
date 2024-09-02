#Hw assignment 1
import pandas as pd

df = pd.read_csv('https://data.cms.gov/sites/default/files/2023-04/67157de9-d962-4af0-bf0e-3578b3afec58/inpatient.csv', sep=';')

print(df.columns)


# print(data.head())

# icd_codes = data['ICD_CODE']
# drg_codes = data['DRG_CODE']
# hcpcs_codes = data['HCPCS_CODE']

#Struggled to print each column in a separeate line. Was difficult to see all column names available. 

#This function will print hello world
