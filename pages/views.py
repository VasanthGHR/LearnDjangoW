from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        listInventory = ['Refridgerator','Washing Machine', 'Pressure Cooker','Water heater','LED Television' ]
        greetTxt = "Thanks for visiting our page. Have a greate day ahead !"

        context = {
            'inventory_list': listInventory,
            'greetings_msg' : greetTxt,
        }
        return context


class AboutView(TemplateView):
    
    template_name = "about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123A - D.B Road"
        context["phone_number"] = "0422-432 975"
        return context
    
    
