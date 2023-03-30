from django.shortcuts import render,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelFrom
from .mixins import OrganisorAndLoginRequiredMixin


# Create your views here.
class AgentListView(OrganisorAndLoginRequiredMixin,generic.ListView):
    template_name = 'agents/agent_list.html'
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation= organisation)
    context_object_name = "agents"

class AgentCreateView(OrganisorAndLoginRequiredMixin,generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelFrom

    def get_success_url(self):
        return reverse("agents:agent-list")


    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView,self).form_valid(form)
    
class AgentDetailView(OrganisorAndLoginRequiredMixin,generic.DeleteView):
    template_name = 'agents/agent_details.html'
    context_object_name = 'agent'


    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation= organisation)

class AgentUpdateView(OrganisorAndLoginRequiredMixin,generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelFrom

    def get_success_url(self):
        return reverse("agents:agent-list")
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation= organisation)

class AgentDeleteView(OrganisorAndLoginRequiredMixin,generic.DeleteView):
    template_name = "agents/agent_delete.html"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation= organisation)
    
    def get_success_url(self):
        return reverse("agents:agent-list")


