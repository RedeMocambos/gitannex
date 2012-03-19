from django.core.management.base import NoArgsCommand, CommandError

from gitannex.models import GitAnnexRepository, runScheduledJobs

"""
Definições do comando para executar as operações planejadas.
"""

class Command(NoArgsCommand):
    """Executa as operações planejadas."""
    help = 'Run scheduled jobs related to git repositories'

    def handle_noargs(self, **options):
        runScheduledJobs()
        
