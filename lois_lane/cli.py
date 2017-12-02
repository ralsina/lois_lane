# -*- coding: utf-8 -*-
"""Console script for lois_lane."""

import json

import click
import jinja2

from .template_helpers import helpers

def load_data(path):
    """Load JSON data."""
    with open(path) as inf:
        return json.load(inf)


def load_template(path):
    """Load and return a Jinja template from a path."""
    with open(path) as inf:
        return jinja2.Template(inf.read())


def render_data(data, template):
    """Render the template filled with the data."""
    context = data.copy()
    context.update(helpers)
    return template.render(**context)


def save_rendered(path, data):
    """Save the data into the path."""
    with open(path, 'w+') as outf:
        outf.write(data)


@click.command()
@click.option('--data', help='JSON data file', required=True)
@click.option('--template', help='JINJA template file', required=True)
@click.option('--output', help='output file', required=True)
def main(data=None, template=None, output=None):
    """Console script for Lois Lane, a reporter."""
    data = load_data(data)
    template = load_template(template)
    rendered = render_data(data, template)
    save_rendered(output, rendered)


if __name__ == "__main__":
    main()
