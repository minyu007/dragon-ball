from django.urls import path
from . import test_api

urlpatterns = [
    # show data
    path('testgetdata', test_api.test_get_data),
    path('testgetsingledata/<str:pk>', test_api.test_get_single_data),

    # add data
    path('testadddata', test_api.test_add_data),

    # update data
    path('testupdatedata/<str:pk>', test_api.test_update_data),

    # delete data
    path('testdeletedata', test_api.test_delete_data),
    path('testdeletedataalt/<str:pk>', test_api.test_delete_data_alt)
]