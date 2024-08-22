import pytest
from app import app, db, Player

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        # Add a test player to the database
        test_player = Player(name="Test Player", position="Forward", age=25)
        db.session.add(test_player)
        db.session.commit()
    
    with app.test_client() as client:
        yield client
    
    with app.app_context():
        db.drop_all()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_get_players(client):
    response = client.get('/api/players')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'name' in data[0]
    assert 'position' in data[0]
    assert 'age' in data[0]

def test_metrics_endpoint(client):
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b'players_api_requests_total' in response.data