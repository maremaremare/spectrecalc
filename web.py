import djmicro
djmicro.configure()

from django.shortcuts import render

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()

@djmicro.route(r'^$')
def hello(request):
    return render(request, 'index.html', {})

@djmicro.route(r'^test/(\d+)/$')
def test(request, id):
    return render(request, 'test.html', {'id': id})

if __name__ == '__main__':
    djmicro.run()