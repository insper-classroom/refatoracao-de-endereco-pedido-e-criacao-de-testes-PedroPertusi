from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.Carrinho import Carrinho
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento
import pytest
import copy

"""

    Alguns dos outros testes já foram testadis no integracao_1 e no próprio pytest da classe

"""

# Caso de uso em que se busca uma pessoa e um produto
# Cria uma pessoa 
pessoa1 = PessoaFisica('524.222.452-6', 'tiago@email.com', 'Carlos')
end1 = Endereco('08320330', 430)
end2 = Endereco('04546042', 300)
sabonete = Produto("0010342967", "Sabonete")

@pytest.mark.integracao_2
def test_busca_nome_pessoa_e_produto():
    pessoas = PessoaFisica.busca_nome('Carlos') #quando criar um novo preciso
    if len(pessoas) > 0:
        pessoa = pessoas[0]  #Pega a primeira pessoa
    assert pessoa == pessoa1
    produtos = Produto.busca_nome("sabon")
    if len(produtos) > 0: 
         produto = produtos[0]
    assert produto == sabonete


@pytest.mark.integracao_2
def test_pagamento():
    carrinho = Carrinho()
    carrinho.adicionar_item(sabonete)
    pedido = Pedido(carrinho=carrinho,pessoa=pessoa1)
    pag = Pagamento(pedido)
    pag.processa_pagamento()
    if pag.pagamento_aprovado:
        pedido.status = Pedido.PAGO 
    assert pag.pedido.status == 2