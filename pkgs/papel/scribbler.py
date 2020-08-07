#!/usr/bin/env python3

import pandas as pd


def scribbler(pair_of_dicts):
    diarios = pair_of_dicts[0]
    tabelas = pair_of_dicts[1]

    with open('pkgs/livro/diarios.py', 'w') as f:
        print('diarios = %s' % diarios, file=f)

    with pd.ExcelWriter(
            'upshot/diarios/diarios.xlsx',
            engine='openpyxl') as xlsx:
        for k in tabelas.keys():
            # aba: identificação
            tabelas[k]['identidade'].to_excel(
                    xlsx,
                    sheet_name='id_%s' % k
                    )
            # aba: controle de faltas
            tabelas[k]['faltas'].to_excel(
                    xlsx,
                    sheet_name='faltas_%s' % k
                    )
            # aba: controle do conteúdo
            tabelas[k]['conteudo'].to_excel(
                    xlsx,
                    sheet_name='conteudos_%s' % k
                    )
            # aba: discentes matriculados
            tabelas[k]['alunos'].to_excel(
                    xlsx,
                    sheet_name='discentes_%s' % k
                    )
