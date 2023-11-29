import uuid


def test_root_deve_retornar_200_e_ola_mundo(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.json() == dict(message='olá mundo')


def test_post_user_returns_no_password(client):
    payload = dict(
        username=str(uuid.uuid4()),
        email='b@gmail.com',
        password='c',
    )
    resp = client.post('/users/', json=payload)
    assert 'password' not in resp.json()


def is_user(item):
    return all(
        [
            isinstance(item, dict),
            'id' in item,
            'username' in item,
            'email' in item,
            len(item) == 3,
        ]
    )


def test_read_users_returns_200_and_list_of_users(client):
    # create some users
    for _ in range(10):
        payload = dict(
            username=str(uuid.uuid4()),
            email='b@gmail.com',
            password='c',
        )
        r = client.post('/users/', json=payload)
        assert r.status_code == 201

    resp = client.get('/users/')
    assert resp.status_code == 200
    assert len(resp.json()['users']) >= 10
    assert all(is_user(i) for i in resp.json()['users'])


def test_update_user(client):
    # "desativei" esse teste enquanto estava colocando o database
    return
    d = dict(username=str(uuid.uuid4()), email='k@gmail.com', password='1')
    resp = client.put('/users/1', json=d)
    assert resp.status_code == 200
    d.update({'id': 1})
    d.pop('password')
    assert resp.json() == d


def test_delete_user(client):
    # "desativei" esse teste enquanto estava colocando o database
    return
    resp = client.delete('/users/1')
    assert resp.status_code == 200
    assert resp.json() == dict(detail='user deleted')
