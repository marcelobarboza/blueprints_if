#!/usr/bin/env python3

xpaths = (
    #
    # xpaths[0]:
    #
    #   numero do diario
    #
    '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[1]/td[2]/font',
    #
    # xpaths[1]:
    #
    #   codigo da turma
    #
    '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[1]/td[6]',
    #
    # xpaths[2]:
    #
    #   disciplina
    #
    '/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[3]/td[2]',
    #
    # xpaths[3]:
    #
    #   faltas
    #
    '//a[contains(@href, "3066&MODO=FALTAS&COD_PAUTA=%s")]',
    #
    # xpaths[4]:
    #
    #   editar aula dada
    #
    '//div/a[contains(@href, "DT_AULA_MINISTRADA=%s")]/img',
)
