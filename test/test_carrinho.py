import pytest
# import numpy as np
from classes.Carrinho import Carrinho
from classes.Produto import Produto
import requests

"""

    Os outros testes do carrinho, são testes que requerem integração, 
    logo seram realizados em outro arquivo (arq de integração)
    
"""

@pytest.mark.carrinho
def test_criacao_carrinho():
    carrinho = Carrinho()
    assert carrinho.get_item() == {}

@pytest.mark.carrinho
def test_carrinho_adc_item():
    nome = 'Sabão em Pó'
    prod_id = 45678
    prod = Produto(nome=nome,id=prod_id)
    carrinho = Carrinho()
    carrinho.adicionar_item(prod, 10)
    result = carrinho.get_item()
    assert prod.id in result and result[prod_id] == 10