#!/usr/bin/env python3

import pkgs.tempo.finito as finito


# frequencia_das_aulas:
#
#   é uma lista de pares ordenados do tipo (ds, qa), em que ds representa o dia
#   da semana e qa representa a quantidade de aulas dadas no dia ds.
#
#   alguns exemplos:
#
#   1) [(2, 1), (5, 1)] significa uma aula na segunda, uma aula na quinta;
#   2) [(3, 2), (4, 1)] significa duas aulas na terca, uma aula na quarta;
#   3) [(2, 1), (4, 1), (6, 1)] significa uma aula na segunda, uma aula na
#      quarta e uma aula na sexta.
def data_da_proxima_aula(data_atual, frequencia_das_aulas, days_off):
    ano = data_atual[0]
    mes = data_atual[1]
    dia = data_atual[2]
    dias_uteis = [x[0] for x in frequencia_das_aulas]
    N = len(frequencia_das_aulas)
    while finito.dia_da_semana(ano, mes, dia) not in dias_uteis:
        data_auxiliar = finito.deslocador_do_dia(ano, mes, dia, 1)
        ano = data_auxiliar[0]
        mes = data_auxiliar[1]
        dia = data_auxiliar[2]
    data_da_proxima_aula = 0
    dia_semana = finito.dia_da_semana(ano, mes, dia)
    while dias_uteis[data_da_proxima_aula] < dia_semana:
        data_da_proxima_aula += 1
    while (ano, mes, dia) in days_off:
        shift = finito.correcao_mod_7(
                (
                    dias_uteis[(data_da_proxima_aula + 1) % N]
                    - dias_uteis[data_da_proxima_aula]
                    ) % 7
                )
        data_auxiliar = finito.deslocador_do_dia(ano, mes, dia, shift)
        ano = data_auxiliar[0]
        mes = data_auxiliar[1]
        dia = data_auxiliar[2]
        data_da_proxima_aula = (data_da_proxima_aula + 1) % N
    return (ano, mes, dia)


def qtd_aulas_consecutivas(data, frequencia, days_off):
    dia_semana = finito.dia_da_semana(data[0], data[1], data[2])
    prox_aula = data_da_proxima_aula(data, frequencia, days_off)
    if data == prox_aula:
        qtd_aulas_consec = [x for x in frequencia if x[0] == dia_semana][0]
    else:
        qtd_aulas_consec = (dia_semana, 0)
    return qtd_aulas_consec


def aulas_aa_frente(data, frequencia, days_off, N):
    data_de_hoje = data
    qtd_aulas = 0
    while qtd_aulas <= N:
        data_prox_aula = data_da_proxima_aula(
                data_de_hoje,
                frequencia,
                days_off
                )
        qtd_aulas += qtd_aulas_consecutivas(
                data_prox_aula,
                frequencia,
                days_off
                )[1]
        data_de_hoje = finito.deslocador_do_dia(
                data_prox_aula[0],
                data_prox_aula[1],
                data_prox_aula[2],
                1
                )
    return data_prox_aula


def cronograma_atividades(inicio_semestre, cronograma, frequencia, days_off):
    crono = {}
    data = data_da_proxima_aula(inicio_semestre, frequencia, days_off)
    qtd_aulas = 0
    for key in cronograma.keys():
        carga = (cronograma[key][0], cronograma[key][1])
        dd = str('%02d/%02d/%d' % (data[2], data[1], data[0]))
        crono[dd] = (2*carga[1], carga[0])
        qtd_aulas += carga[1]
        data = aulas_aa_frente(data, frequencia, days_off, 1)
    return (crono, 2*qtd_aulas)
