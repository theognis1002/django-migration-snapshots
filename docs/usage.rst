=====
Usage
=====

To use Django Migration Snapshots in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'migration_snapshots.apps.DjangoMigrationSnapshotsConfig',
        ...
    )

Add Django Migration Snapshots's URL patterns:

.. code-block:: python

    from migration_snapshots import urls as migration_snapshots_urls


    urlpatterns = [
        ...
        url(r'^', include(migration_snapshots_urls)),
        ...
    ]
