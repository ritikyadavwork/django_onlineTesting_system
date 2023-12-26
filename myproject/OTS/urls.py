from django.urls import path

from .views import welcome, candidateRegistrationForm, candidateRegistration, loginView, candidateHome, \
    testpaper, calculateTestResult, testResultHistroy, showTestResult, logOut, form_view

app_name = 'OTS'

urlpatterns = [

    path('', candidateHome, name='home'),
    path('new-candidate', candidateRegistrationForm, name='registrationForm'),
    path('store-candidate', candidateRegistration, name='storeCandidate'),
    path('login', loginView, name='login'),
    path('test-paper', testpaper, name="testPaper"),
    path('calculate-result', calculateTestResult),
    path('form', form_view, name="form"),
    path('test-history', testResultHistroy, name='testHistory'),
    path('result', showTestResult),
    path('logout', logOut, name='logout'),

]
