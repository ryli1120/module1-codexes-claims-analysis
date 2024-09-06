#Hw assignment 1
import pandas as pd

#Step 1: Load the Data
df = pd.read_csv('https://data.cms.gov/sites/default/files/2023-04/67157de9-d962-4af0-bf0e-3578b3afec58/inpatient.csv', sep='|')
print(df.columns)


#Step 2: Explore the Dataset
#8 Different medical codexes
admitting_diagnosis_codes = df["ADMTG_DGNS_CD"] 
principal_diagnosis_codes = df['PRNCPAL_DGNS_CD']
icd_codes1 = df['ICD_DGNS_CD1']
icd_codes25 = df['ICD_DGNS_CD25']
claim_drg_codes = df['CLM_DRG_CD']
hcpcs_codes = df['HCPCS_CD']
patient_discharge_status_codes = df['PTNT_DSCHRG_STUS_CD']
icd_procedure_code1 = df['ICD_PRCDR_CD1']


#Step 3: Analyze frequency of each unique value
print("\nFrequency of each unique value:")
# Calculate the frequency of each admitting diagnosis code
admitting_diagnosis_frequency = admitting_diagnosis_codes.value_counts()
print("\nAdmitting Diagnosis Codes Frequency:\n", admitting_diagnosis_frequency)

# Calculate the frequency of each principal diagnosis code
principal_diagnosis_frequency = df['PRNCPAL_DGNS_CD'].value_counts()
print("\nPrincipal Diagnosis Codes Frequency:\n", principal_diagnosis_frequency)

# Calculate the frequency of each ICD diagnosis code 1
icd_codes1_frequency = df['ICD_DGNS_CD1'].value_counts()
print("\nICD Diagnosis Codes 1 Frequency:\n", icd_codes1_frequency)

# Calculate the frequency of each ICD diagnosis code 25
icd_codes25_frequency = df['ICD_DGNS_CD25'].value_counts()
print("\nICD Diagnosis Codes 25 Frequency:\n", icd_codes25_frequency)

# Calculate the frequency of each claim DRG code
claim_drg_codes_frequency = df['CLM_DRG_CD'].value_counts()
print("\nClaim DRG Codes Frequency:\n", claim_drg_codes_frequency)

# Calculate the frequency of each HCPCS code
hcpcs_codes_frequency = df['HCPCS_CD'].value_counts()
print("\nHCPCS Codes Frequency:\n", hcpcs_codes_frequency)

# Calculate the frequency of each patient discharge status code
patient_discharge_status_frequency = df['PTNT_DSCHRG_STUS_CD'].value_counts()
print("\nPatient Discharge Status Codes Frequency:\n", patient_discharge_status_frequency)

# Calculate the frequency of each ICD procedure code 1
icd_procedure_code1_frequency = df['ICD_PRCDR_CD1'].value_counts()
print("\nICD Procedure Code 1 Frequency:\n", icd_procedure_code1_frequency)


#Step 4: Handle missing data
missing_admitting_diagnosis = admitting_diagnosis_codes.isnull().sum()
missing_principal_diagnosis = principal_diagnosis_codes.isnull().sum()
missing_icd_codes1 = icd_codes1.isnull().sum()
missing_icd_codes25 = icd_codes25.isnull().sum()
missing_claim_drg_codes = claim_drg_codes.isnull().sum()
missing_hcpcs_codes = hcpcs_codes.isnull().sum()
missing_patient_discharge_status = patient_discharge_status_codes.isnull().sum()
missing_icd_procedure_code1 = icd_procedure_code1.isnull().sum()

print("\nMissing Data Analysis:")
print(f"\nMissing Admitting Diagnosis Codes: {missing_admitting_diagnosis}")
print(f"Missing Principal Diagnosis Codes: {missing_principal_diagnosis}")
print(f"Missing ICD Diagnosis Codes 1: {missing_icd_codes1}")
print(f"Missing ICD Diagnosis Codes 25: {missing_icd_codes25}")
print(f"Missing Claim DRG Codes: {missing_claim_drg_codes}")
print(f"Missing HCPCS Codes: {missing_hcpcs_codes}")
print(f"Missing Patient Discharge Status Codes: {missing_patient_discharge_status}")
print(f"Missing ICD Procedure Code 1: {missing_icd_procedure_code1}")

#filling with placeholder
admitting_diagnosis_codes.fillna('MISSING', inplace=True)
principal_diagnosis_codes.fillna('MISSING', inplace=True)
icd_codes1.fillna('MISSING', inplace=True)
icd_codes25.fillna('MISSING', inplace=True)
claim_drg_codes.fillna('MISSING', inplace=True)
hcpcs_codes.fillna('MISSING', inplace=True)
patient_discharge_status_codes.fillna('MISSING', inplace=True)
icd_procedure_code1.fillna('MISSING', inplace=True)


#Step 5: Summary of Findings
#Provide a summary of the most common codes
# Print the top 5 most common codes for each category
print("\nSummary of Findings:")
print("\nTop 5 Most Common Admitting Diagnosis Codes:\n", admitting_diagnosis_frequency.head(5))
print("\nTop 5 Most Common Principal Diagnosis Codes:\n", principal_diagnosis_frequency.head(5))
print("\nTop 5 Most Common ICD Diagnosis Codes 1:\n", icd_codes1_frequency.head(5))
print("\nTop 5 Most Common ICD Diagnosis Codes 25:\n", icd_codes25_frequency.head(5))
print("\nTop 5 Most Common Claim DRG Codes:\n", claim_drg_codes_frequency.head(5))
print("\nTop 5 Most Common HCPCS Codes:\n", hcpcs_codes_frequency.head(5))
print("\nTop 5 Most Common Patient Discharge Status Codes:\n", patient_discharge_status_frequency.head(5))
print("\nTop 5 Most Common ICD Procedure Code 1:\n", icd_procedure_code1_frequency.head(5))


#Additional Analysis
#Filters dataset where ICD code is I10 (Hypertension)
hypertension_related = df[df['ICD_DGNS_CD1'].str.contains('I10', na=False)]

# Calculates the frequency of each HCPCS code within the hypertension related subset
common_hcpcs_for_hypertension = hypertension_related['HCPCS_CD'].value_counts()

print("\nMost Common HCPCS Codes for Patients with ICD Code I10 (Hypertension):\n", common_hcpcs_for_hypertension)