from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def mine_group_required(gp):
    def wrapperone(fx):
        def wrapper2(request, *args, **kwargs):
            if request.user.groups.filter(name = gp).exists():
                return fx(request, *args, **kwargs)

            # ru = list(request.user.groups.values_list('name',flat=True).distinct())

            # if gp in ru:
            #     return fx(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper2
    return wrapperone   

from django.core.exceptions import PermissionDenied
class CheckPremiumGroupMixin:

    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.filter(name = "premium").exists():
            # return True
            return super().dispatch(request, *args, **kwargs)

        else:
            raise PermissionDenied    