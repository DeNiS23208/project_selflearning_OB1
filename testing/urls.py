from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, TestAttemptViewSet

router = DefaultRouter()
router.register("questions", QuestionViewSet)
router.register("attempts", TestAttemptViewSet)

urlpatterns = router.urls