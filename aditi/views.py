from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request,'home.html')

def count(request):
    data=request.GET['typehere']
    if data:
        len_text=len(data)
        count_list = data.split()
        length=len(count_list)
        lentext=len_text-(length-1)
        
        for i in count_list:
            repeate={i:count_list.count(i) for i in count_list}
        dictionary={'length_word':length,'data':data,'list':count_list,"lenght_text":lentext,'repeate':repeate}                                                      
        return render(request,'count.html',dictionary)
    else:
        return HttpResponse('Type Something')
def about(request):
    return render(request,'about.html')