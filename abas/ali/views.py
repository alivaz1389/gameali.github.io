from django.shortcuts import render

from django.http import HttpResponse
from django.template import TemplateSyntaxError
from numpy import kaiser
TEMPLATE_DIRS=(
    'os.pat.join(BASE_DIR,"templates")'
    )
def index(request):
    return render(request,"index.html")
