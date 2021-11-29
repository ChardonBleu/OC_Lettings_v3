import pytest
from django.test import Client
from django.urls import reverse

from .models import Address, Letting


@pytest.fixture
def client(db) -> Client:
    return Client()


@pytest.fixture
def address1(db) -> Address:
    return Address.objects.create(
        number=1,
        street="Rue du port",
        city="ma_ville",
        state="HP",
        zip_code="12345",
        country_iso_code="EU",
    )


@pytest.fixture
def letting1(db, address1) -> Letting:
    return Letting.objects.create(title="Ma maison de vacances", address=address1)


def test_index_lettings(client: Client) -> None:
    response = client.get(reverse("lettings:index"), data={})
    assert response.status_code == 200
    assert "<title>Lettings</title>" in str(response.content)


def test_detail_letting(client: Client, letting1: Letting) -> None:
    response = client.get(reverse("lettings:letting", args=[1]), data={})
    assert response.status_code == 200
    assert "Ma maison de vacances" in str(response.content)


def test_str_letting(letting1: Letting) -> None:
    assert str(letting1) == "Ma maison de vacances"


def test_str_address(address1: Address) -> None:
    assert str(address1) == "1 Rue du port"
