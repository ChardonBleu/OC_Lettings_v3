import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from .models import Profile


@pytest.fixture
def client(db) -> Client:
    return Client()


@pytest.fixture
def user1(db) -> User:
    return User.objects.create_user(username="toto", password="totoTestPassword")


@pytest.fixture
def profile1(db, user1: User) -> Profile:
    return Profile.objects.create(user=user1, favorite_city="Paris")


def test_index_profile(client: Client) -> None:
    response = client.get(reverse("profiles:index"), data={})
    assert response.status_code == 200
    assert "<title>Profiles</title>" in str(response.content)


def test_details_profile(client: Client, profile1: Profile) -> None:
    response = client.get(reverse("profiles:profile", args=["toto"]), data={})
    assert response.status_code == 200
    assert "<title>toto</title>" in str(response.content)


def test_str_profile(profile1: Profile) -> None:
    assert str(profile1) == "toto"
