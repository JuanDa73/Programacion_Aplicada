MarcasCarros={'Renault':['logan','stepway','twingo'],'Toyota':('prado','runner'),'chevrolet':'tracker'}#usar listas si cambian tuplas no
print(MarcasCarros['Renault'])#imprime los modelos de renault
print(MarcasCarros['Toyota'])#imprime los modelos de toyota

MarcasMoto={'auteco':{'pulsar':('180','200','250')},'suzuki':'gixxer'}
print(MarcasMoto['auteco'])#imprimo los cilindrajes del modelo pulsar
print(MarcasMoto)#llamo a toda la definicion de MarcasMoto
print(MarcasMoto.keys())
print(MarcasMoto.values())
print("auteco"in MarcasMoto)
print(MarcasCarros.get('ferrari','no se encuentra'))
print(len(MarcasCarros))