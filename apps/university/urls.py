from rest_framework import routers

from apps.university.views import CourseViewSet, GroupViewSet, DisciplineViewSet, StudentViewSet, \
    CuratorViewSet

router = routers.SimpleRouter()
router.register('courses', CourseViewSet)
router.register('groups', GroupViewSet)
router.register('disciplines', DisciplineViewSet)
router.register('students', StudentViewSet)
router.register('curators', CuratorViewSet)
urlpatterns = router.urls
