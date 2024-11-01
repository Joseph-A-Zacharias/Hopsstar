from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Campu(models.Model):
    category_name = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    college_name = models.CharField(max_length=250, null=False)
    university_name = models.CharField(max_length=100, null=False)
    affliation = models.CharField(max_length=100, null=False)
    rank = models.CharField(max_length=100, null=False)
    campus_blog = RichTextUploadingField()

    class Meta:
     ordering = ('-id',)

    def __str__(self):
        return f"{self.category_name} - {self.state} - {self.college_name} - {self.university_name}"


    def get_absolute_url(self):
        return reverse('campusblog', args=[self.college_name])

class ad_campu(models.Model): 

    ad_college_name = models.CharField(max_length=250, null=False)
    ad_university_name = models.CharField(max_length=100, null=False)
    ad_affliation = models.CharField(max_length=100, null=False)
    ad_rank = models.CharField(max_length=100, null=False)
    ad_link = models.URLField(max_length=300, null=False)

    def __str__(self):
        return f"{self.ad_college_name} - {self.ad_university_name}"

class Note(models.Model):
    note_name = models.CharField(max_length=100, null=False)
    note_subject = models.CharField(max_length=100, null=False)
    chapter_name = models.CharField(max_length=250, null=False)
    note_blog = RichTextUploadingField()

    class Meta:
        ordering =('id',)

    def __str__(self):
        return f"{self.note_name} - {self.note_subject}"
    
    def get_absolute_url(self):
        return reverse('notesblog', args=[self.chapter_name])
    
class Ad_Note(models.Model):
    ad_note_head = models.CharField(max_length=250, null=False)
    ad_note_link = models.URLField(max_length=300, null=False)

    def __str__(self):
        return self.ad_note_head
    
class Cheatsheet(models.Model):
    cheat_name = models.CharField(max_length=100, null=False , unique=True)
    cheat_blog = RichTextUploadingField()

    def __str__(self):
        return self.cheat_name
    
    def get_absolute_url(self):
        return reverse('cheatsheetsblog', args=[self.cheat_name])
    
class Career(models.Model):
    career_name = models.CharField(max_length=100, null=False)
    career_descirption = models.CharField(max_length=250, null=False)
    career_blog = RichTextUploadingField()

    def __str__(self):
        return f"{self.career_name} - {self.career_descirption}"
    
    def get_absolute_url(self):
        return reverse('careersblog', args=[self.career_descirption])

class Ad_Career(models.Model):
    ad_career_head = models.CharField(max_length=250, null=False)
    ad_career_link = models.URLField(max_length=300, null=False)

    def __str__(self):
        return self.ad_career_head

class Contactbutton(models.Model):

    contact_email = models.EmailField(max_length=100)
    whatsapp_link = models.URLField(max_length=300, null=False)
    telegram_link = models.URLField(max_length=300, null=False)
    youtube_link = models.URLField(max_length=300, null=False)
    instagram_link = models.URLField(max_length=300, null=False)

class Termsandconditon(models.Model):
    term_content = RichTextUploadingField()
    
class Privacypolicy(models.Model):
    privacy_content = RichTextUploadingField()

class Cookiespolicy(models.Model):
    cookies_content = RichTextUploadingField()
