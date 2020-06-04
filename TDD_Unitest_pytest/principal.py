from src.leilao.dominio import Avaliador, Lance, Leilao, Usuario

gui = Usuario('Gui')
yuri = Usuario('Yuri')

lance_do_yuri =Lance(yuri, 100.00)
lance_do_gui =Lance(gui, 150.00)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_yuri)
leilao.lances.append(lance_do_gui)

for lance in leilao.lances:
    print(f'O Usuario {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance for de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')
