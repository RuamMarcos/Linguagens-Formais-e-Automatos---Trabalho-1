Simulador de Autômato Finito Determinístico em Python
Este repositório contém a implementação de um Autômato Finito Determinístico (AFD) como parte de uma atividade acadêmica. O script em Python simula o comportamento de um autômato específico, processando cadeias de caracteres para determinar se pertencem ou não à linguagem definida.

Autor: Ruam Marcos Maciel dos Santos

O Autômato
O AFD implementado neste projeto é representado pelo seguinte diagrama de estados:

Fundamentação Teórica
A lógica principal do simulador baseia-se na função de transição estendida, denotada por δ̂(q, w), que descreve o estado em que o autômato se encontrará após processar uma palavra w a partir de um estado q. A função é definida indutivamente:

Base: Para uma palavra vazia (ε), o autômato permanece no estado atual.

δ
^
 (q,ϵ)=q
$$$$

Indução: Para uma palavra w que pode ser decomposta em uma sub-palavra x e um símbolo final a (ou seja, w = xa), a função é definida como:

δ
^
 (q,xa)=δ( 
δ
^
 (q,x),a)
$$$$
$$A implementação em Python utiliza recursividade para espelhar essa definição formal.