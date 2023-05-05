from django.contrib import admin

from .models import (
    SocialNetwork, Education, Experience, Sertificate,
    CodingLanguage, Quote, FunFact, Contact, UserLetter,
)


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_active', 'order')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('edu_name', 'year', 'specialty', 'about')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'year', 'specialty', 'about')


@admin.register(Sertificate)
class SertificateAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'company', 'logo', 'image',  
        'is_active', 'order', 'year'
    )


@admin.register(CodingLanguage)
class CodingLanguageAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'logo', 'is_active', 'order'
    )


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        'author', 'from_where', 'is_active', 'image'
    )
    

@admin.register(FunFact)
class FunFactAdmin(admin.ModelAdmin):
    list_display = (
        'projects', 'clients', 'work_hour', 
        'posts', 'cv', 'about_me'
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('tel', 'city', 'region', 'email')


@admin.register(UserLetter)
class UserLetterAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'body')