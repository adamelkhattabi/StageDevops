import requests
import pytest

@pytest.fixture(scope="module")
def api_url():
    return "http://web:5000"  # This should match your service name in docker-compose

def test_players_api(api_url):
    response = requests.get(f"{api_url}/api/players")
    assert response.status_code == 200
    players = response.json()
    assert isinstance(players, list)
    assert len(players) > 0
    assert all(isinstance(player, dict) for player in players)
    assert all("name" in player for player in players)