#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re




class Pedido:
    EM_ABERTO = 1
    PAGO = 2
    def __init__(self, carrinho: Carrinho, pessoa: PessoaFisica):
        self.endereco_entrega = None
        self.endereco_faturamento = None
        self.pessoa = pessoa
        self.produtos = carrinho
        self.status = False

    def __str__(self):
        return f'Pessoa: {self.pessoa.nome}, Endereço de entrega: {self.endereco_entrega.rua}, Endereço de faturamento: {self.endereco_faturamento.rua}, Produtos: {self.produtos.get_item()}'

    