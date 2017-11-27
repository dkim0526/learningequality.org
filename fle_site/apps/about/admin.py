from django.contrib import admin
from django.contrib.auth.models import User

from models import TeamMember, BoardMember, PressArticle, PressLogo, Internship, Job, SupportingOrganization, OrganizationType, Translator


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'last_updated',)

class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'last_updated',)

class PressArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'publish_date',)

class PressLogoAdmin(admin.ModelAdmin):
    list_display = ('title',)

class InternshipAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated')

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated')

class SupportingOrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization_type')

class OrganizationTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)

class TranslatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')

admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(BoardMember, BoardMemberAdmin)
admin.site.register(PressArticle, PressArticleAdmin)
admin.site.register(PressLogo, PressLogoAdmin)
admin.site.register(SupportingOrganization, SupportingOrganizationAdmin)
admin.site.register(OrganizationType, OrganizationTypeAdmin)
admin.site.register(Internship, InternshipAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Translator, TranslatorAdmin)
