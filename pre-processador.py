# importações
import re


# subprogramas

# ler arquivo do programa em c e retorna uma string com conteúdo do arquivo
def lerArquivo(nomeArq):
    arq = open(nomeArq, "r")
    string = arq.read()
    arq.close()

    return string


# Pegar os conteúdos dos includes e colocar em um arquivo chamado include
def criarArqIncl(nomeArq, vet):
    arq = open("biblioteca/" + nomeArq, "r")
    ler = arq.read()
    vet.append(ler)
    arq.close()

    return None


"""procurar o regex do include em uma string e colocar o grupo em uma lista e depois percorre a lista para a função
criarArqIncl
"""

def regexInclude(str):
    vet = []
    stringInc = ""
    reInclude = re.search(r'\#include\s\s?\<(.*)\>', str, flags=re.MULTILINE | re.DOTALL)
    if reInclude != None:
        grupo = (reInclude.group()).split("\n")
        for x in grupo:
            proc = re.search(r'<(.*)\>', x, flags=re.MULTILINE | re.DOTALL)
            acerto = proc.group(1)
            criarArqIncl(acerto, vet)  # colocar o conteúdo do include em um vetor
        for y in vet:
            stringInc += y

        return stringInc
    else:
        return None


# regex que substitui comentário por nada
def regexComentUmaLin(str):
    tiraComent = re.sub(r'\/\/(.*)', "", str)

    return tiraComent


# tira os blocos de comentários da string
def tiraComentBLoco(str):
    resul = 0
    resul2 = 0
    while (resul != -1 and resul2 != -1):
        pri = "/*"
        ult = "*/"
        temp = ""
        resul = str.find(pri)
        resul2 = str.find(ult)
        for i in range(resul, resul2 + 2):
            temp += str[i]
        str = str.replace(temp, "")
        resul = str.find(pri)
        resul2 = str.find(ult)

    return str


# acha o define e depois troca as variáveis com os valores do define e retorna a string
def regexDefine(str):
    reDefine = re.search(r'\#define\s\s?(.*)\s\s?(\d+)\n', str, flags=re.MULTILINE | re.DOTALL)
    if reDefine != None:
        grupo = (reDefine.group()).split("\n")
        for i in grupo:
            if i != "":
                pesq = re.search(r'\#define\s\s?(.*)\s\s?(\d+)', i, flags=re.MULTILINE | re.DOTALL)
                x = pesq.group(1)
                y = pesq.group(2)
                str = re.sub(r"\b{0}\b".format(x), y, str)
        str = re.sub(r'\#define\s\s?(.*)\s\s?(\d+)\n', "", str)

        return str
    else:

        return str


# remover o include da string
def removerInclude(str):
    str = re.sub(r'\#include\s\s?\<(.*)\>', "", str)

    return str


# juntar concatenar as strings do arquivo Include.txt e a string principal
def concStr(str, strInc):
    novaStr = strInc + str

    return novaStr


# remover espaço/tabulação/quebra de linha
def remETQ(str):
    str = re.sub(r'\s|\n|\t', " ", str)
    str = re.sub(r'\s\s*', " ", str)
    str = re.sub(r'\s*\(\s*', "(", str)
    str = re.sub(r'\s*\)\s*', ")", str)
    str = re.sub(r'\s*\{\s*', "{", str)
    str = re.sub(r'\s*\}\s*', "}", str)
    str = re.sub(r'\s*\;\s*', ";", str)
    str = re.sub(r'\s*\,\s*', ",", str)
    str = re.sub(r'\s*\=\s*', "=", str)
    str = re.sub(r'\s*\+\s*', "+", str)
    str = re.sub(r'\s*\-\s*', "-", str)
    str = re.sub(r'\s*\*\s*', "*", str)
    str = re.sub(r'\s*\/\s*', "/", str)
    str = re.sub(r'\s*\:\s*', ":", str)
    str = re.sub(r'\s*\-\>\s*', "->", str)
    str = re.sub(r'\s\>\s', ">", str)
    str = re.sub(r'\s\<\s', "<", str)

    return str


# tira espaço da posição inicia que sobrou depois do processo
def tirarEspacoPosIni(str):
    temp = ""
    for i in range(1, len(str)):
        temp += str[i]

    return temp


# salvar string em um arquivo
def saveStr(str):
    arq = open("Pré-processado.txt", "w")
    arq.write(str)
    arq.close()

    return str


# programa principal
arqPrin = lerArquivo("Programa.c")  # ler arquivo para ser processado
strInc = regexInclude(arqPrin)  # procrurar os arquivos includes que serão ulitizados e colocar o conteúdo em uma string
string = regexDefine(arqPrin)  # acha o define e depois troca as variáveis com os valores
string = removerInclude(string)  # remover o include da string
string = concStr(string, strInc)  # Juntar a string do include com a string principal
string = regexComentUmaLin(string)  # retirar o comentário de uma linha
string = tiraComentBLoco(string)  # retirar o comentário de um bloco
string = remETQ(string)  # remover espaço/tabulação/quebra de linha
string = tirarEspacoPosIni(string)  # tira espaço da posição inicial que sobrou depois do processo
string = saveStr(string)  # salvar string em um arquivo
