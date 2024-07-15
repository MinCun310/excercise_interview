from django.shortcuts import render
from rest_framework.views import APIView

from core.utils.shortcuts import success_response, error_response
from staff.services import staff


# Create your views here.


class DetailByConditionView(APIView):
    # filters by staff_id or category
    def get(self, request):
        params_name = dict(request.GET.items())
        staffs_filter = staff.get_list_by_params_for_user(params_name)
        if staffs_filter == -1:
            return error_response(message="Can't filters by these fields")
        return success_response(data=staffs_filter)
