#!/usr/bin/env python3

import pkgs.prova.algebra_moderna_matematica.p1_rnd as r1
import pkgs.papel.texnician as tex
import pkgs.livro.diarios as d


def main():
    diretorio = 'pkgs/prova/algebra_moderna_matematica/'
    arquivo = 'p1_raw.tex'
    payload = {
            'local_e_data': 'Urutaí, 22 de Julho de 2020',
            'docente': 'Prof. Marcelo Barboza',
            'prova': '1',
            'disciplina': 'Álgebra Moderna',
            'curso': 'Licenciatura em Matemática'
            }
    diarios = d.diarios
    fvc = diarios['139676']['alunos']
    for k in fvc.keys():
        nome_partido = fvc[k][1].split()
        primeiro_nome = nome_partido[0]
        ultimo_nome = nome_partido[-1]
        string_nome = '\\texttt{%s %s}' % (primeiro_nome, ultimo_nome)
        matricula = '\\texttt{%s}' % fvc[k][0]
        random = r1.rnd()
        exam = tex.texnician(
                diretorio,
                arquivo,
                payload,
                string_nome,
                matricula,
                random
                )
        with open('upshot/provas/exam_%s.tex' % k, 'w') as f:
            print(exam, file=f)


if __name__ == '__main__':
    main()
