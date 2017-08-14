import zeep
from xml.etree import ElementTree

wsdl = 'http://www.pttplc.com/webservice/pttinfo.asmx?WSDL'
client = zeep.Client(wsdl=wsdl)
xml_resp = (client.service.CurrentOilPrice('EN'))
root = ElementTree.fromstring(xml_resp)
dicti = {}
i = 1
for child in root:
	dicti2 = {}
	for child2 in child:
		dicti2[child2.tag]=child2.text
	dicti[str(i)] = dicti2
	print(i)
	i = i+1

print(dicti)

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
	print(i)
	i = i+1

print(dicti)

