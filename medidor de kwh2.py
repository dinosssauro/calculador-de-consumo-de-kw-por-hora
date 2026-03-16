#entrada de informacoes 
aparelho =input("qual aparelho deseja medir o consumo ?")
watts = float(input("qual  a potencia do aparelho em (w)?"))
tempo = float(input("qual tempo medio de uso diario em (h)?"))

#cauculo da formula 

consumoM = watts*tempo*30/1000
gasto = consumoM*0.75
#saida de informacao
print(f"consumo estimado:{consumoM:.2f} kwh")
print(f"vaor por mes:{gasto:.2f}")
print(f"aparelho:{aparelho}")
#impede que a janela feche
input("presione enter para sair")
