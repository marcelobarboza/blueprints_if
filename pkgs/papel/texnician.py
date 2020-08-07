#!/usr/bin/env python3

import jinja2


def texnician(directory, textfile, payload, student, code, rnd):
    template_loader = jinja2.FileSystemLoader(directory)
    template_envirnoment = jinja2.Environment(loader=template_loader)
    template = template_envirnoment.get_template(textfile)
    template_rendered = template.render(
            dados=payload,
            aluno=student,
            matricula=code,
            random=rnd
            )
    return template_rendered
