import pandas as pd

# FROM: https://www.kaggle.com/fedesoriano/stroke-prediction-dataset
df = pd.read_csv('data/dirty_data.csv')

# Drop any row with N/A data to ensure better accuracy
df = df.dropna()

# Drop ID column since it has no meaning
df.drop(columns=['id'], inplace=True)

# Use label encoding to change categorical data to numerical data
# NOTE: Gets same accuracy as one hot encoding in this case
cleanup_categorical = {
                'gender':           {'Male': 0, 'Female': 1, 'Other': 2},
                'ever_married':     {'No': 0, 'Yes': 1},
                'work_type':        {'Private': 0, 'Self-employed': 1, 'children': 2, 'Govt_job': 3, 'Never_worked': 4},
                'Residence_type':   {'Urban': 0, 'Rural': 1},
                'smoking_status':   {'never smoked': 0, 'Unknown': 1, 'formerly smoked': 2, 'smokes': 3}
                }

df = df.replace(cleanup_categorical)
df.to_csv('data/clean_data.csv', index=False)
