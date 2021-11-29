import pytest
from django.test import Client
from django.urls import reverse


@pytest.fixture
def client(db) -> Client:
    return Client()


def test_index_root_site(client: Client) -> None:
    response = client.get(reverse("index"), data={})
    assert response.status_code == 200
    assert "<title>Holiday Homes</title>" in str(response.content)


def test_sentry(client: Client) -> None:
    try:
        client.get("/sentry-debug/", data={})
    except ZeroDivisionError:
        assert 1
