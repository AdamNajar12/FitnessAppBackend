from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import Client
from exercises.models import Progression


@api_view(['GET'])
def client_progression_stats(request):
    # Requête pour obtenir les clients avec leurs progressions
    clients_with_progression = Progression.objects.all()

    # Calculer les statistiques
    objectifs_atteints = clients_with_progression.filter(status='ATTEINT').count()
    en_progression = clients_with_progression.filter(status='EN_COURS').count()
    objectifs_non_atteints = clients_with_progression.filter(status='NON_ATTEINT').count()
    
    # Structure des données à retourner
    progression_stats = {   
        "Objectifs Atteints": objectifs_atteints,
        "En Progression": en_progression,
        "Objectifs Non Atteints": objectifs_non_atteints
    }

    return Response({"progression_stats": progression_stats})
