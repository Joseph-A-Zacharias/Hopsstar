from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='home'),
   path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
   path('about/', views.about, name='about'), 
   path('terms-and-conditions/', views.termsandcondition, name='terms_and_conditions'),
   path('campus/', views.campus, name='campus'),
   path('campussearch/', views.campussearch, name='campussearch'),
   path('campuslist/<str:category_name>/<str:state>/', views.campuslist, name='campuslist'),
   path('campusblog/<str:college_name>/', views.campusblog, name='campusblog'),
   path('notes/', views.notes, name='notes'),
   path('notesearch/', views.notesearch, name='notesearch'),
   path('noteslist/<str:note_name>/<str:subject_name>/', views.noteslist, name='noteslist'),
   path('notesblog/<str:chapter_name>/', views.notesblog, name='notesblog'),
   path('research/', views.research, name='research'),
   path('cheatsheets/', views.cheatsheets, name='cheatsheets'),
   path('cheatsearch/', views.cheatsearch, name='cheatsearch'),
   path('cheatsheetsblog/<str:cheat_name>/', views.cheatsheetsblog, name='cheatsheetsblog'),
   path('careers/', views.careers, name='careers'),
   path('careersearch/', views.careersearch, name='careersearch'),
   path('careerslist/<str:career_name>/', views.careerslist, name='careerslist'),
   path('careersblog/<str:career_descirption>/', views.careersblog, name='careersblog'),
   path('becomeapartner/', views.becomeapartner, name='partner'),
   path('privacypolicy/', views.privacypolicy, name='privacy'),
   path('cookiespolicy/', views.cookiespolicy, name='cookies'),
]
