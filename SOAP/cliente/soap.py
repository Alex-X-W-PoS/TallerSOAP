import zeep

wsdl = 'http://www.pttplc.com/webservice/pttinfo.asmx?WSDL'
client = zeep.Client(wsdl=wsdl)
print(client.service.CurrentOilPrice('EN'))
