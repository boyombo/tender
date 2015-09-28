from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import modelformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse

from procurement.models import Tender, Documentation, UploadedDoc, Company


@login_required
def tenders(request):
    tender_list = Tender.objects.filter(active=True).order_by('id')
    return render(request, 'list_tenders.html', {'tender_list': tender_list})


@login_required
def upload(request, id):
    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        messages.error(request, 'You are not assigned to any company')
        return redirect('tender_list')

    tender = get_object_or_404(Tender, pk=id)
    docs = Documentation.objects.filter(active=True).order_by('id')
    num_docs = docs.count()
    DocFormset = modelformset_factory(UploadedDoc, fields=(
        'document', 'upload',), extra=num_docs)
    if request.method == 'POST':
        formset = DocFormset(request.POST, request.FILES)
        #import pdb;pdb.set_trace()
        if formset.is_valid():
            instances = formset.save(commit=False)
            for obj in instances:
                obj.tender = tender
                obj.company = company
                try:
                    obj.save()
                except IntegrityError:
                    old_obj = UploadedDoc.objects.get(
                        tender=tender,
                        company=company,
                        document=obj.document)
                    old_obj.delete()
                    obj.save()
            messages.info(request, 'The files were added successfully')
            return redirect('tender_list')
    else:
        formset = DocFormset(queryset=tender.documents.filter(company=company))
        #import pdb;pdb.set_trace()
    return render(
        request, 'upload.html',
        {
            'tender': tender,
            'formset': formset,
            'docs': docs,
            'company': company,
        }
    )


def download(request, id):
    doc = get_object_or_404(UploadedDoc, pk=id)
    content = doc.upload.read()
    response = HttpResponse(content_type='application/octet-stream')
    fname = doc.upload.name.split('/')[-1]
    response['Content-Disposition'] = 'attachment; filename="%s"' % fname
    response.write(content)
    return response
