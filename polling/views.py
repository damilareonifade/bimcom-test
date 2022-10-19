from django.shortcuts import render,redirect
from .models import *
from django.db import transaction
from .form import AnnouncedPuResultsForm


def result_polling_unit(request):
    rpu = AnnouncedPuResults.objects.all()
    return render(request,'bincom_test/polling_unit_result.html',{'rpu':rpu})

@transaction.atomic()
def polling_result_create(request):
    if request.method == 'POST':
        form = AnnouncedPuResultsForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.user_ip_address= '192.168.1.1'
            form.save()
            return redirect('polling:polling_unit_result')
    else:
        form = AnnouncedPuResultsForm()
    return render(request,'bincom_test/polling_result_create.html',{'form':form})



