# Calculadora de Consumo de Energia

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github&logoColor=white)
![Energia](https://img.shields.io/badge/Energia-Consumo-yellow)

## Nome e Objetivo do Sistema
**Nome:** Calculadora de Consumo de Energia  
**Objetivo:** Calcular o consumo mensal de energia elétrica de eletrodomésticos e estimar o valor da conta de luz.

## Linguagem Utilizada
- Python 3

## Fórmula Utilizada para o Cálculo
O consumo mensal é calculado pela fórmula:

\[
\text{Consumo mensal (kWh)} = \frac{\text{Potência (W)} \times \text{Horas de uso diário} \times 30}{1000}
\]

O valor estimado da conta é:

\[
\text{Valor (R\$)} = \text{Consumo mensal (kWh)} \times 0,75
\]

> Obs.: O valor R$ 0,75 por kWh é apenas um exemplo. Você pode ajustar de acordo com a tarifa local.

## Instruções para Executar o Programa
1. Abra o terminal ou PowerShell (Windows) ou Terminal (Mac/Linux).  
2. Navegue até a pasta do projeto.  
   ```bash
   cd "C:\caminho\para\calculadora_energia"
