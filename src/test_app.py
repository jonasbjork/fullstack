from app import app, summa, differens


# Testa funktionerna
def test_summa():
    assert summa(3, 4) == 7
    assert summa(-1, 1) == 0
    assert summa(0, 0) == 0


def test_differens():
    assert differens(10, 5) == 5
    assert differens(0, 5) == -5
    assert differens(-3, -7) == 4


# Testa Flask-applikationen
def test_hello():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_summa_endpoint():
    response = app.test_client().get('/summa?a=3&b=4')
    print(response.data)
    assert b'{"result":7}' in response.data


def test_differens_endpoint():
    response = app.test_client().get('/differens?a=10&b=5')
    assert b'{"result":5}' in response.data


# Testa ogiltiga anrop
def test_invalid_endpoint():
    response = app.test_client().get('/invalid')
    assert response.status_code == 404
    assert b'Not Found' in response.data


def test_invalid_query():
    response = app.test_client().get('/summa?a=3')
    assert response.status_code == 400
    assert b'Bad Request' in response.data
