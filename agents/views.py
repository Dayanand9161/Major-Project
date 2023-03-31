from django.shortcuts import render,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelFrom
from .mixins import OrganisorAndLoginRequiredMixin
from django.core.mail import send_mail
import random


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
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(str(random.randint(1,100009)))
        user.save()
        Agent.objects.create(
            user = user,
            organisation = self.request.user.userprofile
        )
        send_mail(
            subject = "you are invited to be Agent on our Crm system",
            message = "you were added as an agent on CRM. please come login to start working.",
            from_email = "admin@test.com",
            recipient_list = [user.email]
        )

        # agent.organisation = self.request.user.userprofile
        # agent.save()
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


