import csv

file = open('.\Archive_manipulation\desafio-ibge.csv')
reader = csv.DictReader(file)

for row in reader:
 print(f"4: {row['nome_orige']}, 8: {row['cod_destin']}")

 file.close()
