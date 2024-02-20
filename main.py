#Objective: To understand the impact of Payers(Insurers) on the treatment preference of a patient and physician for a given market. The Insights should help a pharmaceutical company to target key Payers or Plans to engage in a meaningful discussion for adding their drug as a preferred drug to the specfic payer/plan. Summary can be further breakdown by geography, patients age, payment type, etc., Additionally, Physician's preference of a drug by each plan will also helps in promoting through different channels.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

df_claims_and_patients = pd.read_csv("/Users/manayapachpor/Desktop/Trinity_Hackathon/claims_and_patient.csv.xlsx")


avg_age_by_drug = df_claims_and_patients.groupby('drug_name')['patient_age'].mean()
