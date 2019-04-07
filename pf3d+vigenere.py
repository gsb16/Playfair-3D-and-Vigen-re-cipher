import sys
import vigenere
import playfair3d as pf3d

def cifraTexto(texto, chave):
    texto = pf3d.cifraTexto(texto, chave)
    return vigenere.cifraTexto(texto, chave)

def decifraTexto(texto, chave):
    texto = vigenere.decifraTexto(texto, chave)
    return pf3d.decifraTexto(texto, chave)

if len(sys.argv) >= 4:
    arquivo = open(sys.argv[2], "r")
    if len(sys.argv) == 5:
        saida = open(sys.argv[4], "w+")
    else:
        saida = sys.stdout

    if sys.argv[1] == '-c':
        saida.write(cifraTexto(arquivo.read(), sys.argv[3]))
    if sys.argv[1] == '-d':
        saida.write(decifraTexto(arquivo.read(), sys.argv[3]))
