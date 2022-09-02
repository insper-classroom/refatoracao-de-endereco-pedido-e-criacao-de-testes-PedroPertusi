import pytest
# import numpy as np
from classes.PessoaFisica import PessoaFisica
import requests

@pytest.mark.pessoa_fisica
def test_criancao_pessoa_fisica_completa():
    cpf = '04726220'
    email = 'pedro@gmail.com'
    nome = 'Pedro Pertusi'
    pessoa = PessoaFisica(cpf=cpf, email=email, nome=nome)
    assert pessoa.cpf == cpf and pessoa.email == email and pessoa.nome == nome

@pytest.mark.pessoa_fisica
def test_criancao_pessoa_fisica_s_cpf():
    with pytest.raises(TypeError) as exc:
        email = 'pedro@gmail.com'
        nome = 'Pedro Pertusi'
        pessoa = PessoaFisica(email=email, nome=nome)
    assert "missing 1 required" in str(exc)

@pytest.mark.pessoa_fisica
def test_criancao_pessoa_fisica_s_email():
    with pytest.raises(TypeError) as exc:
        cpf = '04726220'
        nome = 'Pedro Pertusi'
        pessoa = PessoaFisica(cpf=cpf, nome=nome)
    assert "missing 1 required" in str(exc)

@pytest.mark.pessoa_fisica
def test_criancao_pessoa_fisica_completa_s_nome():
    cpf = '04726220'
    email = 'pedro@gmail.com'
    pessoa = PessoaFisica(cpf=cpf, email=email)
    assert pessoa.cpf == cpf and pessoa.email == email and pessoa.nome == 'Visitante'

@pytest.mark.pessoa_fisica
def test_pessoa_fisica_busca_nome():
    cpf = '04726220'
    email = 'pedro@gmail.com'
    nome = 'Pedro Pertusi'
    pessoa = PessoaFisica(cpf=cpf, email=email, nome=nome)
    result = PessoaFisica.busca_nome(nome)
    assert pessoa.nome == result[0].nome and pessoa.email == result[0].email and pessoa.cpf == result[0].cpf

@pytest.mark.pessoa_fisica
def test_pessoa_fisica_busca_nome_visitante():
    cpf = '04726220'
    email = 'pedro@gmail.com'
    pessoa = PessoaFisica(cpf=cpf, email=email)
    result = PessoaFisica.busca_nome('Visitante')
    assert 'Visitante' == result[0].nome and pessoa.email == result[0].email and pessoa.cpf == result[0].cpf

@pytest.mark.pessoa_fisica
def test_pessoa_fisica_busca_nome_inexistente():
    cpf = '04726220'
    email = 'pedro@gmail.com'
    nome = 'Pedro'
    pessoa = PessoaFisica(cpf=cpf, email=email, nome=nome)
    result = PessoaFisica.busca_nome('João')
    assert result == []