<?php

function chkStock(int $val) {
	$stocks=simplexml_load_file("stock.xml") or die("Error: Cannot create object");
	#echo $val;
	foreach($stocks->children() as $item) {
		
 		if($item->sku==$val){
 			#echo $item->sku;
 			return $item->stock;

 		}
	}
  return 0;
}

$xml=simplexml_load_file("items.xml") or die("Error: Cannot create object");


$dom = new DOMDocument();

$dom->encoding = 'utf-8';

$dom->xmlVersion = '1.0';

$dom->formatOutput = true;

$xml_file_name = 'products.xml';
$root = $dom->createElement('items');
$i=0;
foreach($xml->children() as $item) {
	$item_node = $dom->createElement('item');
	//$track = $xml->addChild('item');
	  $item_node->appendChild($dom->createElement('number', $item->number ));
	  $nameCZ=strval($item->nameCZ);
	  $item_node->appendChild($dom->createElement('nameCZ',  htmlspecialchars($nameCZ) ));
	    $description=strval($item->description);
	$item_node->appendChild($dom->createElement('description', htmlspecialchars($description)));
	 $manufacturer=strval($item->manufacturer);
	 $item_node->appendChild(  $dom->createElement('manufacturer',$manufacturer));
	$item_node->appendChild( $dom->createElement('barcode', strval($item->barcode) ));
	  $item_node->appendChild($dom->createElement('image', strval($item->image)));
	  #$no=(int)$item->number;
	  $item_node->appendChild( $dom->createElement('stock', chkStock((int)$item->number)));
	  #die();
	  $root->appendChild($item_node);
	  $i++;
}
$dom->appendChild($root);

	$dom->save($xml_file_name);

	echo "$i items to $xml_file_name has been successfully created";
?>
