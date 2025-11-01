from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, SectionViewSet, MaterialViewSet

router = DefaultRouter()
router.register("courses", CourseViewSet)
router.register("sections", SectionViewSet)
router.register("materials", MaterialViewSet)

urlpatterns = router.urls
