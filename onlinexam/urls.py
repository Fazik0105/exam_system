from django.urls import path,include
from django.contrib import admin
from exam import views
from django.contrib.auth.views import LogoutView,LoginView
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [

    path('admin/', admin.site.urls),
    path('teacher/',include('teacher.urls')),
    path('student/',include('student.urls')),



    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='exam/logout.html'),name='logout'),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('before-exam', views.take_exam_wait_view,name='before-exam'),



    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='exam/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-teacher', views.admin_teacher_view,name='admin-teacher'),
    path('admin-view-teacher', views.admin_view_teacher_view,name='admin-view-teacher'),
    path('update-teacher/<int:pk>', views.update_teacher_view,name='update-teacher'),
    path('delete-teacher/<int:pk>', views.delete_teacher_view,name='delete-teacher'),
    path('admin-view-pending-teacher', views.admin_view_pending_teacher_view,name='admin-view-pending-teacher'),
    path('admin-view-pending-student', views.admin_view_pending_student_view,name='admin-view-pending-student'),
    path('approve-teacher/<int:pk>', views.approve_teacher_view,name='approve-teacher'),
    path('reject-teacher/<int:pk>', views.reject_teacher_view,name='reject-teacher'),
    path('approve-student/<int:pk>', views.approve_student_view,name='approve-student'),
    path('reject-student/<int:pk>', views.reject_student_view,name='reject-student'),
    path('approve-student-for-exam/<int:pk>', views.approve_student_for_exam_view,name='approve-student-for-exam'),
    path('reject-student-for-exam/<int:pk>', views.reject_student_for_exam_view,name='reject-student-for-exam'),

    path('teacher-view-pending-exam', views.teacher_view_pending_student_view,name='teacher-view-pending-exam'),
    path('approve-student-for-exam/<int:pk>', views.approve_student_for_exam_view, name='approve-student-for-exam'),
    path('reject-student-for-exam/<int:pk>', views.reject_student_for_exam_view, name='reject-student-for-exam'),
    path('teacher-student', views.teacher_student_view, name='teacher-student'),
    path('teacher-view-student-marks', views.teacher_view_student_marks_view, name='teacher-view-student-marks'),
    path('teacher-view-marks/<int:pk>', views.teacher_view_marks_view, name='teacher-view-marks'),
    path('teacher-check-marks/<int:pk>', views.teacher_check_marks_view, name='teacher-check-marks'),

    path('admin-student', views.admin_student_view,name='admin-student'),
    path('admin-view-student', views.admin_view_student_view,name='admin-view-student'),
    path('admin-view-student-marks', views.admin_view_student_marks_view,name='admin-view-student-marks'),
    path('admin-view-marks/<int:pk>', views.admin_view_marks_view,name='admin-view-marks'),
    path('admin-check-marks/<int:pk>', views.admin_check_marks_view,name='admin-check-marks'),
    path('update-student/<int:pk>', views.update_student_view,name='update-student'),
    path('delete-student/<int:pk>', views.delete_student_view,name='delete-student'),
    path('admin-student-exams-pending', views.admin_student_exams_pending_view,name='admin_student_exams_pending'),
    path('approve-student-exam/<int:pk>', views.approve_student_exam_view,name='approve-student-exam'),
    path('reject-student-exam/<int:pk>', views.reject_student_exam_view,name='reject-student-exam'),

    path('admin-course', views.admin_course_view,name='admin-course'),
    path('admin-add-course', views.admin_add_course_view,name='admin-add-course'),
    path('admin-view-course', views.admin_view_course_view,name='admin-view-course'),
    path('delete-course/<int:pk>', views.delete_course_view,name='delete-course'),

    path('admin-question', views.admin_question_view,name='admin-question'),
    path('admin-add-question', views.admin_add_question_view,name='admin-add-question'),
    path('admin-view-question', views.admin_view_question_view,name='admin-view-question'),
    path('view-question/<int:pk>', views.view_question_view,name='view-question'),
    path('delete-question/<int:pk>', views.delete_question_view,name='delete-question'),
    
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 


]
