import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

file_path = "../preprocessing/new_dataset1.csv"
df = pd.read_csv(file_path)

# Columns to consider for EDA (excluding '.IR' columns)
columns = ['Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos',
           'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin']


def plot_in_range_vs_dead_grouped_bar(df, col):
    in_range_col = col + '.IR'
    total_in_range = df[df[in_range_col] == 1].shape[0]
    total_not_in_range = df[df[in_range_col] == 0].shape[0]

    dead_in_range = df[(df[in_range_col] == 1) & (df['st'] == 1)].shape[0]
    dead_not_in_range = df[(df[in_range_col] == 0) & (df['st'] == 1)].shape[0]

    # Calculate proportions
    prop_dead_in_range = dead_in_range / total_in_range if total_in_range != 0 else 0
    prop_dead_not_in_range = dead_not_in_range / total_not_in_range if total_not_in_range != 0 else 0

    data = {
        'Category': ['In Range', 'Not In Range'],
        'Proportion': [prop_dead_in_range, prop_dead_not_in_range]
    }

    plot_df = pd.DataFrame(data)

    sns.barplot(x='Category', y='Proportion', data=plot_df)
    plt.title(f'{col}')
    plt.ylabel('Proportion of dead')

    plt.show()


# Plotting for each column
for col in columns:
    if col + '.IR' in df.columns:
        plot_in_range_vs_dead_grouped_bar(df, col)

# Calculate the correlation matrix
corr_matrix = df.corr()

# Sort the correlation values with respect to 'st'
corr_with_target = corr_matrix['st'].abs().sort_values(ascending=False)

# Plotting the heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()

# Plot the distribution of the target variable
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', hue='st', multiple='stack', kde=True)
plt.title('Age Distribution by Mortality (st)')
plt.show()

# Feature importance using RandomForest
# Define features and target variable
X = df.drop('st', axis=1)
y = df['st']

# Train a RandomForest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X, y)

# Get feature importances
feature_importances = pd.DataFrame(rf_model.feature_importances_, index=X.columns, columns=['Importance']).sort_values('Importance', ascending=False)


# Plot feature importances
plt.figure(figsize=(12, 8))
sns.barplot(x=feature_importances['Importance'], y=feature_importances.index)
plt.title('Feature Importances')
plt.show()

# Select top 5 most important features for pairplot
top_features = feature_importances.index[:5].tolist()

# Pairplot with top features
sns.pairplot(df[top_features + ['st']], hue='st')
plt.show()

# Boxplots for individual features grouped by 'st'
for feature in top_features:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='st', y=feature, data=df)
    plt.title(f'Boxplot of {feature} by Status')
    plt.show()