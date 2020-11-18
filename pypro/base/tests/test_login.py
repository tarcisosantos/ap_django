import pytest
from django.urls import reverse
from model_mommy import mommy


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


def test_login_form_page(resp):
    assert resp.status_code == 200


@pytest.fixture
def usuario(db, django_user_model):
    usuario_model = mommy.make(django_user_model)
    senha = 'senha'
    usuario_model.set_password(senha)
    usuario_model.save()
    usuario_model.senha_plana = senha
    return usuario_model


@pytest.fixture
def resp_post(client, usuario):
    return client.post(reverse('login'), {'username': usuario.email, 'password': usuario.senha_plana})


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('modulos:indice')
