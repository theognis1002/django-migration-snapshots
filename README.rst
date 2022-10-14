=============================
Django Migration Snapshots
=============================

.. image:: https://img.shields.io/pypi/v/django-migration-snapshots.svg?style=for-the-badge
   :target: https://pypi.org/project/django-migration-snapshots/

.. image:: https://img.shields.io/pypi/pyversions/django-migration-snapshots?style=for-the-badge
   :target: https://pypi.org/project/django-migration-snapshots/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
   :target: https://github.com/psf/black


Capture django migration history snapshots

Documentation
-------------

The full documentation is at https://django-migration-snapshots.readthedocs.io.

Quickstart
----------

Install Django Migration Snapshots::

    pip install django-migration-snapshots

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        "migration_snapshots",
        ...
    )


Features
--------

* Digraph text and visual output
* `MigrationSnapshot` data model


TODO's
------
* Tests


Development commands
---------------------

::

    make install
    make package
    make deploy
