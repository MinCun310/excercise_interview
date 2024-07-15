from django.db.models import Q

from staff.models import Staff
from staff.serializers import StaffSerializer


def get_list_by_params_for_user(params):
    filters = Q()
    try:
        if 'id' in params:
            filters &= Q(staff_id=params['id'])
        if 'category' in params:
            filters &= Q(category=params['category'])
    except Exception:
        return -1

    results = Staff.objects.filter(filters)
    serializers = StaffSerializer(results, many=True)
    return serializers.data
