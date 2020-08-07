#!/usr/bin/env python3

import pkgs.tempo.inacao as nc
import pkgs.scrap.stratagem as st

import pkgs.plano.algebra_linear_matematica.crono
import pkgs.plano.algebra_moderna_matematica.crono
import pkgs.plano.logica_sistemas_informacao.crono
import pkgs.plano.variaveis_complexas_matematica.crono

import pkgs.papel.ghostwriter as gw
import pkgs.papel.scribbler as sc


def main():
    professor = 'Marcelo Barboza'
    inicio_das_aulas = (2020, 2, 3)
    ano = inicio_das_aulas[0]

    ferias_0 = nc.dias_anergicos((ano, 1, 2), (ano, 1, 24))
    semana_0 = nc.dias_anergicos((ano, 1, 27), (ano, 1, 31))
    ferias_1 = nc.dias_anergicos((ano, 7, 1), (ano, 7, 26))
    semana_1 = nc.dias_anergicos((ano, 7, 24), (ano, 7, 25))

    frds_urt = nc.feriados_urutai(ano)

    feriados = {
            k: frds_urt[k] for k in frds_urt.keys()
            if frds_urt[k][1][1] != 10
            }

    recessos = nc.recessos_urutai(ano, feriados)

    # em nossa instituicao o mes de outubro nao segue qualquer padrao no que
    # diz respeito a feriados, entao...
    dias_quietos_outubruo = {
            20201012: ('Semana do saco cheio', (2020, 10, 12)),
            20201013: ('Semana do saco cheio', (2020, 10, 13)),
            20201014: ('Semana do saco cheio', (2020, 10, 14)),
            20201015: ('Semana do saco cheio', (2020, 10, 15)),
            20201016: ('Semana do saco cheio', (2020, 10, 16)),
            }

    # dias sem aulas (quietos), ordenados cronologicamente
    dias_sem_aulas = {
            **feriados,
            **recessos,
            **dias_quietos_outubruo,
            **ferias_0,
            **semana_0,
            **ferias_1,
            **semana_1
            }

    dias_quietos = [
            dias_sem_aulas[k][1] for k in sorted(dias_sem_aulas.keys())
            ]

    encargos = {
            'algebra_linear_matematica':
            (
                pkgs.plano.algebra_linear_matematica.crono.crono,
                [(4, 1), (5, 1)],
                '20201.01MAT22N.3N'
                ),
            'algebra_moderna_matematica':
            (
                pkgs.plano.algebra_moderna_matematica.crono.crono,
                [(2, 1), (5, 1)],
                '20201.01MAT22N.5N'
                ),
            'logica_sistemas_informacao':
            (
                pkgs.plano.logica_sistemas_informacao.crono.crono,
                [(3, 1), (4, 1)],
                '20201.01SDI20M.3M'
                ),
            'variaveis_complexas_matematica':
            (
                pkgs.plano.variaveis_complexas_matematica.crono.crono,
                [(2, 1), (3, 1)],
                '20201.01MAT22N.7N'
                )
            }

    resultado = st.stratagem(encargos, inicio_das_aulas, dias_quietos)
    sc.scribbler(resultado)

    gw.ghostwriter(
            encargos,
            inicio_das_aulas,
            dias_quietos,
            professor
            )


if __name__ == '__main__':
    main()
