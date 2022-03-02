from .views import *
from rest_framework import routers


router = routers.SimpleRouter()

router.register(r'posts', PostListView())
router.register(r'posts/{pk}', PostDetailView())
router.register(r'comments', CommentView())
router.register(r'comments/{pk}',CommentDetailView())
router.register(r'tags',TagsView())

urlpatterns = router.urls
