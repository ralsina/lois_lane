=========
Lois Lane
=========


.. image:: https://img.shields.io/pypi/v/lois_lane.svg
        :target: https://pypi.python.org/pypi/lois_lane

.. image:: https://img.shields.io/travis/ralsina/lois_lane.svg
        :target: https://travis-ci.org/ralsina/lois_lane

.. image:: https://readthedocs.org/projects/lois-lane/badge/?version=latest
        :target: https://lois-lane.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/ralsina/lois_lane/shield.svg
     :target: https://pyup.io/repos/github/ralsina/lois_lane/
     :alt: Updates


A tool to write reports.


* Free software: MIT license
* Documentation: https://lois-lane.readthedocs.io.

This is based on a blog post I wrote in 2008 because nobody bothered implementing my idea.
So, `feel free to read it <https://ralsina.me/weblog/posts/BB738.html>`__

Features
--------

Creates reports by merging data (in JSON) and a Jinja template

Example
-------

::

    lois_lane --data example/data.json --template example/template.j2 --output report.rst

The example report is `reStructured text` but you can just as easily do markdown, HTML, or whatever.


TODO
----

* Provide helper sets for different output formats.
* Support postprocessing chains to generate PDF or whatever

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

