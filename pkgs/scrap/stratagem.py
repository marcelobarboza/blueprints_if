#!/usr/bin/env python3

import re
import time

import pandas
import selenium.webdriver

import pkgs.tempo.porvir as porvir

import pkgs.scrap.credenciais as credenciais
import pkgs.scrap.urls as urls
import pkgs.scrap.xpaths as xpaths


def stratagem(duties, starting_date, quiet_days):

    marionete = selenium.webdriver.Firefox()

    marionete.get(urls.urls[0])

    marionete.find_element_by_name('LOGIN').send_keys(
            credenciais.credenciais['login']
            )

    marionete.find_element_by_name('SENHA').send_keys(
            credenciais.credenciais['senha']
            )

    marionete.find_element_by_name('Submit').click()

    time.sleep(6)

    marionete.find_element_by_link_text('Meus Diários').click()

    atalhos_para_meus_diarios = [
            x.get_attribute('href')
            for x in marionete.find_elements_by_xpath(
                '//a[contains(@href, "MODO=FALTAS")]')
            ]

    diarios = {}
    tabelas = {}

    for atalho in atalhos_para_meus_diarios:
        time.sleep(3)

        marionete.get(atalho)

        cod_diario = marionete.find_element_by_xpath(xpaths.xpaths[0]).text
        cod_equipe = marionete.find_element_by_xpath(xpaths.xpaths[1]).text
        disciplina = marionete.find_element_by_xpath(xpaths.xpaths[2]).text

        diarios[cod_diario] = {}

        diarios[cod_diario]['turma'] = cod_equipe
        diarios[cod_diario]['disciplina'] = disciplina

        dados_brutos_alunos = [
                (x.get_attribute('href'), x.get_attribute('text'))
                for x in marionete.find_elements_by_xpath(
                    '//a[contains(@href, "COD_MATRICULA")]'
                    )
                ]

        dados_refinados_alunos = [
                (re.search(r'COD_MATRICULA=([0-9]+)', x[0])[1], x[1])
                for x in dados_brutos_alunos
                ]

        M = len(dados_refinados_alunos)

        alunos_matrs = [
                dados_refinados_alunos[i] for i in range(M)
                if i % 2 == 0
                ]

        alunos_nomes = [
                dados_refinados_alunos[i] for i in range(M)
                if i % 2 == 1
                ]

        diarios[cod_diario]['alunos'] = {}

        N = M // 2

        for i in range(N):
            x = alunos_matrs[i]
            y = alunos_nomes[i]
            diarios[cod_diario]['alunos'][x[0]] = (
                    x[1], y[1], x[0] == y[0]
                    )

        disciplina = [
                k for k in duties.keys()
                if duties[k][2] == cod_equipe
                ][0]

        cron = duties[disciplina][0]
        freq = duties[disciplina][1]

        cron_ativ = porvir.cronograma_atividades(
                starting_date,
                cron,
                freq,
                quiet_days
                )

        diarios[cod_diario]['conteudo'] = {
                k: v[1] for k, v in cron_ativ[0].items()
                }

        tabelas[cod_diario] = {}

        # tabela: identidade
        tabela_identidade = pandas.Series(
                {'disciplina': disciplina, 'turma': cod_equipe},
                name='identidade'
                )

        tabelas[cod_diario]['identidade'] = tabela_identidade

        # tabela: faltas
        datas_das_aulas = list(diarios[cod_diario]['conteudo'].keys())

        tabela_faltas = pandas.DataFrame(
                [
                    ['' for y in alunos_nomes]
                    for data in datas_das_aulas
                    ],
                index=datas_das_aulas,
                columns=[y[1] for y in alunos_nomes],
                )

        tabelas[cod_diario]['faltas'] = tabela_faltas

        # tabela: conteúdo
        tabela_conteudo = pandas.Series(
                diarios[cod_diario]['conteudo'],
                name='conteúdo'
                )

        tabelas[cod_diario]['conteudo'] = tabela_conteudo

        # tabela: alunos
        tabela_alunos = pandas.DataFrame(
                list(diarios[cod_diario]['alunos'].values()),
                index=diarios[cod_diario]['alunos'].keys(),
                columns=['matrícula', 'nome', 'match']
                )

        tabelas[cod_diario]['alunos'] = tabela_alunos

        time.sleep(3)

        # deve ficar dentro do loop cuja variavel eh atalho
        marionete.back()

    time.sleep(3)

    marionete.find_element_by_xpath('//*[@id="Image1"]').click()

    time.sleep(3)

    marionete.close()

    return (diarios, tabelas)
