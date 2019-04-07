# Playfair 3D + Vigenère

## Autores:
- Gabriel de Souza Barreto
- Guilherme Bastos de Oliveira

## Resumo:
A Playfair 3D é uma versão da cifra Playfair onde os caracteres são organizados em um cubo 4x4x4 e indexados por um sistema de coordenadas baseadas na linha, coluna e camada.
O sistema Playfair 3D + Vigenère é a aplicação da cifra Playfair 3D sobre um texto claro e em seguida a aplicação da cifra de Vigenère.

## Motivação:
Quando a cifra Playfair foi apresentada em sala, foi mencionada a possibilidade da sua implementação com três coordenadas. Com isso, não seria mais necessária a junção i/j,
mais caracteres poderiam ser usados e o número bem maior (mais que o dobro) de caracteres possíveis aumentaria muito as possibilidades a serem avaliadas numa tentativa de
quebra por força bruta. Isso gerou curiosidade de como seria o resultado dessa alteração no modelo, principalmente adicionando a etapa de cifra adicional por Vigenère.
Com isso, foi decidido fazer essa implementação e avaliar quais seriam as eventuais diferenças em relação à cifra original.

# Cifra Playfair 3D
## Organização dos caracteres:
### Camada 0:
```
" # $ %
& ' ( )
* + , -
. / 0 1
```

### Camada 1:
```
2 3 4 5
6 7 8 9
: ; < =
> ? @ A
```

### Camada 2:
```
B C D E
F G H I
J K L M
N O P Q
```

### Camada 3:
```
R S T U
V W X Y
Z [ \ ]
^ _ `  
```

## Cifração:
Os caracteres são organizados em um cubo 4x4x4, onde primeiro são inseridos os caracteres únicos da chave e depois é completado com os caracteres da organização base de
maneira que os caracteres já presentes na chave não são repetidos.

O texto claro é interpretado em trigramas.

Em um trigrama, se a primeira letra é igual a a segunda ou a ultima: insere "XY" após primeira letra. Se a segunda letra é igual a ultima: insere "X" após a segunda letra

Caso sobre um caractere isolado no último trigrama, adiciona "XY". Caso sobrem 2 caracteres, adiciona " ".

Cada trigrama do texto claro é mapeado para um trigrama do texto cifrado, da seguinte maneira:

    ca = caractere aberto
    cc = caractere cifrado

    1ºcc = {linha(1ca), coluna(2ca), camada(3ca))}
    2ºcc = {camada(1ca), linha(2ca), coluna(3ca))}
    3ºcc = {coluna(1ca), camada(2ca), linha(3ca))}

## Decifração:
Cada trigrama do texto claro é mapeado para um trigrama do texto cifrado, da seguinte maneira:

    cc = caractere cifrado
    cd = caractere decifrado

    1ºdc = {linha(1ca), camada(2ca), coluna(3ca)}
    2ºdc = {coluna(1ca), linha(2ca), camada(3ca)}
    3ºdc = {camada(1ca), coluna(2ca), linha(3ca)}

# Cifra Vigenère
O texto claro é cifrado da seguinte maneira:

Para cada caractere i do texto claro até acabar a chave é realizado um "shift" no caractere com deslocamento referente ao caractere i da chave.

Após a aplicação da chave, cada caractere seguinte é cifrado por um caractere do texto claro, seguindo assim até o final do texto.

Para decifrar basta realizar o mesmo processo com "shift" para o lado inverso.


# Funcionamento Playfair 3D + Vigenère
## Cifração:
0. Dado texto aberto TA
1. Define chave C
2. Cifra TA com C usando Playfair 3D
3. Cifra o produto do passo 2 com Vigenère e C gerando o texto cifrado

## Decifração:
0. Dados texto cifrado TC e chave C
1. Decifra TC com chave C sobre Vigenère
2. Decifra produto do passo 1 com chave C usando Playfair 3D

## Conclusão:
 Ao planejar esse modelo, foram percebidas algumas características interessantes e tomadas decisões para dificultar qualquer criptoanálise:
  - Com o sistema de 3 coordenadas, não é necessário tratar de forma especial um trigrama que seja adjacente na mesma camada tanto na horizontal quanto na vertical;
  - Ao preencher o cubo a partir de uma posição arbitrária da tabela ASCII e incluir o símbolo de espaço no fim, tornamos a quebra por força bruta ainda mais
  difícil, já que seria necessário incluir essas variações nos testes;
  - Com os 64 símbolos diferentes e usando uma chave de 6 caracteres, existe quase 54 bilhões de possibilidades para teste;
  - A cifra adicional com Vigenère atrapalha qualquer criptoanálise, já que elimina qualquer padrão que porventura pudesse ser percebido apenas com a PlayFair 3D;
  - Ao incluir os espaços para cifrar, fica impossível saber onde as palavras começam e terminam. Além disso, os números e outros símbolos estratégicos estão
  incluídos, o que vai mascarar a presença de outros símbolos e evitar que seja percebida alguma informação importante.
