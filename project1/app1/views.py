from django.shortcuts import render, redirect
from app1.forms import UserUploadForm
from app1.convert import convert_file
from app1.transfer import move_dir
import os
from project1 import settings

# Create your views here.

# path = settings.MEDIA_ROOT
# print(path)
# i = os.listdir(path + '/converted_files')
# print(i)




def home(request):
    
    if request.method == 'POST':
        form = UserUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            f = form.save()
            f.user = request.user
            f.save()
            
            
            ff = request.FILES.getlist('file')
            
            #type is weird
            # ff = request.FILES['file']
            #type is str
            file_name = form.cleaned_data['file'].name
            #abs path and type is str
            file_path = f.file.path
            
            #not the full path and type is weird
            # p = f.file
            
            
            print(f.user, ff, type(ff))
                  # file_name, type(file_name),
                  # file_path, type(file_path))
            
            for i in ff:
                convert_file(file_path)
            
            folder_name = 'media/converted_files'
            src_dir = os.getcwd()
            dest_dir = os.path.join(src_dir, folder_name)
            
            move_dir(src_dir, dest_dir, '*.png')
            
            return redirect('app1-display')
        
    else:
        
        form = UserUploadForm()
    
    return render(request, 'app1/home.html', {'form' : form})


def display(request):
    
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/converted_files')
    context = {'images' : img_list} 
    
    return render(request, 'app1/display.html', context)


















