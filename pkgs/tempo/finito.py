#!/usr/bin/env python3


def ano_bissexto(ano):
    if ano % 100 == 0 and ano % 400 == 0:
        bissexto = 1
    elif ano % 4 == 0:
        bissexto = 1
    else:
        bissexto = 0
    return bissexto


# códigos utilizados para se representar aos meses do ano (standard):
#
#  jan | fev | mar | abr | mai | jun | jul | ago | set | out | nov | dez
# -----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----
#  1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12
def qtd_dias_do_mes_de(ano, mes):
    if mes in (4, 6, 9, 11):
        qtd_dias = 30
    elif mes == 2:
        if ano_bissexto(ano) == 0:
            qtd_dias = 28
        else:
            qtd_dias = 29
    else:
        qtd_dias = 31
    return qtd_dias


def deslocador_do_dia(ano, mes, dia, shift):
    if shift > 0:
        while shift > 0:
            if dia + shift > qtd_dias_do_mes_de(ano, mes):
                aux = qtd_dias_do_mes_de(ano, mes) - dia + 1
                dia = 1
                if mes < 12:
                    mes += 1
                else:
                    mes = 1
                    ano += 1
            else:
                aux = shift
                dia += shift
            shift -= aux
    else:
        while shift < 0:
            if dia + shift < 1:
                aux = dia
                if mes > 1:
                    mes -= 1
                    dia = qtd_dias_do_mes_de(ano, mes)
                else:
                    ano -= 1
                    mes = 12
                    dia = 31
            else:
                aux = -shift
                dia += shift
            shift += aux
    return (ano, mes, dia)


def correcao_mod_7(codigo):
    if codigo == 0:
        dia_da_semana = 7
    else:
        dia_da_semana = codigo
    return dia_da_semana


# códigos utilizados para se representar aos dias da semana:
#
#  dom | seg | ter | qua | qui | sex | sab
# -----+-----+-----+-----+-----+-----+-----
#  1   | 2   | 3   | 4   | 5   | 6   | 7
def dia_da_semana_de_primeiro_de_janeiro(ano):
    dia_da_semana = 2
    dia_da_semana += 5*((ano - 1) % 4)
    dia_da_semana += 4*((ano - 1) % 100)
    dia_da_semana += 6*((ano - 1) % 400)
    dia_da_semana %= 7
    dia_da_semana_de_primeiro_de_janeiro = correcao_mod_7(dia_da_semana)
    return dia_da_semana_de_primeiro_de_janeiro


def qtd_dias_desde_primeiro_de_janeiro_deste_ano(ano, mes, dia):
    if mes == 1:
        qtd_dias = dia - 1
    else:
        i = 1
        qtd_dias = 0
        while i < mes:
            qtd_dias += qtd_dias_do_mes_de(ano, i)
            i += 1
        qtd_dias += dia - 1
    return qtd_dias


def dia_da_semana(ano, mes, dia):
    codigo = dia_da_semana_de_primeiro_de_janeiro(ano)
    codigo += qtd_dias_desde_primeiro_de_janeiro_deste_ano(ano, mes, dia)
    codigo %= 7
    dia_da_semana = correcao_mod_7(codigo)
    return dia_da_semana


def data_da_pascoa(ano):
    e_00 = ano % 19
    e_01 = ano // 100
    e_02 = ano % 100
    e_03 = e_01 // 4
    e_04 = e_01 % 4
    e_05 = (e_01 + 8) // 25
    e_06 = (e_01 - e_05 + 1) // 3
    e_07 = (19*e_00 + e_01 - e_03 - e_06 + 15) % 30
    e_08 = e_02 // 4
    e_09 = e_02 % 4
    e_10 = (32 + 2*e_04 + 2*e_08 - e_07 - e_09) % 7
    e_11 = (e_00 + 11*e_07 + 22*e_10) // 451
    mes = (e_07 + e_10 - 7*e_11 + 114) // 31
    dia = (e_07 + e_10 - 7*e_11 + 114) % 31 + 1
    return (ano, round(mes), round(dia))


# Esta função será útil para que possamos comparar datas segundo a relação de
# odem dos números inteiros
def data_como_um_inteiro(ano, mes, dia):
    ano_str = str(ano)
    if mes < 10:
        mes_str = str('%02d' % mes)
    else:
        mes_str = str(mes)
    if dia < 10:
        dia_str = str('%02d' % dia)
    else:
        dia_str = str(dia)
    data_concat_str = ano_str + mes_str + dia_str
    data_concat_int = int(data_concat_str)
    return data_concat_int
