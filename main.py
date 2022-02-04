import json
import sys

import requests

URL = "https://restcountries.com/v2/all";
URLNAME = "https://restcountries.com/v2/name/"

def requisicao(URL):
    try:
        resposta = requests.get(URL);

        if resposta.status_code == 200:
            return resposta.text
        else:
            return None;
    except Exception as error:
        print("Erro ao fazer requisição em ", URL)
        print(error);

def parsing(textoReposta):
    try: 
        return json.loads(textoReposta);
    except Exception as error:
        print("Erro ao fazer parsing.")
        print(error);

def contagemPaises():
    resposta = requisicao(URL);
    if resposta:
        listaPaises = parsing(resposta);
        if listaPaises:
            return len(listaPaises);

def listarPaises(paises):
    for pais in paises:
        print(pais['name'])
    
def mostrarPopulacao(nomePais):
    resposta = requisicao("{}{}" .format(URLNAME, nomePais));
    listaPaises = parsing(resposta);
    
    if listaPaises:
        for pais in listaPaises:
            print("{} : {}".format(pais['name'], pais['population']));
    else:
        print("País não encontrado.");

def mostrarMoeda(nomePais):
    resposta = requisicao("{}{}" .format(URLNAME, nomePais));
    listaPaises = parsing(resposta);
    
    if listaPaises:
        for pais in listaPaises:
            print("Moedas do {}".format(pais['name']))
            moedas = pais['currencies'];
            for moeda in moedas:
                print("{} - {}" .format(moeda['name'], moeda['code']))
    else:
        print("País não encontrado.");

if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print("## Bem vindo ao sistema de países. ##");
        print("Uso: python main.py <acao> <nome do país>");
        print("Ações disponíveis: contagem, moeda, população");
    else:
        argumento1 = sys.argv[1];
        
        if argumento1 == "contagem":
            print("Existem {} países no mundo." .format(contagemPaises()));
        else:
            print("Argumento Inválido.");

