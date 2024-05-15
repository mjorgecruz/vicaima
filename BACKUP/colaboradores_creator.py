import pandas as pd

import chardet

rawdata = open('02_BD_colaboradores.csv', 'rb').read()
result = chardet.detect(rawdata)
encoding = result['encoding']

df = pd.read_csv('02_BD_colaboradores.csv', encoding=encoding, sep=',')
df = df[['Nº colaborador', 'Nome', 'Apelido','Departamento', 'Função',
'Data de Admissão', 'Grupo Funcional:']]
df.to_csv('colaboradores.csv', index=False)

df = pd.read_csv('02_BD_colaboradores.csv', encoding=encoding, sep=',')
df = df[['Nº colaborador', 'Nº avaliador \n(= nº colaborador)', 'Diretor Unidade\n(= nº colaborador)']]
df.to_csv('correlacoes.csv', index=False)

