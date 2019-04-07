alfabeto="\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_` "

def cifraLetra(letra, chave):
    l = alfabeto.index(letra.upper())
    c = alfabeto.index(chave.upper())
    return alfabeto[(l+c) % len(alfabeto)]

def decifraLetra(letra, chave):
    l = alfabeto.index(letra.upper())
    c = alfabeto.index(chave.upper())
    return alfabeto[(l-c) % len(alfabeto)]

def cifraTexto(text, key):
    fechado = ""
    for i, c in enumerate(key):
        cf = cifraLetra(text[i], c)
        fechado += cf

    for i, c in enumerate(text[len(key):]):
        cf = cifraLetra(c, text[i])
        fechado += cf

    return fechado

def decifraTexto(text, key):
    aberto = ""
    for i, c in enumerate(key):
        ca = decifraLetra(text[i], c)
        aberto += ca

    for i, c in enumerate(text[len(key):]):
        ca = decifraLetra(c, aberto[i])
        aberto += ca
    return aberto
