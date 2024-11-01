from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from .models import Campu, ad_campu, Note, Ad_Note, Cheatsheet, Career,  Ad_Career, Termsandconditon, Privacypolicy, Cookiespolicy, Contactbutton
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




# Create your views here.
@require_GET
def index(request):
    contact_button = Contactbutton.objects.first()
    if contact_button:
        context = {
            'contact_email': contact_button.contact_email,
            'whatsapp_link': contact_button.whatsapp_link
        }
    else:
        context = {
            'contact_email': None,
            'whatsapp_link': None
        }
    return render(request, 'index.html', context)

@csrf_protect
@require_POST
def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = 'User Feedback'
        email_message = 'Name: {}\nMobile: {}\nEmail: {}\nMessage: {}'.format(name, mobile, email, message)
        send_mail(subject, email_message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        
    return redirect(request.META.get('HTTP_REFERER', '/'))

@require_GET
def about(request):
    return render(request, 'about.html')


@require_GET
def termsandcondition(request):
    termsandcondition_data = Termsandconditon.objects.only('term_content').first()
    return render(request, 'terms_and_conditions.html',{'termsandcondition_data':termsandcondition_data})

@require_GET
def becomeapartner(request):
    return render(request, 'becomeapartner.html')

@require_GET
def privacypolicy(request):
    privacy_data = Privacypolicy.objects.only('privacy_content').first()
    return render(request, 'privacypolicy.html', {'privacy_data':privacy_data})

@require_GET
def cookiespolicy(request):
    cookies_data = Cookiespolicy.objects.only('cookies_content').first()
    return render(request, 'cookiespolicy.html', {'cookies_data':cookies_data})

@require_GET
def campus(request):
    campus_data = Campu.objects.values('category_name', 'state')
    
    unique_campus = {}

    for campus in campus_data:
        category_name = campus['category_name']
        state = campus['state'] 
        unique_campus.setdefault(category_name, set()).add(state)

    canonical_url = request.build_absolute_uri(reverse('campus'))

    return render(request, 'campus.html', {'unique_campus': unique_campus, 'canonical_url': canonical_url})


@csrf_protect
@require_POST
def campussearch(request):

    if request.method == 'POST':
        nts = request.POST.get('searchInput1')
        if nts: 
            campus_data = Campu.objects.filter(Q(category_name__iexact=nts) | Q(category_name__icontains=nts)).values('category_name', 'state')
            unique_results = {}

            for campus in campus_data:
                unique_results.setdefault(campus['category_name'], set()).add(campus['state'])

            campussearch_data = [{'category_name': category, 'states': list(states)} for category, states in unique_results.items()]

    search_data = {
        'campussearch_data': campussearch_data
    }
    
    return render(request, 'campus.html', search_data)

@require_GET
def campuslist(request, category_name, state):

    campuslist_data = Campu.objects.filter(category_name=category_name, state=state).values('college_name', 'university_name', 'affliation', 'rank')
    campus_ads_data = ad_campu.objects.all()
    canonical_url = request.build_absolute_uri(reverse('campuslist', args=[category_name, state]))
    return render(request, 'campuslist.html', {'campuslist_data': campuslist_data, 'campus_ads_data': campus_ads_data, 'canonical_url': canonical_url})

@require_GET
def campusblog(request, college_name):
    campublog_data = Campu.objects.filter(college_name=college_name).only('campus_blog').first()
    canonical_url = request.build_absolute_uri(reverse('campusblog', args=[college_name]))
    return render(request, 'campusblog.html', {'campublog_data': campublog_data, 'canonical_url': canonical_url})

@require_GET
def notes(request):

    notes_data = Note.objects.values('note_name', 'note_subject')
    
    unique_notes = {}

    for note in notes_data:
        note_name = note['note_name']
        note_subject = note['note_subject'] 
        unique_notes.setdefault(note_name, set()).add(note_subject)
    
    canonical_url = request.build_absolute_uri(reverse('notes'))
    
    return render(request, 'notes.html', {'unique_notes': unique_notes, 'canonical_url': canonical_url})

@csrf_protect
@require_POST
def notesearch(request):

    notesearch_data = []

    if request.method == 'POST':
        nts = request.POST.get('searchInput1')
        if nts: 
            notesearch_data = Note.objects.filter(Q(note_name__iexact=nts) | Q(note_name__icontains=nts)).values('note_name', 'note_subject')
            unique_results = {} 

            for note in notesearch_data:
                unique_results.setdefault(note['note_name'], set()).add(note['note_subject'])

            notesearch_data = [{'note_name': name, 'note_subjects': subjects} for name, subjects in unique_results.items()]

    search_data = {
        'notesearch_data': notesearch_data
    }
    
    return render(request, 'notes.html', search_data)

@require_GET
def noteslist(request, note_name, subject_name):
    chapter_data = Note.objects.filter(note_name=note_name, note_subject=subject_name).only('chapter_name')
    notes_ads_data = Ad_Note.objects.all()
    canonical_url = request.build_absolute_uri(reverse('noteslist', args=[note_name, subject_name]))
    return render(request, 'noteslist.html',{'chapter_data': chapter_data, 'notes_ads_data':notes_ads_data, 'canonical_url': canonical_url})

@require_GET
def notesblog(request, chapter_name):
    content_data = Note.objects.filter(chapter_name=chapter_name).only('note_blog').first()
    note_blog_content = content_data.note_blog if content_data else ''

    total_items = len(note_blog_content)
    midpoint = total_items // 2
    note_blog_list = [note_blog_content[:midpoint], note_blog_content[midpoint:]]
    
    paginator = Paginator(note_blog_list, 1) 
    
    page = request.GET.get('page')
    
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)
    
    next_page_exists = notes.has_next()

    canonical_url = request.build_absolute_uri(reverse('notesblog', args=[chapter_name]))
    
    return render(request, 'notesblog.html', {'notes': notes, 'next_page_exists': next_page_exists, 'canonical_url': canonical_url })

