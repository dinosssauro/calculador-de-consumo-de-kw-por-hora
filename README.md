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

> Obs.: O valor R$ 0,75 por kWh é apenas um exemplo. Pode ser ajustado conforme a tarifa local.

## Instruções Detalhadas para Executar o Programa

Siga estes passos:

1. **Certifique-se de que o Python 3 está instalado**
   - Para verificar, abra o terminal ou PowerShell e digite:
     ```bash
     python --version
     ```
   - Deve aparecer algo como `Python 3.11.x`.

2. **Abra o terminal ou PowerShell**
   - **Windows:** clique na pasta do projeto, segure **Shift** + clique direito → "Abrir PowerShell aqui"  
   - **Mac/Linux:** abra o Terminal e navegue até a pasta do projeto com o comando `cd`

3. **Navegue até a pasta do projeto**
   - Exemplo Windows:
     ```powershell
     cd "C:\Users\SeuUsuario\Documents\calculadora_energia"
     ```
   - Exemplo Mac/Linux:
     ```bash
     cd "/Users/SeuUsuario/Documents/calculadora_energia"
     ```

4. **Execute o programa**
   ```bash
   python medidor_de_kmh2.py
