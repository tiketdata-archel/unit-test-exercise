import pandas as pd
from pandas.testing import assert_frame_equal
import pytest

from preprocess import Preprocess


### FIXTURES: use this part to define necessary fixtures
@pytest.fixture
def normal_input():
    return pd.DataFrame(data={
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, None, 28],
        'Gender': ['F', 'M', None, 'M', 'F'],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']
    })

### END OF FIXTURES


### TODO: complete below test case 
def test_preprocess_call_with_age_scale(normal_input):
    preprocess = Preprocess(scale_age=True)
    result = preprocess(normal_input)
    expected_result = pd.DataFrame(data={
        'Name': [], # define the expected values for 'Name'
        'Age': [], # define the expected values for 'Age'
        'Gender': [], # define the expected values for 'Gender'
        'City': [] # define the expected values for 'City'
    })

    # assert result vs expected_result

    # 1 more thing to assert, can you find it?



### TODO: create test cases for the rest of the Preprocess class
### HINT 1: you can always use fixtures to create multiple test cases
### HINT 2: when testing class methods (e.g. __impute_age), you can call them by doing this:
### preprocess = Preprocess()
### result = preprocess.__impute_age(...) --> this will raise an error
### result = preprocess._Preprocess__impute_age(...) --> do this instead





