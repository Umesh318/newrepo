from django.contrib import admin
from . models import category,Post
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','tittle','description','add_time')
    search_fields = ('tittle',)
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('tittle',)
    search_fields = ('tittle',)
    list_filter = ('images',)
    

    
admin.site.register(category,categoryAdmin)
admin.site.register(Post,PostAdmin)
