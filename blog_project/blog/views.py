# -*- coding: utf-8 -*-
import logging
from django.shortcuts import render

logger = logging.getLogger('blog.views')
# Create your views here.
def index(request):
    # try:
    #     open('sss.txt','r')
    # except Exception as e:
    #     logger.error(e)
    return render(request, 'index.html', locals())

