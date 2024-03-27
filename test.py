import pytest
import requests
import yaml


with open('testcase/api.yaml', 'r') as file:
    test_cases = yaml.safe_load(file)
# 参数化装饰器，传递所有测试用例的数据
@pytest.mark.parametrize("test_case", test_cases)
def test_run(test_case):
    response = requests.request(test_case['method'],test_case['url'], json=test_case['body'])
    assert response.status_code == test_case['status_code']
