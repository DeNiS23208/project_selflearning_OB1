from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, MaterialViewSet, SectionViewSet

router = DefaultRouter()
router.register("courses", CourseViewSet)
router.register("sections", SectionViewSet)
router.register("materials", MaterialViewSet)

urlpatterns = router.urls
