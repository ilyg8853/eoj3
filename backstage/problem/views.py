from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator

from .forms import ProblemEditForm
from problem.models import Problem
from eoj3.settings import TESTDATA_DIR
from utils.testdata_preview import sort_data_from_zipfile

from ..base_views import BaseCreateView, BaseUpdateView


def testdata(request, pk):
    import os
    file_path = os.path.join(TESTDATA_DIR, str(pk) + '.zip')
    problem = Problem.objects.get(pk=pk)

    if request.method == 'POST':
        if request.FILES['data'].size > 128 * 1048576:
            print('Warning: the file is too large.')
            # TODO: file size should not be too large
        # Chunk is not used for the convenience of hash
        data = request.FILES['data'].read()
        import hashlib
        with open(file_path, 'wb') as destination:
            destination.write(data)
        problem.testdata_hash = hashlib.md5(data).hexdigest()
        problem.save()

    return render(request, 'backstage/problem/problem_testdata.html',
                  {'data_set': sort_data_from_zipfile(file_path),
                   'hash': problem.testdata_hash})


class ProblemCreate(BaseCreateView):
    form_class = ProblemEditForm
    template_name = 'backstage/problem/problem_add.html'

    def get_redirect_url(self, instance):
        return reverse("backstage:problem")


class ProblemUpdate(BaseUpdateView):
    form_class = ProblemEditForm
    queryset = Problem.objects.all()
    template_name = 'backstage/problem/problem_edit.html'


@method_decorator(login_required(), name='dispatch')
class ProblemList(ListView):
    template_name = 'backstage/problem/problem.html'
    queryset = Problem.objects.all()
    paginate_by = 20
    context_object_name = 'problem_list'
