# Calculadora de Consumo de Energia

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github&logoColor=white)
![Energia](https://img.shields.io/badge/Energia-Consumo-yellow)

## Nome e Objetivo do Sistema
**Nome:** Calculadora de Consumo de Energia  
**Objetivo:** Calcular o consumo mensal de energia elétrica de eletrodomésticos e estimar o valor da conta de luz.

## Linguagem Utilizada
- Python 3

## Fórmula Utilizada
O consumo mensal é calculado por:

\[
\text{Consumo mensal (kWh)} = \frac{\text{Potência (W)} \times \text{Horas de uso diário} \times 30}{1000}
\]

O valor estimado da conta é:

\[
\text{Valor (R\$)} = \text{Consumo mensal (kWh)} \times 0,75
\]

---

## Como Executar o Programa

1. **Baixe o arquivo** `medidor_de_kmh2.py` do GitHub.  
2. **Vá até a pasta** onde o arquivo foi salvo usando o **Explorador de Arquivos**.  
3. **Clique duas vezes** no arquivo para abrir (ou abra via terminal se preferir).  
4. **Digite as informações solicitadas** pelo programa:
   - Nome do aparelho (ex: Geladeira, Televisão)  
   - Potência em watts (W)  
   - Tempo médio de uso diário em horas (h)  
5. **Veja o resultado na tela**:
   - Nome do aparelho  
   - Consumo estimado (kWh)  
   - Valor aproximado da conta (R$)  

