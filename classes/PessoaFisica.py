#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''

    lista_pessoas = []    

    def __init__(self, cpf, email, nome='Visitante'):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.__enderecos = {}
        PessoaFisica.lista_pessoas.append(self)

    # escolher o estilo de retorno
    
    def __str__(self):
        return self.nome + ' ' + self.email + ' ' + self.cpf

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.__enderecos.setdefault(apelido_endereco,end)

    def remover_endereco(self, apelido_endereco):
        pass

    def get_endereco(self, apelido_endereco):
        pass

    def listar_enderecos(self):
        return self.__enderecos
    
    def busca_nome(nome):
        achados = []
        for pessoa in PessoaFisica.lista_pessoas:
            if nome.lower() in pessoa.nome.lower():
                achados.append(pessoa)
        return achados

    