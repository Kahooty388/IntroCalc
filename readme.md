# INTROCALC

## COMO JOGAR

O **IntroCalc** é roguelike de matemtica em que o jogador utiliza uma calculadora com usos limitados para resolver problemas.

A cada rodada:

1. Um número alvo é gerado.
2. O jogador recebe uma quantidade limitada de usos totais, alem dos usos limitaods de cada botão (cada botão começa o jogo com 2 usos e mantem de rodada para rodada, essa quatidade podendo ser incrementada na loja).
3. O jogador deve montar uma expressão usando os botões da calculadora para chegar exatamente ao alvo.
4. Ao pressionar `=`, a expressão é calculada.
5. Se o resultado for igual ao alvo, a rodada é vencida.
6. Quanto mais usos sobrarem, maior será a recompensa de dinheiro da rodada.
7. Depois da vitória, aparece uma tela mostrando o dinheiro obtido na rodada, os usos restantes, os juros e o pagamento final. (os juros de dão R$1, a cada R$5, dando no maximo R$5)
8. Depois disso, o jogador vai para a loja.

A dificuldade vai aumentando com as rodadas. Nas primeiras rodadas, os alvos são números inteiros menores. Conforme a partida contuinua, os alvos ficam maiores e, nas rodadas mais avançadas, também podem ser números decimais.

## LOJA

Depois de vencer uma rodada, o jogador irá a loja.

Na loja, os botões da calculadora podem ser comprados para aumentar a quantidade de usos disponíveis para eles. Cada botão tem preço inicial de  R$2 e sobe e, R$1 cada vez que são comprados, isso para incentivar variedade de botoes comprados.

## CONTROLES

**Mouse:**

* Clicar nos botões da calculadora.
* Comprar melhorias na loja.
* Interagir com os botões dos menus.
* Interagir com os botões da tela de Game Over.

**Enter:**

* Verificar a expressão durante a partida.

**Tela de Game Over:**

* **Tente de novo:**
* **Fechar jogo:**

## OBJETIVO

O objetivo é completar o máximo de rodadas possível, usando os recursos da calculadora de maneira eficiente e administrando o dinheiro recebido entre as rodadas.

O jogo não tem final determinado, podendo ir teoricamente infinitamente

## DIFICULDADES ENCONTRADAS


A maior dificuldade foi fazer a calculadora funcionar de verdade. No começo, os botões apenas eram desenhados e registravam que haviam sido pressionados. Depois foi necessário implementar a criação das expressões, o cálculo dos resultados e a comparação com o número-alvo.

Também tive problemas com o tratamento das expressões. Foi necessário impedir que o jogador colocasse operadores seguidos e criasse expressões inválidas. O uso do `eval()` para calcular as expressões também apresentou alguns problemas que precisaram ser corrigidos.

A implementação do fullscreen também deu bastante trabalho. Inicialmente o jogo era desenhado diretamente na tela, mas depois foi necessário adaptar as posições e tamanhos dos elementos de acordo com o tamanho da tela para que o jogo funcionasse corretamente em diferentes resoluções.

Os efeitos sonoros também deram alguns problemas. Alguns sons pareciam tocar atrasados e outros eram reproduzidos várias vezes quando deveriam tocar apenas uma vez. Foi necessário usar flags para controlar quando determinados sons deveriam ser executados.

Além disso, foram encontrados vários pequenos bugs visuais durante o desenvolvimento, como elementos sendo desenhados incorretamente, problemas de posicionamento, textos que não apareciam e problemas com o ícone do jogo.

## EXPERIÊNCIA DE DESENVOLVIMENTO

No começo, programar o jogo parecia relativamente simples. A ideia inicial era criar uma calculadora, colocar alguns botões e fazer as expressões funcionarem. Porém, conforme o projeto foi crescendo, ficou mais difiícil, mas tambem achei mais divertido.

Foi necessário aprender a trabalhar com diferentes estados de jogo, eventos, colisões de mouse, fontes, superfícies, efeitos sonoros, música, transições, fullscreen, animações e objetos, mas tudo se tornou mais simples apos passar dois dias assistindo o tutorial de pygame do clear code.

No geral, foi uma experiência divertida. toveram vezes que bugs foram bem frustantes, principalmente quando uma solução parecia funcionar e acabava criando outro problema. Mas, acabei resolvendo e agora o jogo está pronto

Eu não diria que fazer o jogo foi extremamente difícil, mas também não foi tão simples quanto parece no começo. Criar uma tela e fazer um botão funcionar é relativamente fácil. O que realmente aumenta a dificuldade é juntar todas as partes e fazer com que elas funcionem juntas sem criar novos bugs.

Também me arrependo um pouco de não fazer mais arquivos e classes, pois acabou tudo ficando no calc.py, quando poderia ter feito um game_over.py e um shop.py

O projeto mostrou que fazer um jogo exige bastante organização e atenção aos detalhes, além de programação.

## DIÁRIO DE DESENVOLVIMENTO

### Dia 1

Criei o esqueleto do `main.py` e o esqueleto inicial dos botões. No começo, não parecia que seria muito difícil.

### Dia 2

Criei o esqueleto do `calc.py`.

### Dia 3

Fiz o desenho básico da calculadora na tela e implementei os botões sendo pressionados. Eles ainda não faziam nada além de mostrar no terminal que haviam sido apertados.

### Dia 4

As expressões básicas começaram a funcionar.

### Dia 5

Restava apenas um erro. Fora isso, o loop principal de gameplay com a calculadora já estava completo.

### Dia 6

Criei o menu e deixei ele funcional. Nesse ponto, só faltava fazer a loja para ter uma partida completa. Depois disso, faltariam apenas o polimento, as instruções, as transições de tela e a música.

### Dia 7

Implementei as transições entre os estados e a tela de vitória da rodada. Depois disso, faltava apenas fazer a loja.

### Dia 8

A loja foi feita e o gameplay ficou pronto.

### Dia 9

Corrigi bugs visuais, coloquei efeitos sonoros e música. Depois disso, ficaram apenas alguns ajustes relacionados ao `eval()` e a documentação do jogo.

### Dia 10

Bugs resolvidos e finalizados, jogo pronto

## CONCLUSÃO

O IntroCalc começou como uma ideia simples de um roguelike de calculadora e foi evoluiu durante o desenvolvimento até eu tranforma-lo num jogo completo baseado em rodadas, gerenciamento de recursos e resolução de expressões matemáticas.

Durante o desenvolvimento, aprendi muito sobre Pygame e POO, o que achei bem divertido e gostaria de fazer denovo.

Apesar das dificuldades e dos bugs encontrados durante o processo, o desenvolvimento foi uma experiência positiva e divertida, que me ensinou bastante sobre python e pygame, já que mal havia programado em python antes, apenas em C.

##PS

Eu sei que esse jogo tem muita coisa em parecido com o calculate it que está em early acess na steam, mas como era para um projeto da faculdade, e descobri da existencia do calculate it depois que comecei, decidi fazer esse jogo mesmo.

Credito ao Louis F e ao LocalThunk pela minha música de gameplay (Balatro Main Theme) e pela Nintendo pelo SFX de game over (Vem de Breath of the Wild)
