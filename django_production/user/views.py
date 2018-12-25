from django.shortcuts import render

def send_email(request):
    print('COUCOU')
    # send_email_task.delay("guillaume.guerdoux@mayerprezioso.com")
    return render(request, 'home.html')
