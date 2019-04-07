# Playfair3D + Vigenère

## Autores:
- Gabriel de Souza Barreto
- Guilherme Bastos de Oliveira

## O que é:
A Playfair 3D é uma versão da cifra Playfair onde os caracteres são organizados em um cubo 4x4x4 e indexados por um sistema de coordenadas baseadas na linha, coluna e camada.  
O sistema Playfair 3D + Vigenère é a aplicação da cifra Playfair 3D sobre um texto claro e em seguida a aplicação da cifra de Vigenère.

Uma descrição detalhada pode ser encontrada no arquivo **playfair3d.md**

## Execução:
    python pf3d+viginere.py <op> <arq_entrada> <chave> <arq_saida>

__op__: '-c' para cifrar texto, '-d' para decifrar texto_inter  
__arq_entrada__: arquivo a ser cifrado/decifrado  
__chave__: chave para cifrar/decifrar texto de arquivo_entrada  
__arq_saida__ _(opcional)_: se informada, arquivo onde será impresso o texto de saida, caso contrário é usada a saída padrão  
