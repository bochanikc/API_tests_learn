from pprint import pprint
import pytest

TEST_RESULT_EXAMPLE = '''{
    "now": 1604311413,
    "now_dt": "2020-11-02T10:03:33.089Z",
    "info": {
        "lat": 55.75396,
        "lon": 37.620393,
        "url": "https://yandex.ru/pogoda/?lat=55.75396&lon=37.620393"
    },
    "fact": {
        "temp": 7,
        "feels_like": 5,
        "icon": "ovc",
        "condition": "overcast",
        "wind_speed": 2,
        "wind_gust": 6.7,
        "wind_dir": "e",
        "pressure_mm": 752,
        "pressure_pa": 1003,
        "humidity": 89,
        "daytime": "d",
        "polar": false,
        "season": "autumn",
        "obs_time": 1604310800
    },
    "forecast": {
        "date": "2020-11-02",
        "date_ts": 1604264400,
        "week": 45,
        "sunrise": "07:38",
        "sunset": "16:46",
        "moon_code": 1,
        "moon_text": "moon-code-1",
        "parts": [
            {
                "part_name": "evening",
                "temp_min": 7,
                "temp_max": 7,
                "temp_avg": 7,
                "feels_like": 4,
                "icon": "ovc",
                "condition": "overcast",
                "daytime": "n",
                "polar": false,
                "wind_speed": 3,
                "wind_gust": 6,
                "wind_dir": "e",
                "pressure_mm": 752,
                "pressure_pa": 1003,
                "humidity": 93,
                "prec_mm": 0,
                "prec_period": 360,
                "prec_prob": 0
            },
            {
                "part_name": "night",
                "temp_min": 6,
                "temp_max": 7,
                "temp_avg": 7,
                "feels_like": 4,
                "icon": "ovc",
                "condition": "overcast",
                "daytime": "n",
                "polar": false,
                "wind_speed": 2.7,
                "wind_gust": 5.8,
                "wind_dir": "e",
                "pressure_mm": 752,
                "pressure_pa": 1003,
                "humidity": 94,
                "prec_mm": 0,
                "prec_period": 360,
                "prec_prob": 0
            }
        ]
    }
}'''


@pytest.mark.parametrize('token, status_code_answer', [('', 403), ('test', 403)])
def test_autorization_fail_status_code_403(api_client, token, status_code_answer, lat=55.75396, lon=37.620393):
    result = api_client.get(
        path=f'/v2/informers?lat={lat}&lon={lon}',
        headers={'X-Yandex-API-Key': token}
    )
    assert result.status_code == status_code_answer


def test_autorization_success(api_client, status_code_answer=200, lat=55.75396, lon=37.620393):
    result = api_client.get(
        path=f'/v2/informers?lat={lat}&lon={lon}',
        headers={'X-Yandex-API-Key': api_client.token}
    )
    assert result.status_code == status_code_answer
