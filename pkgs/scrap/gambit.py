#!/usr/bin/env python3

import math
import re
import time
import pandas as pd
import selenium.webdriver as webdriver
import pkgs.livro.diarios as d
import pkgs.scrap.credenciais as minhas
import pkgs.scrap.urls as qad
import pkgs.scrap.xpaths as xpaths


def diarios_de_classe():
    diarios = d.diarios
    for cod_diario in diarios.keys():
        xlsx = pd.read_excel(
                'upshot/diarios/diarios.ods',
                sheet_name='faltas_{}'.format(cod_diario),
                engine='odf'
                )
        datas = xlsx['Unnamed: 0']
        alunos = diarios[cod_diario]['alunos']
        faltas = {}
        for cod_matricula in alunos.keys():
            aluno = alunos[cod_matricula][1]
            faltas[cod_matricula] = {
                    datas[k]: round(v) for k, v in xlsx[aluno].items()
                    if math.isnan(v) is False
                    }
        diarios[cod_diario]['faltas'] = faltas
    return diarios


def missings():
    driver = webdriver.Firefox()

    driver.get(qad.urls[0])
    driver.find_element_by_name('LOGIN').send_keys(minhas.credenciais['login'])
    driver.find_element_by_name('SENHA').send_keys(minhas.credenciais['senha'])
    driver.find_element_by_name('Submit').click()

    time.sleep(6)
    driver.find_element_by_link_text('Meus Diários').click()

    diarios = diarios_de_classe()

    for cod_diario in diarios.keys():
        driver.find_element_by_xpath(xpaths.xpaths[3] % cod_diario).click()
        datas = list(diarios[cod_diario]['conteudo'].keys())[36:38]
        for data in datas:
            cntd = diarios[cod_diario]['conteudo'][data]
            qtd = '2'

            faltas = diarios[cod_diario]['faltas']

            codigos_de_matricula = [
                    x for x in faltas.keys() if data in faltas[x].keys()
                    ]
            str_data = re.sub(r'/', r'%2F', data)
            try:
                aula_dada = driver.find_element_by_xpath(
                        xpaths.xpaths[4] % str_data
                        )
                aula_dada.click()
                input_field_n_aulas = driver.find_element_by_name('N_AULAS')
                input_field_n_aulas.clear()
                input_field_n_aulas.send_keys(qtd)
                input_field_conteudo = driver.find_element_by_name('CONTEUDO')
                input_field_conteudo.clear()
                input_field_conteudo.send_keys(cntd)
                for cod_matricula in codigos_de_matricula:
                    input_field = driver.find_element_by_name(
                            'N_FALTAS_%s' % cod_matricula
                            )
                    input_field.clear()
                    input_field.send_keys(qtd)

                time.sleep(3)
                driver.find_elements_by_xpath(
                        '//*[@id="btnSalvar"]'
                        )[0].click()
            except aula_dada:
                driver.find_element_by_name(
                        'DT_AULA_MINISTRADA'
                        ).send_keys(data)
                driver.find_element_by_name('N_AULAS').send_keys(qtd)
                driver.find_element_by_name('CONTEUDO').send_keys(cntd)
                for cod_matricula in codigos_de_matricula:
                    driver.find_element_by_name(
                            'N_FALTAS_%s' % cod_matricula
                            ).send_keys(qtd)

                time.sleep(3)
                driver.find_elements_by_xpath(
                        '//input[contains(@value, "Inserir")]'
                        )[1].click()

        time.sleep(3)
        driver.find_element_by_link_text('Meus Diários').click()

    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="Image1"]').click()

    time.sleep(3)
    driver.close()


def main():
    print(diarios_de_classe())


if __name__ == '__main__':
    main()
