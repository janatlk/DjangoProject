import urllib.request

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm, CustomUser
from main.models import Director,Review,Movie, ConfirmCode
from django.utils.html import format_html
from django.core.files import File
# Register your models here.

class AdminReviewInline(admin.StackedInline):
    model = Review
    extra = 0

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser


class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = 'title description director image_tag'.split()
    def image_tag(self,obj):
        return format_html('<img src={} style="wight: 300px; height:200px;" />'.format(obj.image.url))
    search_fields = ['title']
    image_tag.allow_tags = True
    image_tag.__name__ = 'image'
    list_filter = ['director']
    list_editable = 'director'.split()
    list_per_page = 5
    inlines = [AdminReviewInline]
    # list_select_related = True


admin.site.register(ConfirmCode)
admin.site.register(Review)
admin.site.register(Director)
admin.site.register(Movie, MovieAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
