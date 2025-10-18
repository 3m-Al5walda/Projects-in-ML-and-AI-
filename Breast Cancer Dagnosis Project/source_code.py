
import pandas as pd
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

x = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data['target'])

import seaborn as sns

sns.barplot(x=y.value_counts().index,y=y.value_counts())

# print the first 5 records
x.head()

# get the number of rows and columns
x.shape

#==================================================== preprocess =============================================
# نقوم بالتاكد من البيانات اذا كانت تحوي قيم مفقودة
x.isnull().sum()

x.isna().sum()

y.isnull().sum()

import numpy as np

# Random values assignment black and white && add the new feuter " complexion"
np.random.seed(42)
x['complexion'] = np.random.choice(['white', 'black'], size=len(x))

# display the values
x['complexion'].value_counts()

sns.barplot(x=x['complexion'].value_counts().index,y=x['complexion'].value_counts(),color='red')

# get count of the number of malogant (0) or benign (1) cells
y.value_counts()

# data with sensitve data
x.shape

# data without sensitve data
#X_without_sensitive.shape

# encodeing for black and white | black = 1 and white = 2 , We did this to avoid potential errors.
x['complexion_encoded'] = x['complexion'].map(lambda e : 2 if e == 'white' else 1)
x.drop('complexion',inplace=True , axis = 1)

x.head()

from sklearn.preprocessing import StandardScaler

sensitve_col = x['complexion_encoded']
X_scaled = StandardScaler().fit_transform(x.drop('complexion_encoded',axis=1))

# split the data set into 75% training and 25% testing

from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test,s_train,s_test = train_test_split(X_scaled,y,sensitve_col,test_size=0.25,random_state=42)

from sklearn.metrics import accuracy_score , precision_score, recall_score, f1_score

!pip install fairlearn

from fairlearn.metrics import MetricFrame ,demographic_parity_difference , equalized_odds_difference , selection_rate

#######################################
# create a function for models ....
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

def models(X_train,y_train, X_test, y_test,sensitive_features): # Added X_test as an argument
  models = {
    'LR': LogisticRegression(max_iter=1000),      # Logistic Regression
    'SVM': SVC(probability=True , random_state=42),                   # Support Vector Machine
    'NN': MLPClassifier(max_iter=1000,random_state=42)            # Neural Network
  }
  results = []
  data = X_train
  for nameModel , model in models.items():
    model.fit(data,y_train)
    y_pred = model.predict(X_test) # Changed to predict on X_test instead of X_train
    metrics = {
      'name ' : nameModel,
      'accuracy': accuracy_score(y_test,y_pred), # Changed to compare with y_test
      'precision': precision_score(y_test,y_pred), # Changed to compare with y_test
      'recall': recall_score(y_test,y_pred), # Changed to compare with y_test
      'f1': f1_score(y_test,y_pred)   } # Changed to compare with y_test
    metric_frame = MetricFrame(
            metrics={"selection_rate": selection_rate, "accuracy": accuracy_score},
            y_true=y_test,
            y_pred=y_pred,
            sensitive_features=s_test
        )
    metrics.update({
            "DemographicParityDiff": demographic_parity_difference(y_test, y_pred, sensitive_features=s_test),
            "EqualizedOddsDiff": equalized_odds_difference(y_test, y_pred, sensitive_features=s_test)
    })
    results.append(metrics)
  return results

results = models(x_train,y_train, x_test, y_test,sensitve_col)

result_df = pd.DataFrame(results)

print(result_df)

sns.lineplot(data=result_df)

melted_df = result_df.melt(id_vars='name ', var_name='Metric', value_name='Score')
acc_recall_df = melted_df[melted_df['Metric'].isin(['DemographicParityDiff','EqualizedOddsDiff'])]
sns.lineplot(data=acc_recall_df, x='name ', y='Score', hue='Metric')

acc_recall_df = melted_df[melted_df['Metric'].isin(['accuracy', 'recall', 'precision','f1'])]
sns.lineplot(data=acc_recall_df, x='name ', y='Score', hue=' Metric')

lr_metrics = result_df[result_df['name '] == 'LR']


sns.heatmap(lr_metrics[['accuracy', 'precision', 'recall', 'f1', 'DemographicParityDiff', 'EqualizedOddsDiff']])

Svm_metrics = result_df[result_df['name '] == 'SVM']

sns.heatmap(Svm_metrics[['accuracy', 'precision', 'recall', 'f1', 'DemographicParityDiff', 'EqualizedOddsDiff']])

NN_metrics = result_df[result_df['name '] == 'NN']

sns.heatmap(NN_metrics[['accuracy', 'precision', 'recall', 'f1', 'DemographicParityDiff', 'EqualizedOddsDiff']])

