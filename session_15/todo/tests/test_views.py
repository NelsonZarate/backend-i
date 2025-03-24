import pytest

@pytest.mark.django_db
def test_homepage(client):
    response = client.get("/")
    assert response
    assert response.status_code == 200


@pytest.mark.django_db
def test_tasks_not_logged(client):
    response = client.get("/tasks")
    assert response
    assert response.status_code != 200