#!/usr/bin/env python3

import os

import jinja2

import pkgs.tempo.inacao as inacao
import pkgs.tempo.porvir as porvir


def sumario(duties, starting_date):
    half = inacao.semestre_atual(starting_date)
    text = 'Planos de Ensino: {}'.format(half[1])
    rule = ''
    for c in text:
        rule += '='
    title = '{}\n{}\n'.format(text, rule)
    # white spaces
    ws = ' ' * 3
    # table of contents
    toc = '.. toctree::\n{}:caption: Planos:\n{}:maxdepth: 1\n'.format(ws, ws)
    frames = ''
    for k in duties.keys():
        frames += '{}plano/{}/index.rst\n'.format(ws, k)
    token = title + '\n' + toc + '\n' + frames
    return token


def ghostwriter(duties, starting_date, quiet_days, teacher):
    os.system('rm -rf sphinx/source/plano/*')

    half = inacao.semestre_atual(starting_date)

    with open('sphinx/source/index.rst', 'w') as f:
        print(sumario(duties, starting_date), file=f)

    jj_loader = jinja2.FileSystemLoader('pkgs/plano')
    jj_environment = jinja2.Environment(loader=jj_loader)

    for k in duties.keys():
        jj_template = jj_environment.get_template('%s/index.rst' % k)
        orderliness = jj_template.render(professor=teacher, semestre=half[1])

        os.system('mkdir sphinx/source/plano/%s' % k)

        with open('sphinx/source/plano/%s/index.rst' % k, 'w') as f:
            print(orderliness, file=f)

        orig_refs = 'pkgs/plano/%s/refs.bib' % k
        dest_refs = 'sphinx/source/plano/%s/refs.bib' % k
        os.system('cp %s %s' % (orig_refs, dest_refs))

        cron = duties[k][0]
        freq = duties[k][1]

        cron_ativ = porvir.cronograma_atividades(
                starting_date,
                cron,
                freq,
                quiet_days
                )

        crono = cron_ativ[0]
        aulas = cron_ativ[1]

        with open('sphinx/source/plano/%s/cronograma.csv' % k, 'w') as f:
            for k in crono.keys():
                print('"%s", %s, "%s"' % (k, crono[k][0], crono[k][1]), file=f)

            print('"Total", %d, "---"' % aulas, file=f)

    os.system('cd sphinx && make clean && make html')
