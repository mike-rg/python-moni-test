from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import LoanForm
from .models import Loan


class LoanCreate(CreateView):
    form_class = LoanForm
    template_name = 'loans/loan_create.html'
    success_url = reverse_lazy('loan-create')
    success_message = _("Loan message")

    def form_valid(self, form):
        approved, error = form.request_loan()
        if error:
            self.success_message = _("Loan Reject")
            return HttpResponseRedirect(self.get_success_url())
        if approved:
            self.success_message = _("Loan Accepted")
            form.instance.approved = True
            super(LoanCreate, self).form_valid(form)

        return render(self.request, self.template_name,
                      self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(LoanCreate, self).get_context_data(**kwargs)
        context['message'] = self.success_message
        return context


@method_decorator(staff_member_required, name='dispatch')
class LoanDelete(DeleteView):
    model = Loan
    success_url = reverse_lazy('loan-list')


@method_decorator(staff_member_required, name='dispatch')
class LoanList(ListView):
    model = Loan


@method_decorator(staff_member_required, name='dispatch')
class LoanUpdate(UpdateView):
    model = Loan
    form_class = LoanForm
    template_name = 'loans/loan_create.html'
    success_url = reverse_lazy('loan-list')


@method_decorator(staff_member_required, name='dispatch')
class LoanDetail(DetailView):
    model = Loan
