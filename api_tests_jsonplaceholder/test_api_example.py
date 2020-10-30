import pytest
import random


@pytest.mark.parametrize('userId, userId_in_response', [(1, 1), (2, 2)])
def test_api_get_request_id_filtering(api_client, userId, userId_in_response):
    result = api_client.get(
        path='/posts',
        params={'userId': userId}
    )
    random_post_number = random.randint(1, 10)
    assert result.json()[random_post_number]['userId'] == userId_in_response


@pytest.mark.parametrize('input_id, output_id',
                         [(1000, '1000'), (-1, '-1'), (100, '100'), (0, '0')])
@pytest.mark.parametrize('input_title, output_title',
                         [('test', 'test'), ('', ''), (100, '100'), ('!-!', '!-!')])
def test_api_post_add_post(api_client, input_id, output_id, input_title, output_title):
    result = api_client.post(
        path='/posts',
        data={'title': input_title,
              'body': 'bar',
              'userId': input_id
              }).json()
    assert result['title'] == output_title
    assert result['body'] == 'bar'
    assert result['userId'] == output_id
