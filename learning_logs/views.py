from django.shortcuts import render
def test(request):
    return render(request,'learning_logs/index.html')
