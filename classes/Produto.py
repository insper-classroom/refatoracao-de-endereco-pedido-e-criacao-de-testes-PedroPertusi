#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------



class Produto:

    lista_produtos = []
    def __init__(self, id, nome=''):
        self.id = id
        self.nome = nome
        Produto.lista_produtos.append(self)

    def get_id(self):
        return self.id

    def busca_nome(nome):
        achados = []
        for produto in Produto.lista_produtos:
            if nome.lower() in produto.nome.lower():
                achados.append(produto)
        return achados
