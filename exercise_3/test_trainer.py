import pandas as pd
from pandas.testing import assert_frame_equal

import pytest
from unittest.mock import patch, MagicMock
from google.cloud import bigquery

from trainer import Data, Trainer


### FIXTURES: use this part to define necessary fixtures

### END OF FIXTURES


### MOCK: use this part to define necessary mock
@pytest.fixture
def mock_query_result():
    mock_df = MagicMock()
    mock_df.result().to_dataframe.return_value = pd.DataFrame(data={"size":[-0.29], "weight":[-1.35], "sweetness":[-1.73], "crunchiness":[-0.34], "juiciness":[2.93], "ripeness":[-0.03], "acidity":[2.62], "quality": ["bad"]})
    
    return mock_df
    
### END OF MOCK



@patch("google.cloud.bigquery.Client")
def test_trainer_get_data(mock_client_class, mock_query_result):
    # mock BQ client instantiation
    mock_client_instance = MagicMock()
    mock_client_class.return_value = mock_client_instance

    # mock BQ query result
    mock_query_job = MagicMock()
    mock_query_job.result.return_value = mock_query_result
    mock_client_instance.query.return_value = mock_query_job

    data = Data()
    result_df = data.get()

    # mock assertion
    assert result_df.equals(mock_query_result)
    # assert_frame_equal(result_df, mock_query_result) can't be used in this case because they ARE NOT instances of pd.DataFrame, but rather mocked so that they mimic the actual implementation of dataframes.

### TODO: create a mock test for the Trainer class
@patch("...")
def test_trainer_train(...):
    pass

