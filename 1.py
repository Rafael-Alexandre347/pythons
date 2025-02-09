'''Uma empresa de logística precisa otimizar suas entregas. Ela recebe uma lista de pacotes com os seguintes dados: (código, peso, cidade de destino). O objetivo é distribuir os pacotes em caminhões, respeitando as seguintes regras:

Cada caminhão suporta no máximo 200 kg.
Os pacotes devem ser agrupados por cidade de destino sempre que possível.
Se um pacote exceder o limite do caminhão, ele deve ser enviado separadamente.

Código	Peso (kg)	Cidade de Destino
101	    50	        São Paulo
102	    80	        Rio de Janeiro
103	    120	        São Paulo
104	    40	        São Paulo
105	    70	        Rio de Janeiro
106	    90	        Curitiba
107	    30      	Belo Horizonte
108	    110     	São Paulo
109	    60      	Rio de Janeiro
110	    95      	Curitiba
111	    45      	Belo Horizonte
112	    100	        Porto Alegre
113	    55      	Porto Alegre
114	    85      	São Paulo
115	    70      	Rio de Janeiro'''

pacotes = [
    (101, 50, "São Paulo"),
    (102, 80, "Rio de Janeiro"),
    (103, 120, "São Paulo"),
    (104, 40, "São Paulo"),
    (105, 70, "Rio de Janeiro"),
    (106, 90, "Curitiba"),
    (107, 30, "Belo Horizonte"),
    (108, 110, "São Paulo"),
    (109, 60, "Rio de Janeiro"),
    (110, 95, "Curitiba"),
    (111, 45, "Belo Horizonte"),
    (112, 100, "Porto Alegre"),
    (113, 55, "Porto Alegre"),
    (114, 85, "São Paulo"),
    (115, 70, "Rio de Janeiro")
]

cidades = {}

for pacote in pacotes:
    codigo, peso, cidade = pacote

    if cidade not in cidades:
        cidades[cidade] = []

        cidades[cidade].append(pacote)

print(cidades)