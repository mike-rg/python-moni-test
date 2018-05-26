import json
import urllib.parse
import urllib.request

from django import forms
from django.conf import settings

from .models import Loan


class LoanForm(forms.ModelForm):
    dni = forms.CharField(min_length=7, max_length=8)

    class Meta:
        model = Loan
        fields = [
            'dni',
            'firstname',
            'lastname',
            'gender',
            'email',
            'amount'
        ]

    def request_loan(self):
        """
        Example request:
        <api-endpoint>/?document_number=30156149&gender=M&email=fran@mail.com
        """
        data = {
            'document_number': self.cleaned_data['dni'],
            'gender': self.cleaned_data['gender'],
            'email': self.cleaned_data['email']
        }
        params = urllib.parse.urlencode(data)
        url = settings.URL_SCORING_SERVICE + '?' + params
        response = urllib.request.urlopen(url)
        try:
            json_response = json.loads(response.read().decode('utf-8'))
        except Exception as e:
            return None, None
        approved = json_response.get('approved')
        error = json_response.get('error')
        return approved, error