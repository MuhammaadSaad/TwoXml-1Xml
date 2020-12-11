# TwoXml-1Xml
Convert 2 Xml file into 1 Xml File

Im looking for merge two parts of XML files items.xml and stock.xml to one XML file products.xml
This XML files must be defined as variable
tags nameCZ and description must be defined as variable
Reguired tags from items.xml we take: 
  number( key for stock.xml  ( warning – variable as char besause first letter can be 0  010801) ) tag must be defined in variable 
 nameCZ → tag must be defined in variable 
    description,price,manufacturer,barcode → tag must be defined in variable  
    image → URL aadress
Reguired tags from stock.xml
    stock
# Keys number ( items.xml )   < ---- >  sku ( stock.xml )
Result products.xml having number,nameCZ,description,price,manufacturer,barcode,image from items.xml and stock from stock.xml

  
