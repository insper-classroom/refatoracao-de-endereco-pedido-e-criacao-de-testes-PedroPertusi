from typing import Type
import pytest
# import numpy as np
from classes.Carrinho import Carrinho
from classes.Produto import Produto
from classes.Endereco import Endereco
from classes.Pedido import Pedido
from classes.PessoaFisica import PessoaFisica
import requests

"""

    Os outros testes do Pedido, são testes que requerem integração, 
    logo seram realizados em outro arquivo (arq de integração)

"""

@pytest.mark.pedido
def test_pedido_s_nada():
    with pytest.raises(TypeError) as excinfo:
        pedido = Pedido()
    assert 'missing 2' in str(excinfo)

@pytest.mark.pedido
def test_pedido_completo():
    nome = 'Sabão em Pó'
    prod_id = 45678
    prod = Produto(nome=nome,id=prod_id)
    carrinho = Carrinho()
    carrinho.adicionar_item(prod, 10)
    cep = '04726220'
    numero = 148
    end = Endereco(cep=cep,numero=numero)
    pessoa = PessoaFisica(nome='Pedro',cpf='04726220',email='pedrovazpertusi@gmail.com')
    pedido = Pedido(carrinho,pessoa)
    pedido.endereco_entrega = end
    pedido.endereco_faturamento = end
    assert f'Pessoa: {pessoa.nome}, Endereço de entrega: {end.rua}, Endereço de faturamento: {end.rua}, Produtos: {carrinho.get_item()}' == pedido.__str__()

@pytest.mark.pedido
def test_pedido_s_pessoa():
    with pytest.raises(TypeError) as excinfo:
        nome = 'Sabão em Pó'
        prod_id = 45678
        prod = Produto(nome=nome,id=prod_id)
        carrinho = Carrinho()
        carrinho.adicionar_item(prod, 10)
        cep = '04726220'
        numero = 148
        end = Endereco(cep=cep,numero=numero)
        pedido = Pedido(carrinho)
        pedido.endereco_entrega = end
        pedido.endereco_faturamento = end
    assert 'missing 1' in str(excinfo)

@pytest.mark.pedido
def test_pedido_s_carrinho():
    with pytest.raises(TypeError) as excinfo:
        cep = '04726220'
        numero = 148
        end = Endereco(cep=cep,numero=numero)
        pessoa = PessoaFisica(nome='Pedro',cpf='04726220',email='pedrovazpertusi@gmail.com')
        pedido = Pedido(pessoa)
        pedido.endereco_entrega = end
        pedido.endereco_faturamento = end
    assert 'missing 1' in str(excinfo)