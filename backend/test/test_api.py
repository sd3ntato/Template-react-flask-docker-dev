import sys
sys.path.append('../')
import pytest

from server import create_app

@pytest.fixture
def client():
  app = create_app()
  app.config['TESTING'] = True

  with app.test_client() as client:
    yield client

def test_get_data(client):
  res = client.get('/data')
  assert res.status_code == 200
