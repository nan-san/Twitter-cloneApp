from django.views.generic import ListView #投稿一覧を表示させる
from .models import Post


# Modelsで設定したものを表示するための設定


class PostListView(ListView):
    model = Post
    template_name = "tweet/index.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']  #最新を上に表示する
    paginate_by = 5 #何ページ表示させるか
