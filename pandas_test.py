import pandas as pd
import matplotlib.pyplot as plt

COLUMNS = ['age','workclass', 'fnlwgt', 'education', 'education_num', 'marital',
           'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
           'hours_week', 'native_country', 'label']

PATH = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
df_train = pd.read_csv(PATH,
                       skipinitialspace=True,
                       names = COLUMNS,
                       index_col=False)

df_plot = df_train.groupby(['label', 'marital'])['capital_gain'].mean().unstack()
df_plot.plot()
plt.show()