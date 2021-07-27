<!-- PROJECT LOGO -->
<br />
<p align="center">
  <img src="../images/logo.png" alt="UFES" width="340" height="240">

  <h3 align="center">Trabalho 1.2</h3>

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

<div style="text-align: justify"> Experimentar a implementação de sistemas cliente/servidor por meio de _middleware_ RPC _(Remote Procedure Call)_ aos conceitos de paralelismo. Comparar o tempo de execução com diferentes quantidades de processos. Avaliar a necessidade de controle de concorrência quando há múltiplos clientes e um único servidor. </div>

### Feito com

* [Python 3](https://www.python.org/about/)
* [xmlrpc](https://docs.python.org/3/library/xmlrpc.html)
* [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)

## Executando

O script pode ser executado seguindo estes passos:

**Obs: Os passos a seguir foram escritos para sistema Linux.**

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
2. Entre na pasta Trabalho-1.2
  ```sh
  cd Trabalho-1.2
  ```

## Uso

Este programa pode ser executado na porta pré-determinada ou determinada pelo usuário.

1. Porta pré-determinada (8000)
  ```sh
  python3 main.py
  ```
2. Porta determinada pelo usuário
  ```sh
  python3 main.py --port your-port-here
  ```

## Módulos

O pacote `src` contém os módulos auxiliares desenvolvidos, são eles:

1. [client.py](https://github.com/ugiete/PPD-2021-1/blob/master/Trabalho-1.2/src/client.py), módulo de operações do cliente;

2. [server.py](https://github.com/ugiete/PPD-2021-1/blob/master/Trabalho-1.2/src/server.py), módulo de conexão e registro de funções do servidor;

3. [utils.py](https://github.com/ugiete/PPD-2021-1/blob/master/Trabalho-1.2/src/utils.py), módulo que contém funções auxiliares para gerar uma lista aleatória e plotar gráficos.

## Resultados

<div style="text-align: justify"> Foram utilizados os valores de 1, 2, 4 e 8 processos durante os testes. Para cada instância de processos foram avaliados diferentes quantidades de valores a serem incluídos e recuperados na tabela, variando entre 100.000, 500.000 e 1.000.000. Apenas um teste foi realizado por quantidade de valores por processo. Os resultados estão apresentados na tabela abaixo. </div>

- 1 Cliente
  - 100k - 57.77926158905029
  - 500k - 293.5026035308838
  - 1M - 612.4989190101624

<center>

  | Num Processos | Quant. Valores (m) |    Tempo Exec.    |
  |:-------------:|:------------------:|:-----------------:|
  |      1        |      100.000       |     57.7793 s     |
  |               |      500.000       |    293.5026 s     |
  |               |     1.000.000      |    612.4990 s     |
  |      2        |      100.000       |     21.0353 s     |
  |               |      500.000       |     21.0353 s     |
  |               |     1.000.000      |     21.0353 s     |
  |      4        |      100.000       |     21.0353 s     |
  |               |      500.000       |     21.0353 s     |
  |               |     1.000.000      |     21.0353 s     |
  |      8        |      100.000       |     21.0353 s     |
  |               |      500.000       |     21.0353 s     |
  |               |     1.000.000      |     21.0353 s     |

</center>


<div style="text-align: justify"> Python possui o Python Global Interpreter (GIL) que é um lock mutex que permite apenas uma thread esteja sendo executada por vez no interpretador.

Embora em programas que utilizem uma única thread o GIL é interessante para gerenciamento de memória, em situações de paralelismo pode ser um gargalo na execução como vemos nas figuras, onde com o aumento do número de threads praticamente não há melhora no tempo de execução individual de cada uma e acaba por aumentar o tempo total de execução por conta dos overheads gerados. </div>

## Grupo

Felippe Barbosa Mozer - 2016102801  
Leonardo Silva Ugiete - 2016101234  
Lucas Quintino Frinhani - 2016101227
