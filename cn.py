from xml.etree import ElementTree
from xml.dom import minidom 
import os

# get root element 
def picklang(value):
 	root = ElementTree.parse("stock.xml").getroot()
 	for item in root.findall('./item'):
 		if item.find("sku").text==value:
 			return item.find("stock").text
 	#exit()
root = ElementTree.parse("items.xml").getroot()

rooted = minidom.Document() 
xml = rooted.createElement('items')  

rooted.appendChild(xml)
#print("<items>");
for item in root.findall('./item'):
	#print("<item>");
	stock=picklang(item.find("number").text)

	#print(stock)
	"""print("\t<number>"+"" if item.find("number").text==None else item.find("number").text.encode('utf8') +"</number>")
	print("\t<nameCZ>"+"" if item.find("nameCZ").text==None else item.find("nameCZ").text.encode('utf8') +"</nameCZ>")
	print("\t<description>"+"" if item.find("description").text==None else item.find("description").text.encode('utf8') +"</description>")
	print("\t<manufacturer>"+"" if item.find("manufacturer").text==None else item.find("manufacturer").text.encode('utf8') +"</manufacturer>")
	print("\t<barcode>"+"" if item.find("barcode").text==None else item.find("barcode").text.encode('utf8') +"</barcode>")
	print("\t<image>"+"" if item.find("image").text==None else item.find("image").text.encode('utf8') +"</image>")
	print("\t<stock>"+"" if stock==None else stock+"</stock>")

	print("</item>");"""
	
	productChild = rooted.createElement('item') 
	productChild.setAttribute('number', "" if item.find("number").text==None else item.find("number").text.encode('utf8')) 
	productChild.setAttribute('nameCZ', "" if item.find("nameCZ").text==None else item.find("nameCZ").text.encode('utf8')) 
	productChild.setAttribute('description',"" if item.find("description").text==None else item.find("description").text.encode('utf8')) 
	productChild.setAttribute('manufacturer',"" if item.find("manufacturer").text==None else item.find("manufacturer").text.encode('utf8')) 
	productChild.setAttribute('barcode', "" if item.find("barcode").text==None else item.find("barcode").text.encode('utf8')) 
	productChild.setAttribute('image', "" if item.find("image").text==None else item.find("image").text.encode('utf8')) 
	productChild.setAttribute('stock',stock) 
	xml.appendChild(productChild)
	#for child in item: 

	    # special checking for namespace object content:media 
	    #print(child.text)
	   
	# append news dictionary to news items list 
	#exit()
#print("<items>");
"""xml_str = rooted.toprettyxml()   
with open("products.xml", "w") as f: 
    f.write(xml_str)"""
file_handle = open("products.xml","wb")
rooted.writexml(file_handle)
file_handle.close()