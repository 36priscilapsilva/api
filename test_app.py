from app import app
import json

def test_get_itens():
    tester = app.test_client()
    response = tester.get('/itens')
    assert response.status_code == 200
    assert type(response.get_json()) == list

def test_post_item():
    tester = app.test_client()
    payload = {"nome": "Teste"}
    response = tester.post('/itens',
                           data=json.dumps(payload),
                           content_type='application/json')
    assert response.status_code == 201
    assert response.get_json() == payload
