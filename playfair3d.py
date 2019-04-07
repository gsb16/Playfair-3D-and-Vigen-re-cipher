alfabeto="\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_` "

def coordParaIndice(linha, coluna, camada):
    return (linha + coluna * 4 + camada * 16)

def indiceParaCoord(i):
    coluna = i % 4
    linha = i / 4 % 4
    camada = i / 16
    return (coluna, linha, camada)

def trataTexto(texto_inter):
    texto_inter = texto_inter.upper()
    tratado = ""
    texto = ""
    i = 0

    for c in texto_inter:
        if c in alfabeto:
            texto += c

    while i < len(texto)-2:
        trigrama = texto[i:i+3]
        tratado += trigrama[0]
        if trigrama[0] == trigrama[1] or trigrama[0] == trigrama[2]:
            tratado += "XY"
            i += 1
        elif trigrama[1] == trigrama[2]:
            tratado += trigrama[1] + "X"
            i += 2
        else:
            tratado += trigrama[1:]
            i += 3

    tratado += texto[i:]

    if len(tratado) % 3 == 2:
        tratado += "X"
    if len(tratado) % 3 == 1:
        tratado += "XY"

    return tratado

def geraCubo(chave):
    cubo_inicial = alfabeto
    chave = chave.upper()
    cubo = ""

    for k in chave:
        if k not in cubo and k in cubo_inicial:
            cubo += k
    for d in cubo_inicial:
        if d not in chave:
            cubo += d
    return cubo

def cifraTrigrama(tri, cubo):
    c1 = indiceParaCoord(cubo.index(tri[0]))
    c2 = indiceParaCoord(cubo.index(tri[1]))
    c3 = indiceParaCoord(cubo.index(tri[2]))

    cc1 = cubo[coordParaIndice(c1[0], c2[1], c3[2])]
    cc2 = cubo[coordParaIndice(c2[0], c3[1], c1[2])]
    cc3 = cubo[coordParaIndice(c3[0], c1[1], c2[2])]

    return cc1+cc2+cc3

def decifraTrigrama(tri, cubo):
    c1 = indiceParaCoord(cubo.index(tri[0]))
    c2 = indiceParaCoord(cubo.index(tri[1]))
    c3 = indiceParaCoord(cubo.index(tri[2]))

    cd1 = cubo[coordParaIndice(c1[0], c3[1], c2[2])]
    cd2 = cubo[coordParaIndice(c2[0], c1[1], c3[2])]
    cd3 = cubo[coordParaIndice(c3[0], c2[1], c1[2])]

    return cd1+cd2+cd3

def cifraTexto(texto, chave):
    cifrado = ""
    cubo = geraCubo(chave)
    texto = trataTexto(texto)
    for i in range (0, len(texto), 3):
        cifrado += cifraTrigrama(texto[i:i+3], cubo)
    return cifrado

def decifraTexto(texto, chave):
    decifrado = ""
    cubo = geraCubo(chave)

    for i in range (0, len(texto), 3):
        decifrado += decifraTrigrama(texto[i:i+3], cubo)
    return decifrado
