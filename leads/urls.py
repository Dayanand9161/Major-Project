from django.urls import path
from leads.views import (LeadListView,LeadDetailView,
LeadCreateView,LeadUpdateView,LeadDeleteView,AssignAgentView,CategoryListView,
CategoryDetailView,LeadCategoryUpdateView,CategoryCreateView,CategoryUpdateView,
CategoryDeleteView
)
app_name = "leads"
urlpatterns = [
    path('',LeadListView.as_view(),name="lead-list"),
    path('<int:pk>',LeadDetailView.as_view(),name="lead-detail"),
    path('<int:pk>/update/',LeadUpdateView.as_view(),name="lead-update"),
    path('<int:pk>/delete/',LeadDeleteView.as_view(),name="lead-delete"),
    path('<int:pk>/delete/',LeadDeleteView.as_view(),name="lead-delete"),
    path('<int:pk>/assignagent/',AssignAgentView.as_view(),name="lead-assign-agent"),
    path('<int:pk>/category-update/',LeadCategoryUpdateView.as_view(),name="lead-category-update"),
    path('categories/',CategoryListView.as_view(),name= "category-list"),
    path('categories-details/<int:pk>',CategoryDetailView.as_view(),name= "category-detail"),
    path('categories-details/<int:pk>/update',CategoryUpdateView.as_view(),name= "category-update"),
    path('categories-details/<int:pk>/delete',CategoryDeleteView.as_view(),name= "category-delete"),
    path('create',LeadCreateView.as_view(),name='lead-create'),
    path('create-cateogry',CategoryCreateView.as_view(),name = 'category-create')

]
