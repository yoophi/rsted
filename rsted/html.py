import random
import subprocess

from flask import url_for
import os.path as op

default_rst_opts = {
    'no_generator': True,
    'no_source_link': True,
    'tab_width': 4,
    'file_insertion_enabled': False,
    'raw_enabled': False,
    'stylesheet_path': None,
    'traceback': True,
    'halt_level': 5,
}


def rst2html(rst, theme=None, opts=None):
    proj_dir = op.dirname(op.dirname(__file__))

    filename = op.join(proj_dir, 'static', 'tmp', 'docs', 'index.rst')
    source_dir = op.join(proj_dir, 'static', 'tmp', 'docs')
    target_dir = op.join(proj_dir, 'static', 'tmp', 'docs', 'build')

    print proj_dir, filename, source_dir, target_dir

    with open(filename, 'w') as f:
        f.write(rst)
        f.flush()

        subprocess.call(['sphinx-build', source_dir, target_dir, filename])

    return '<html><head><script>window.location.href = "{url}"; </script><body><a href="{url}">link</a></body></html>'.format(url=url_for('static', filename='tmp/docs/build/index.html', version=random.random()))
