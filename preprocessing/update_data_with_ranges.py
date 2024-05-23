import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("train.csv")

# Define a function to check if the test result falls within the specified age range
def check_test_result(row):
    age_days = row['Age']
    alk_phos = row['Alk_Phos']
    copper = row['Copper']
    sgot = row['SGOT']
    platelets = row['Platelets']
    gender = row['Sex']
    status = row['Status']
    bilirubin = row['Bilirubin']
    cholesterol = row['Cholesterol']
    albumin = row['Albumin']
    Tryglicerides = row['Tryglicerides']
    Prothrombin = row['Prothrombin']

    # Set default values
    alk_phos_check = 'N'
    copper_check = 'N'
    sgot_check = 'N'
    platelets_check = 'N'
    bilirubin_check = 'N'
    cholesterol_check = 'N'
    albumin_check = 'N'
    Tryglicerides_check = 'N'
    Prothrombin_check = 'N'
    st = 0

    # Check Alk_Phos
    if 0 <= age_days <= 14:
        alk_phos_check = 'Y' if 830 <= alk_phos <= 2480 else 'N'
    elif 15 <= age_days <= 364:
        alk_phos_check = 'Y' if 1220 <= alk_phos <= 4690 else 'N'
    elif 365 <= age_days <= 3649:
        alk_phos_check = 'Y' if 1420 <= alk_phos <= 3350 else 'N'
    elif 3650 <= age_days <= 4744:
        alk_phos_check = 'Y' if 1290 <= alk_phos <= 4170 else 'N'
    elif 4745 <= age_days <= 5474:
        alk_phos_check = 'Y' if 1160 <= alk_phos <= 4680 else 'N'
    elif 5475 <= age_days <= 6204:
        alk_phos_check = 'Y' if 820 <= alk_phos <= 3310 else 'N'
    elif 6205 <= age_days <= 6935:
        alk_phos_check = 'Y' if 550 <= alk_phos <= 1490 else 'N'
    elif 6936 <= age_days:
        alk_phos_check = 'Y' if 400 <= alk_phos <= 1290 else 'N'
    else:
        alk_phos_check = 'N'

    # Check Copper
    if 0 <= age_days:
        copper_check = 'Y' if 62 <= copper <= 140 else 'N'

    # Check SGOT based on gender
    if gender == 'F':
        sgot_check = 'Y' if 8 <= sgot <= 45 else 'N'
    else:  # Male
        sgot_check = 'Y' if 8 <= sgot <= 50 else 'N'

    # Check Platelets
    if age_days <= 6570:
        platelets_check = 'Y' if 150 <= platelets <= 450 else 'N'
    else:
        platelets_check = 'Y' if 150 <= platelets <= 350 else 'N'

    # Check Bilirubin
    bilirubin_check = 'Y' if 0.3 <= bilirubin <= 1.2 else 'N'

    # Check Cholesterol
    cholesterol_check = 'Y' if 130 <= cholesterol <= 220 else 'N'

    # Check Albumin
    albumin_check = 'Y' if 3.4 <= albumin <= 5.4 else 'N'

    # Check Triglycerides
    Tryglicerides_check = 'Y' if 0 <= Tryglicerides <= 150 else 'N'

    # Check Prothrombin
    Prothrombin_check = 'Y' if 11 <= Prothrombin <= 13.5 else 'N'
    
    if status == 'D':
        st = 1

    return (alk_phos_check, copper_check, sgot_check, platelets_check, bilirubin_check, cholesterol_check, albumin_check, Tryglicerides_check, Prothrombin_check, st)

# Apply the function to each row of the DataFrame and store the result in new columns
df['Alk_Phos.IR'], df['Copper.IR'], df['SGOT.IR'], df['Platelets.IR'], df['Bilirubin.IR'], df['Cholesterol.IR'], df['Albumin.IR'], df['Tryglicerides.IR'], df['Prothrombin.IR'], df['st'] = zip(*df.apply(check_test_result, axis=1))

# Write the updated DataFrame to a new CSV file
df.to_csv("train_new.csv", index=False)