from django.contrib import admin

# Register your models here.
from .models import Post , PostView , Comment , Like , User_model

admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(User_model)