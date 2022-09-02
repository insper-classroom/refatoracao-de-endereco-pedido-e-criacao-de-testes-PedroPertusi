from unittest.mock import patch
import pytest
# import numpy as np
from classes.Endereco import Endereco
import requests

@pytest.mark.endereco
def test_criacao_objeto_apenas_cep_rua():
    cep = '04726220'
    numero = 148
    end = Endereco(cep=cep,numero=numero)
    assert end.rua == 'Rua Luís Correia de Melo' and end.estado == 'SP' and end.cidade == 'São Paulo'

@pytest.mark.endereco
def test_criacao_objeto_completo():
    cep = '04726220'
    numero = 148
    rua = 'Luís Correia de Melo'
    estado = 'SP'
    cidade = 'São Paulo'
    complemento = 'Apt 133 Torre 5'
    end = Endereco(cep=cep,numero=numero,rua=rua,estado=estado,cidade=cidade,complemento=complemento)
    assert end.rua == rua and end.estado == estado and end.cidade == cidade and end.complemento == complemento and end.cep == cep and end.numero == numero

@pytest.mark.endereco
def test_consultar_cep_como_str():
    cep = '04726220'
    end = Endereco.consultar_cep(cep=cep)
    assert end['logradouro'] == 'Rua Luís Correia de Melo' and end['localidade'] == 'São Paulo' and end["uf"] == 'SP'
    
@pytest.mark.endereco
def test_consultar_cep_como_int():
    cep = 4726220
    end = Endereco.consultar_cep(cep=cep)
    assert end['logradouro'] == 'Rua Luís Correia de Melo' and end['localidade'] == 'São Paulo' and end["uf"] == 'SP'

@pytest.mark.endereco
def test_consultar_cep_com_menos_digitos():
    cep = '6220'
    end = Endereco.consultar_cep(cep=cep)
    assert end == False

@pytest.mark.endereco
def test_consultar_cep_mais_digitos():
    cep = '6223465760'
    end = Endereco.consultar_cep(cep=cep)
    assert end == False

@pytest.mark.endereco
def test_consultar_cep_invalido():
    cep = '99999999'
    end = Endereco.consultar_cep(cep=cep)
    assert end == False

@pytest.mark.endereco
def test_consultar_cep_nao_str_ou_int():
    cep = ['9','9','9']
    end = Endereco.consultar_cep(cep=cep)
    assert end == False

@pytest.mark.erro_connection
def test_connection_error():
    cep = '04726220'
    with pytest.raises(requests.exceptions.ConnectionError) as excinfo:
        end = Endereco.consultar_cep(cep=cep)
    assert "Max retries exceeded with url" in str(excinfo.value)