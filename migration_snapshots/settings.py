from django.conf import settings

MIGRATION_SNAPSHOT_FILENAME = getattr(
    settings, "MIGRATION_SNAPSHOT_FILENAME", "migration_snapshot"
)

MIGRATION_SNAPSHOT_MODEL = getattr(settings, "MIGRATION_SNAPSHOT_MODEL", False)
