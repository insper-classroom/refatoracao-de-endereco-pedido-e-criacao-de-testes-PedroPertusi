#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.PessoaFisica import PessoaFisica

# Esta classe deverá permitir a inserção de items, bem como a atualização da quantidade de
# produtos em um item

class Carrinho:

    def __init__(self):
        # Chave é o id do Produto e o Valor é a quantidade desse item no carrinho
        self.__itens = {}

    def adicionar_item(self, item:Produto, qtd=None):
        
        id = item.get_id()
        
        # Implemente a adição do item no dicionário
        self.__itens.setdefault(id,0)
        if qtd != None:
            self.__itens[id] += qtd
        

    def remover_item(self, item:Produto):
        id = item.get_id()
        del self.__itens[id]

    def get_item(self):
        return self.__itens

