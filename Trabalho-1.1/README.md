<!-- PROJECT LOGO -->
<br />
<p align="center">
  <img src="../images/logo.png" alt="UFES" width="340" height="240">

  <h3 align="center">Trabalho 1.1</h3>

  <p align="center">
    Felippe Barbosa Mozer
    <br />
    Leonardo Silva Ugiete
    <br />
    Lucas Quintino Frinhani
    <br />
  </p>
</p>

## Sobre

Experimentar o paralelismo por meio de processos e threads na ordenação de um
vetor de grandes dimensões. Comparar o tempo de execução da tarefa de ordenação
de vetores com diferentes quantidades de processos ou threads.

### Feito com

* [Python 3](https://www.python.org/about/)
* [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
* [threading](https://docs.python.org/3/library/threading.html)

## Executando

O script de ordenação pode ser executado seguindo estes passos. Os passos foram escritos para sistema Linux.

### Hardware

O programa foi testado utilizando uma máquina com as seguintes especificações:

* Processador de 8 núcleos e 16 threads
* Memória de 32 GB e 3200 MHz

Os resultados mostrados aqui podem variar de acordo com as especificações de hardware de diferentes máquinas.

### Instalação

1. Clone este repositório
  ```sh
  git clone https://github.com/ugiete/PPD-2021-1.git
  ```
2. Entre na pasta Trabalho-1.1
  ```sh
  cd Trabalho-1.1
  ```

## Uso

Este programa pode ser executado tanto em modo de paralelismo por **processos** quanto por **threads**.

1. Paralelismo com processos
  ```sh
  python3 main.py
  ```
2. Paralelismo com threads
  ```sh
  python3 main.py --thread
  ```

## Resultados

Foram utilizados os valores de 1, 2, 4 e 8 threads/processos durante os testes e para cada um destas instâncias foram realizados 10 testes, a lista que foir ordenada possui 50M de elementos que são números inteiros randomicamente gerados.

| Num Threads | Média Tempo Exec. | Desvio Padrão Tempo Exec. |
|:-----------:|:-----------------:|:-------------------------:|
|      1      |     20.5488 s     |          0.2856 s         |
|      2      |     39.3205 s     |          0.4757 s         |
|      4      |     55.5700 s     |          0.6703 s         |
|      8      |     70.6508 s     |          0.7966 s         | 

| Num Processos | Média Tempo Exec. | Desvio Padrão Tempo Exec. |
|:-------------:|:-----------------:|:-------------------------:|
|      1        |     21.0353 s     |          0.5227 s         |
|      2        |     40.8518 s     |          0.5871 s         |
|      4        |     57.6770 s     |          0.9950 s         |
|      8        |     74.3596 s     |          2.7458 s         | 

<img src="images/threads.jpeg" alt="Threads Média" height="240">  
<br />
<img src="images/processos.jpeg" alt="Processos Desvio" height="240">

Python possui o Python Global Interpreter (GIL) que é um lock mutex que permite apenas uma thread esteja sendo executada por vez no interpretador.

Embora em programas que utilizem uma única thread o GIL é interessante para gerenciamento de memória, em situações de paralelismo pode ser um gargalo na execução como vemos nas figuras, onde com o aumento do número de threads praticamente não há melhora no tempo de execução individual de cada uma e acaba por aumentar o tempo total de execução por conta dos overheads gerados.

## Grupo

Felippe Barbosa Mozer - 2016102801  
Leonardo Silva Ugiete - 2016101234  
Lucas Quintino Frinhani - 2016101227
