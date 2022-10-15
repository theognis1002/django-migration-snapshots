from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--format", help="output format for digraph")
        parser.add_argument(
            "--date",
            help="end date for migration history output",
            required=False,
            default="",
        )
        # parser.add_argument("--caption", help="caption for digraph out")

    def handle(self, *args, **options):
        """
        Create migration snapshot using input arguments.
        Default format: 'pdf'
        """
        MigrationSnapshot = apps.get_model("migration_snapshots", "MigrationSnapshot")
        MigrationSnapshot.objects.create(
            output_format=options.get("format", MigrationSnapshot.PDF)
        )
