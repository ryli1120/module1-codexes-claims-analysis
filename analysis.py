#Hw assignment 1
import pandas as pd

df = pd.read_csv('https://data.cms.gov/sites/default/files/2023-04/67157de9-d962-4af0-bf0e-3578b3afec58/inpatient.csv', sep=';')

print(df.columns)

admitting_diagnosis_codes = df['ADMTG_DGNS_CD']
principal_diagnosis_codes = df['PRNCPAL_DGNS_CD']
icd_codes1 = df['ICD_DGNS_CD1']
icd_codes25 = df['ICD_DGNS_CD25']
claim_drg_codes = df['CLM_DRG_CD']
hcpcs_codes = df['HCPCS_CD']


# Calculate the frequency of each admitting diagnosis code
admitting_diagnosis_frequency = df['ADMTG_DGNS_CD'].value_counts()
print("Admitting Diagnosis Codes Frequency:\n", admitting_diagnosis_frequency)

# Calculate the frequency of each principal diagnosis code
principal_diagnosis_frequency = df['PRNCPAL_DGNS_CD'].value_counts()
print("Principal Diagnosis Codes Frequency:\n", principal_diagnosis_frequency)

# Calculate the frequency of each ICD diagnosis code 1
icd_codes1_frequency = df['ICD_DGNS_CD1'].value_counts()
print("ICD Diagnosis Codes 1 Frequency:\n", icd_codes1_frequency)

# Calculate the frequency of each ICD diagnosis code 25
icd_codes25_frequency = df['ICD_DGNS_CD25'].value_counts()
print("ICD Diagnosis Codes 25 Frequency:\n", icd_codes25_frequency)

# Calculate the frequency of each claim DRG code
claim_drg_codes_frequency = df['CLM_DRG_CD'].value_counts()
print("Claim DRG Codes Frequency:\n", claim_drg_codes_frequency)

# Calculate the frequency of each HCPCS code
hcpcs_codes_frequency = df['HCPCS_CD'].value_counts()
print("HCPCS Codes Frequency:\n", hcpcs_codes_frequency)


#Struggled to print each column in a separeate line. Was difficult to see all column names available. 

#This function will print hello world
