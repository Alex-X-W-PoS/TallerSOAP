# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cliente.models import Oil
from cliente.forms import CurrentOilPrice, GetOilPrice
from django.shortcuts import render, redirect
import zeep
from xml.etree import ElementTree
# Create your views here.
def index(request):
        return render(request, 'index/index_principal.html',{})

def current(request):
	
	if request.method == 'POST':
                form = CurrentOilPrice(request.POST)
                if form.is_valid():
                        lenguaje = form.cleaned_data['lenguaje']
                        wsdl = 'http://www.pttplc.com/webservice/pttinfo.asmx?WSDL'
                        client = zeep.Client(wsdl=wsdl)
                        xml_resp = (client.service.CurrentOilPrice(lenguaje))
                        root = ElementTree.fromstring(xml_resp)
                        dicti = {}
                        i = 1
                        for child in root:
                                dicti2 = {}
                                for child2 in child:
                                        dicti2[child2.tag]=child2.text
                                dicti[str(i)] = dicti2
                                i = i+1
                        return render(request, 'index/results.html', {'data': sorted(dicti.items())})
	else:
                form = CurrentOilPrice()
                return render(request, 'index/index.html', {'form':form})


	

def getprice(request):
	if request.method == 'POST':
                form = GetOilPrice(request.POST)
                if form.is_valid():
                        lenguaje = form.cleaned_data['lenguaje']
                        dia = form.cleaned_data['dia']
                        mes = form.cleaned_data['mes']
                        anio = form.cleaned_data['anio']
                        wsdl = 'http://www.pttplc.com/webservice/pttinfo.asmx?WSDL'
                        client = zeep.Client(wsdl=wsdl)
                        xml_resp = (client.service.GetOilPrice(lenguaje,dia,mes,anio))
                        root = ElementTree.fromstring(xml_resp)
                        dicti = {}
                        i = 1
                        for child in root:
                                dicti2 = {}
                                for child2 in child:
                                        dicti2[child2.tag]=child2.text
                                dicti[str(i)] = dicti2
                                i = i+1
                        return render(request, 'index/results.html', {'data': sorted(dicti.items())})
	else:
                form = GetOilPrice()
                return render(request, 'index/index.html', {'form':form})
