# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from app01 import models
import os
 
def upload(request):
    if request.method == 'GET':
        return render(request,'upload.html')
    elif request.method == 'POST':
        obj = request.FILES.get('fafafa')
	print obj
        f = open(os.path.join('upload',obj.name),'wb')
        for line in obj.chunks():
            f.write(line)
        f.close()
        return HttpResponse('上传成功')
