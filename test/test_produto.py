import pytest
# import numpy as np
from classes.Produto import Produto
import requests

@pytest.mark.produto
def test_criacao_de_produto_nome_id():
    nome = 'Sabão em Pó'
    prod_id = 45678
    prod = Produto(nome=nome,id=prod_id)
    assert prod.nome == nome and prod.id == prod_id

@pytest.mark.produto
def test_criacao_de_produto_sem_id():
    with pytest.raises(TypeError) as exc:
        nome = 'Sabão em Pó'
        prod = Produto(nome=nome)
    assert "missing 1 required" in str(exc)

@pytest.mark.produto
def test_criacao_de_produto_sem_nome():
    prod_id = 45678
    prod = Produto(id=prod_id)
    assert prod.nome == '' and prod_id == prod.id

@pytest.mark.produto
def test_method_buscar_nome():
    nome = 'Sabão em Pó'
    prod_id = 45678
    prod = Produto(nome=nome,id=prod_id)
    result = Produto.busca_nome(nome)
    assert result[0].nome == prod.nome and result[0].id == prod.id

@pytest.mark.produto
def test_method_get_id():
    nome = 'Sabão em Pó'
    prod_id = 45678
    prod = Produto(nome=nome,id=prod_id)
    result = prod.get_id()
    assert result == prod.id