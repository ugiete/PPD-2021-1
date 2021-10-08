<!-- PROJECT LOGO -->
<br />
<p align="center">
  <img src="../images/logo.png" alt="UFES" width="340" height="240">

  <h3 align="center">Trabalho 2</h3>

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

Experimentar a implementação de sistemas cliente/servidor por meio de _middleware_ RPC _(Remote Procedure Call)_ aliado aos conceitos de paralelismo. Comparar o tempo de execução com diferentes quantidades de processos. Avaliar a necessidade de controle de concorrência quando há múltiplos clientes e um único servidor.

Complemento ao [Trabalho 1.3](https://github.com/ugiete/PPD-2021-1/tree/master/Trabalho-1.3). Consiste da adição e remoção dinâmica de clientes do servidor, além de alguns ajustes necessários a este complemento.

### Recursos

* [Python 3](https://www.python.org/about/)
* [Mosquitto](https://mosquitto.org/)
* [paho-mqtt](https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php)

## Executando

O script pode ser executado seguindo estes passos:

**Obs: Os passos a seguir foram escritos para sistema Linux.**

### Hardware

O programa foi testado utilizando uma máquina com as seguintes especificações:

* Processador de 8 núcleos e 16 threads
* Memória de 32 GB e 3200 MHz

O passo a passo para execução mostrado aqui podem variar de acordo com as especificações de hardware de diferentes máquinas.

### Instalação

1. Clone este repositório
  ```sh
  git clone https://github.com/ugiete/PPD-2021-1.git
  ```
2. Entre na pasta Trabalho-2
  ```sh
  cd Trabalho-2
  ```

## Uso

Este programa é executado por padrão em um loop infinito de postagens para os nós com um único cliente, no entanto o número de iterações máximas pode ser definido assim como o número de clientes. Contudo, com mais de um cliente as mensagens são duplicadas, já que todos estão assinando o mesmo tópico.

1. 1 cliente e loop infinito de execução
  ```sh
  python3 main.py
  ```
2. Definir número de clientes e iterações máximas
  ```sh
  python3 main.py --clients NC --iterMax IT
  ```

## Módulos

O pacote `src` contém os módulos auxiliares desenvolvidos, são eles:

1. [client.py](https://github.com/ugiete/PPD-2021-1/blob/master/Trabalho-1.2/src/client.py), módulo de operações do cliente;

2. [nodes.py](https://github.com/ugiete/PPD-2021-1/blob/master/Trabalho-1.2/src/nodes.py), módulo de operações dos nós da DHT;

3. [utils.py](https://github.com/ugiete/PPD-2021-1/blob/master/Trabalho-1.2/src/utils.py), módulo que contém funções auxiliares para gerar um array de clientes e de nós.

## Grupo

Felippe Barbosa Mozer - 2016102801  
Leonardo Silva Ugiete - 2016101234  
Lucas Quintino Frinhani - 2016101227