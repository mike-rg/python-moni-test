from django.conf.urls import url

from .views import (
    LoanCreate, 
    LoanDelete,
    LoanDetail,
    LoanUpdate,
    LoanList,
)

urlpatterns = [
    url(r'^$', LoanList.as_view(), name='loan-list'),
    url(r'^create/', LoanCreate.as_view(), name='loan-create'),
    url(r'^update/(?P<pk>\d+)/', LoanUpdate.as_view(), name='loan-update'),
    url(r'^delete/(?P<pk>\d+)/', LoanDelete.as_view(), name='loan-delete'),
    url(r'^detail/(?P<pk>\d+)/', LoanDetail.as_view(), name='loan-detail'),
]