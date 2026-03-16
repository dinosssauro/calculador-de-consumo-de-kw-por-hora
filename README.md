# Calculadora de Consumo de Energia

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github&logoColor=white)
![Energia](https://img.shields.io/badge/Energia-Consumo-yellow)

## Descrição do Projeto
Este projeto é um sistema simples para calcular o **consumo de energia elétrica de eletrodomésticos**.  
O objetivo é fornecer uma estimativa de **kWh consumidos por mês** e o **valor aproximado da conta de luz**.

## Linguagem Utilizada
- Python 3

## Fórmula de Cálculo
O consumo mensal é calculado usando a fórmula:

\[
\text{Consumo mensal (kWh)} = \frac{\text{Potência (W)} \times \text{Horas de uso diário} \times 30}{1000}
\]

O valor estimado da conta é calculado multiplicando o consumo pelo preço do kWh:

\[
\text{Valor (R\$)} = \text{Consumo mensal (kWh)} \times 0,75
\]

> Observação: O valor de R$ 0,75 por kWh é um exemplo, podendo ser ajustado conforme a tarifa local.

## Como Executar
1. Certifique-se de ter o **Python 3** instalado em seu computador.
2. Abra o terminal ou prompt de comando.
3. Navegue até a pasta do projeto.
4. Execute o programa com o comando:

```bash
python calculadora_consumo.py
