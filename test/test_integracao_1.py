from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.Carrinho import Carrinho
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento
import pytest
import copy

 
pessoa1 = PessoaFisica('524.222.452-6', 'tiago@email.com', 'Carlos' )
end1 = Endereco('08320330', 430)
end2 = Endereco('04546042', 300)
sabonete = Produto("0010342967", "Sabonete")

@pytest.mark.integracao_1
def test_adicionar_endereco_e_get_endereco_em_pessoa():
    pessoa1.adicionar_endereco('casa', end1)
    end_pessoa = pessoa1.get_endereco('casa')
    assert end_pessoa.rua == end1.rua

@pytest.mark.integracao_1
def test_pessoa_listar_enderecos():
    pessoa1.adicionar_endereco('casa', end1)
    pessoa1.adicionar_endereco('trabalho', end2)
    list_end_pessoa = pessoa1.listar_enderecos()
    assert end1 in list_end_pessoa.values() and end2 in list_end_pessoa.values()

@pytest.mark.integracao_1
def test_integra_pessoa_endereco_carrinho_em_pedido_completo():
    carrinho = Carrinho()
    carrinho.adicionar_item(sabonete, 10)
    pedido = Pedido(carrinho,pessoa1)
    pedido.endereco_entrega = copy.deepcopy(end1)
    pedido.endereco_faturamento = copy.deepcopy(end2)
    assert f'Pessoa: {pessoa1.nome}, Endereço de entrega: {end1.rua}, Endereço de faturamento: {end2.rua}, Produtos: {carrinho.get_item()}' == str(pedido)