@require_GET
def research(request):
    return render(request, 'research.html')

@require_GET
def cheatsheets(request):
    cheatname_data = Cheatsheet.objects.only('cheat_name')
    canonical_url = request.build_absolute_uri(reverse('cheatsheets'))
    return render(request, 'cheatsheets.html', {'cheatname_data': cheatname_data, 'canonical_url': canonical_url})

@csrf_protect
@require_POST
def cheatsearch(request):

    cheatsearch_data = []

    if request.method == 'POST':
        chts = request.POST.get('searchInput2')
        if chts: 
            cheatsearch_data = Cheatsheet.objects.filter(Q(cheat_name__iexact=chts) | Q(cheat_name__icontains=chts)).only('cheat_name')
           
    return render(request, 'cheatsheets.html', {'cheatsearch_data': cheatsearch_data})

@require_GET
def cheatsheetsblog(request, cheat_name):
    cheatblog_data = Cheatsheet.objects.filter(cheat_name=cheat_name).only('cheat_blog').first()
    canonical_url = request.build_absolute_uri(reverse('cheatsheetsblog', args=[cheat_name]))
    return render(request, 'cheatsheetsblog.html', {'cheatblog_data': cheatblog_data, 'canonical_url': canonical_url})

@require_GET
def careers(request):
    careername_data = Career.objects.values_list('career_name', flat=True).distinct()
    unique_career_names = sorted(set(careername_data))  # Ensure uniqueness and sort the names
    canonical_url = request.build_absolute_uri(reverse('careers'))
    return render(request, 'careers.html', {'careername_data': unique_career_names, 'canonical_url': canonical_url})

@csrf_protect
@require_POST
def careersearch(request):

    careersearch_data = []

    if request.method == 'POST':
        cats = request.POST.get('searchInput3')
        if cats:
            careersearch_data =  Career.objects.filter(Q(career_name__iexact=cats) | Q(career_name__icontains=cats)).values_list('career_name', flat=True).distinct()
            unique_careersearch = sorted(set(careersearch_data))
    return render(request, 'careers.html', {'careersearch_data': unique_careersearch})


@require_GET
def careerslist(request, career_name):
    careerdiscrp_data =  Career.objects.filter(career_name=career_name).only('career_descirption')
    careers_ads_data = Ad_Career.objects.all()
    canonical_url = request.build_absolute_uri(reverse('careerslist', args=[career_name]))
    return render(request, 'careerslist.html', {'careerdiscrp_data': careerdiscrp_data, 'careers_ads_data':careers_ads_data, 'canonical_url': canonical_url})

@require_GET
def careersblog(request, career_descirption):
    careerblog_data = Career.objects.filter(career_descirption=career_descirption).only('career_blog').first()
    canonical_url = request.build_absolute_uri(reverse('careersblog', args=[career_descirption]))
    return render(request, 'careersblog.html', {'careerblog_data': careerblog_data, 'canonical_url': canonical_url})


