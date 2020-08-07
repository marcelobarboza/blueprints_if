#!/Usr/bin/env python3

import pkgs.tempo.finito as finito


def feriados_urutai(ano):
    psc = finito.data_da_pascoa(ano)

    s_crnvl = finito.deslocador_do_dia(ano, psc[1], psc[2], -48)
    t_crnvl = finito.deslocador_do_dia(ano, psc[1], psc[2], -47)
    q_crnvl = finito.deslocador_do_dia(ano, psc[1], psc[2], -46)

    px = finito.deslocador_do_dia(ano, psc[1], psc[2], -2)
    cc = finito.deslocador_do_dia(ano, psc[1], psc[2], 60)

    nacionais = {
            finito.data_como_um_inteiro(ano, 1, 1): (
                'Confraternização Universal',
                (ano, 1, 1)
                ),
            finito.data_como_um_inteiro(s_crnvl[0], s_crnvl[1], s_crnvl[2]): (
                'Recesso: Carnaval',
                s_crnvl
                ),
            finito.data_como_um_inteiro(t_crnvl[0], t_crnvl[1], t_crnvl[2]): (
                'Carnaval',
                t_crnvl
                ),
            finito.data_como_um_inteiro(q_crnvl[0], q_crnvl[1], q_crnvl[2]): (
                'Quarta-feira de Cinzas',
                q_crnvl
                ),
            finito.data_como_um_inteiro(px[0], px[1], px[2]): (
                'Paixão de Cristo',
                px
                ),
            finito.data_como_um_inteiro(ano, 4, 21): (
                'Tiradentes',
                (ano, 4, 21)
                ),
            finito.data_como_um_inteiro(ano, 5, 1): (
                'Dia Mundial do Trabalho',
                (ano, 5, 1)
                ),
            finito.data_como_um_inteiro(cc[0], cc[1], cc[2]): (
                'Corpus Christi',
                cc
                ),
            finito.data_como_um_inteiro(ano, 9, 7): (
                'Independência do Brasil',
                (ano, 9, 7)
                ),
            finito.data_como_um_inteiro(ano, 10, 12): (
                'Nossa Senhora Aparecida',
                (ano, 10, 12)
                ),
            finito.data_como_um_inteiro(ano, 10, 12): (
                'Dia do Servidor Público',
                (ano, 10, 28)
                ),
            finito.data_como_um_inteiro(ano, 11, 2): (
                'Finados',
                (ano, 11, 2)
                ),
            finito.data_como_um_inteiro(ano, 11, 15): (
                'Proclamação da República',
                (ano, 11, 15)
                ),
            finito.data_como_um_inteiro(ano, 12, 25): (
                    'Natal',
                    (ano, 12, 25)
                    ),
            finito.data_como_um_inteiro(ano, 12, 24): (
                    'Véspera de Natal',
                    (ano, 12, 24)
                    ),
            finito.data_como_um_inteiro(ano, 12, 31): (
                    'Véspera de Ano Novo',
                    (ano, 12, 31)
                    ),
            }

    estaduais = {}

    municipais = {
            finito.data_como_um_inteiro(ano, 8, 6): (
                'Senhor Bom Jesus',
                (ano, 8, 6)
                ),
            finito.data_como_um_inteiro(ano, 12, 15): (
                'Aniversário de Urutaí',
                (ano, 12, 15)
                ),
            }

    feriados = {**nacionais, **estaduais, **municipais}
    feriados_ordenados = {k: feriados[k] for k in sorted(feriados.keys())}

    return feriados_ordenados


def recessos_urutai(ano, feriados):
    recessos = {}

    psc = finito.data_da_pascoa(ano)

    data_rec_px_cristo = finito.deslocador_do_dia(psc[0], psc[1], psc[2], -3)

    ano_px = data_rec_px_cristo[0]
    mes_px = data_rec_px_cristo[1]
    dia_px = data_rec_px_cristo[2]

    data_rec_px_cristo_int = finito.data_como_um_inteiro(
            ano_px,
            mes_px,
            dia_px
            )

    recessos[data_rec_px_cristo_int] = (
            'Recesso: Paixão de Cristo',
            data_rec_px_cristo
            )

    # feriados = feriados_urutai(ano)

    dias_mortos = [
            k for k in feriados.keys()
            if finito.dia_da_semana(
                feriados[k][1][0],
                feriados[k][1][1],
                feriados[k][1][2]
                ) in [3, 5]
            ]

    for key in dias_mortos:
        feriado = feriados[key][0]
        data = feriados[key][1]

        ano_data = data[0]
        mes_data = data[1]
        dia_data = data[2]

        dia_semana = finito.dia_da_semana(ano_data, mes_data, dia_data)

        if dia_semana == 3:
            shift = -1
        elif dia_semana == 5:
            shift = 1

        data_recesso = finito.deslocador_do_dia(
                ano_data,
                mes_data,
                dia_data,
                shift
                )

        ano_rec = data_recesso[0]
        mes_rec = data_recesso[1]
        dia_rec = data_recesso[2]

        data_recesso_int = finito.data_como_um_inteiro(
                ano_rec,
                mes_rec,
                dia_rec
                )

        if ano_rec == ano and data_recesso_int not in feriados.keys():
            recessos[data_recesso_int] = (
                    'Recesso: %s' % feriado,
                    data_recesso
                    )

            recessos_ordenados = {
                    k: recessos[k] for k in sorted(recessos.keys())
                    }

    return recessos_ordenados


def dias_anergicos(data_0, data_1):
    ano = data_0[0]
    mes = data_0[1]
    dia = data_0[2]

    inic_int = finito.data_como_um_inteiro(ano, mes, dia)

    ANO = data_1[0]
    MES = data_1[1]
    DIA = data_1[2]

    term_int = finito.data_como_um_inteiro(ANO, MES, DIA)

    if inic_int < term_int:
        dias_anergicos = {}
        data = data_0
        i = 1
        data_int = finito.data_como_um_inteiro(ano, mes, dia)
        while data_int < term_int:
            dias_anergicos[data_int] = ('Dia %d' % i, data)
            data = finito.deslocador_do_dia(data[0], data[1], data[2], 1)
            i += 1
            data_int = finito.data_como_um_inteiro(data[0], data[1], data[2])
    return dias_anergicos


def semestre_atual(inicio_das_aulas):
    ano = inicio_das_aulas[0]
    mes = inicio_das_aulas[1]
    dia = inicio_das_aulas[2]

    inicio_das_aulas_int = finito.data_como_um_inteiro(ano, mes, dia)
    segundo_semestre_int = finito.data_como_um_inteiro(ano, 8, 1)

    if inicio_das_aulas_int < segundo_semestre_int:
        ano_semestre_0 = '{}_1'.format(ano)
        ano_semestre_1 = '{}/1'.format(ano)
    else:
        ano_semestre_0 = '{}_2'.format(ano)
        ano_semestre_1 = '{}/2'.format(ano)

    return (ano_semestre_0, ano_semestre_1)
