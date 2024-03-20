import pandas as pd


class Preprocess:

    def __init__(self, scale_age: bool=True):
        self.scale_age = scale_age

    def __impute_age(self, target:pd.Series):
        return target.median()

    def __impute_gender(self, target:pd.Series):
        return target.mode()

    def __scale_age(self, x: float , min_v: float, max_v: float):
        return (x-min_v) / (max_v-min_v)

    def __call__(self, df:pd.DataFrame):
        df['Age'] = df['Age'].fillna(self.__impute_age(df['Age']))
        df['Gender'] = df['Gender'].fillna(self.__impute_gender(df['Gender']))
        if self.scale_age:
            df['Age_scaled'] = df['Age'].apply(lambda x: self.__scale_age(x, df['Age'].min(), df['Age'].max()))

        return df