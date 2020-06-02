import re

padrao = "[0-9]{4,5}-?[0-9]{4}"
# Vamos testar esse padrão.
texto =  "Meu número para contato é 2633-5723"
retorno = re.search(padrao,texto)
print(retorno.group())

# -----------------------------------

frase1 = "podemos marcar de sair sabado 23h"
frase2 = "acho que quinta 21h é a melhor hora para a gente ir lá"
frase3 = "terca 19h é um bom momento para sairmos"

padrao = "[a-z]{1,20}[ ][0-9]{1,2}[h]"

retorno = re.search(padrao,frase1)
print(retorno.group())

retorno = re.search(padrao,frase2)
print(retorno.group())

retorno = re.search(padrao,frase3)
print(retorno.group())
