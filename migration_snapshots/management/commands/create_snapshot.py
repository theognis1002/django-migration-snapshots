from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--format", help="output format for digraph")

    def handle(self, *args, **options):
        MigrationSnapshot = apps.get_model("migration_snapshots", "MigrationSnapshot")
        MigrationSnapshot.objects.create(
            output_format=options.get("format", MigrationSnapshot.PDF)
        )
