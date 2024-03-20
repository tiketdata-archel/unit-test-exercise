from google.cloud import bigquery

from sklearn.linear_model import LogisticRegression


class Data:
    def __init___(self):
        pass

    def get(self):
        client = bigquery.Client()
        QUERY = (
                    'SELECT * EXCEPT(apple_id) FROM `tiket-0818.sandbox_datascientist.archel_apple_quality`'
                )
        query_job = client.query(QUERY)
        df_result = query_job.result().to_dataframe()

        return df_result


class Trainer:

    def __init__(self):
        pass

    def train(self, X, y):
        model = LogisticRegression(random_state=0).fit(X, y)
        return model