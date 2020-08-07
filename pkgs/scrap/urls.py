#!/usr/bin/env python3

base_url = 'https://academico.ifgoiano.edu.br/qacademico/index.asp?t='

urls = (
    '{}1000'.format(base_url),
    '{}3066&MODO=FALTAS&COD_PAUTA=%s&ETAPA=1&N_ETAPA=N'.format(base_url),
    '{}3066&COD_PAUTA=%s&N_ETAPA=N&MODO='.format(base_url)
)
