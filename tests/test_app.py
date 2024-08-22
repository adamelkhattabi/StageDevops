import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
    
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
    assert isinstance(response.json, list)

def test_metrics_endpoint(client):
    response = client.get('/metrics')
    assert response.status_code == 200