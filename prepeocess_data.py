import pandas as pd

# Load the CSV file into a DataFrame
data = pd.read_csv('train_new.csv')

empty_cell_counts = data.isna().sum() # No missing data

# Convert age from days to years
data['Age'] = data['Age'].apply(lambda x: x/365)

# Replace 'Sex' values with 0 for male and 1 for female
data['Sex'] = data['Sex'].map({'M': 0, 'F': 1})

data['Drug'] = data['Drug'].map({'D-penicillamine': 0, 'Placebo': 1})

data = data[data['Edema'] != 'S']

# Replace 'Y' and 'N' values with 1 and 0, respectively, for all other columns
cols_to_replace = ['Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin.IR', 'Cholesterol.IR', 'Albumin.IR', 'Copper.IR', 'Alk_Phos.IR', 'SGOT.IR', 'Tryglicerides.IR', 'Platelets.IR', 'Prothrombin.IR']
data[cols_to_replace] = data[cols_to_replace].replace({'N': 0, 'Y': 1})

# Drop irrelevant cols from the dataset
#cols_to_drop = ['id', 'Ascites', 'Hepatomegaly', 'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin']
#new_data = data.drop(cols_to_drop, axis=1)

cols_to_drop = ['id', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin','Status']
new_data = data.drop(cols_to_drop, axis=1)

# Save the modified DataFrame as a new CSV file without cols_to_replace
new_csv = 'new_dataset1.csv'
new_data.to_csv(new_csv, index=False)
