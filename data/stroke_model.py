import pandas as pd

from sklearn.linear_model import LogisticRegression as lr
from sklearn.preprocessing import StandardScaler as ss
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

from imblearn.under_sampling import RandomUnderSampler

df = pd.read_csv('data/clean_data.csv')

y = df['stroke']
x = df.drop(columns=['stroke'])

under = RandomUnderSampler(sampling_strategy=0.6)
x_under, y_under = under.fit_resample(x, y)
x_train, x_test, y_train, y_test = train_test_split(x_under, y_under, test_size=0.4)

model = make_pipeline(ss(), lr())
model.fit(x_train, y_train)
accuracy = model.score(x_test, y_test)
print("Accuracy based on Testing Data: ", accuracy)


def calc_prob(user_input):
    # NOTE: Any input into 'predict_proba' needs to be a nested list!
    # 1st = prob of no stroke | 2nd = prob of a stroke
    return model.predict_proba(user_input).tolist()


def model_accuracy():
    return accuracy
