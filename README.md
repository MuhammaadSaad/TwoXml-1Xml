# TwoXml-1Xml
Convert 2 Xml file into 1 Xml File

Im looking for merge two parts of XML files items.xml and stock.xml to one XML file products.xml
This XML files must be defined as variable
tags <nameCZ> and <description> must be defined as variable
Reguired tags from items.xml we take: 
  <number></number> ( key for stock.xml  ( warning – variable as char besause first letter can be 0  010801) ) tag must be defined in variable 
  <nameCZ><nameCZ> → tag must be defined in variable 
    <price></price> <manufacturer></manufacturer> <barcode></barcode> <description></description> → tag must be defined in variable  
    <image></image> → URL aadress
Reguired tags from stock.xml
    <stock></stock>
Keys <number> ( items.xml )   < ---- >  <sku> ( stock.xml )
Result products.xml 
    <?xml version="1.0" encoding="UTF-8"?> 
    <items> <item> 
      <number></number> → from items.xml 
      <nameCZ></nameCZ> → from items.xml 
      <description></description> → from items.xml 
      <price></price> → from items.xml 
      <manufacturer></manufacturer> →from items.xml 
      <barcode></barcode> → from items.xml 
      <image></image> → from items.xml 
      <stock></stock> → from stock.xml 
    </item> 
