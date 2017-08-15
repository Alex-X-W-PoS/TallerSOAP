# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cliente.models import Oil
from cliente.forms import OilForm
from django.shortcuts import render, redirect
import zeep
from xml.etree import ElementTree
# Create your views here.
def soap(request):
	dicti = {}
	if request.method == 'GET':
		wsdl = request.GET
		client = zeep.Client(wsdl=wsdl)
		xml_resp = (client.service.CurrentOilPrice('EN'))
		root = ElementTree.fromstring(xml_resp)

		i = 1
		for child in root:
			dicti2 = {}
			for child2 in child:
				dicti2[child2.tag]=child2.text
			dicti[str(i)] = dicti2
			i = i+1
		form = OilForm(instance=dicti)
		return render(request, 'index/index.html', {'form':form})


	

def soap2(request):
	if request.method == 'POST':
		wsdl = request.POST
		client2 = zeep.Client(wsdl=wsdl)
		xml_resp = (client2.service.GetOilPrice('EN',5,5,2005))
		root = ElementTree.fromstring(xml_resp)
		dicti = {}
		i = 1
		for child in root:
			dicti2 = {}
			for child2 in child:
				dicti2[child2.tag]=child2.text
			dicti[str(i)] = dicti2
			i = i+1
		return render(request, '', {'dict':dicti})
