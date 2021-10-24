import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


if __name__ == '__main__':
    titanic_train = pd.read_csv(
        filepath_or_buffer='./data/train.csv',
        dtype={
            'Sex': 'category',
            'Survived': 'category',
            'Embarked': 'category'
        }
    )
    sns.relplot(
        kind='scatter',
        data=titanic_train,
        x='Age',
        y='Fare',
        hue='Survived'
    )
    plt.title('Scatter')
    plt.show()
