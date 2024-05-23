import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "new_dataset1.csv"
df = pd.read_csv(file_path)

# Columns to consider for EDA (excluding '.IR' columns)
columns = ['Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos',
           'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin']


# Function to plot data
def plot_in_range_vs_dead_grouped_bar(df, col):
    in_range_col = col + '.IR'
    dead_in_range = df[(df[in_range_col] == 1) & (df['st'] == 1)].shape[0]
    dead_not_in_range = df[(df[in_range_col] == 0) & (df['st'] == 1)].shape[0]

    data = {
        'Category': ['In Range', 'Not In Range'],
        'Count': [dead_in_range, dead_not_in_range]
    }

    plot_df = pd.DataFrame(data)

    sns.barplot(x='Category', y='Count', data=plot_df)
    plt.title(f'{col}')
    plt.ylabel('Number of dead')

    plt.show()


# Plotting for each column
for col in columns:
    if col + '.IR' in df.columns:
        plot_in_range_vs_dead_grouped_bar(df, col)
        
# Calculate the correlation matrix
corr_matrix = df.corr()

# Sort the correlation values with respect to 'st'
corr_with_target = corr_matrix['st'].abs().sort_values(ascending=False)

# Calculate the correlation matrix
corr_matrix = df.corr()

# Plotting the heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()

# Print the top correlated features
print(corr_with_target)

# Plot the distribution of the target variable
sns.countplot(data=df, x='st')
plt.title('Distribution of Mortality (st)')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', hue='st', multiple='stack', kde=True)
plt.title('Age Distribution by Mortality (st)')
plt.show()