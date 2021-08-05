<?php

    session_start();

    define("XML_FOLDER", "xml");
    define("CSV_FOLDER", "csv");
    define("CAC", "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2");
    define("CBC", "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2");

    $directory_string = XML;

    $directory_handle = opendir( $directory_string );

    if ( $directory_handle )
    {
        // GET FILES

        $files = array_diff(scandir($directory_string), array('.', '..'));

        echo 'Total file:'. sizeof($files);
        echo "<br>";

        $i=1;

        foreach ($files as $file_string)
        {
            $full_file_path = $directory_string.'/'.$file_string;
           
            if (file_exists($full_file_path)) 
            {

               try{

                    $xml = simplexml_load_file($full_file_path, NULL, NULL, CAC);
                    if($xml === false){
                        echo $i.'. '.'Unable to load and parse the xml file: ' . $upPath.' <span style="color:red">KO</span>';
                        echo "<br>";

                    }else{
                        $x = pathinfo($file_string, PATHINFO_FILENAME);
                        
                        $upPath = CSV_FOLDER.'/'.$x.'.csv';

                        $f = fopen($upPath, 'w'); 

                        chmod($f, 0777); 
                      
                        createCsv($xml, $f);
                        
                        fclose($f);

                        echo $i.'. '.$upPath.' <span style="color:green">OK</span>';
                        echo "<br>";
                    }

                   

                
               }catch(\Throwable $e){

                    echo $i.'. '.$e->getMessage().' <span style="color:red">KO</span>';
                    echo "<br>";
                
               }
               

            }
            $i++;

            //sleep(1);
        }
    }

    // NO MORE FILES? CLOSE THE DIRECTORY
    closedir( $directory_handle );


    function createCsv($xml,$f)
    {
        $put_arr = array('Header','Data');
        fputcsv($f, $put_arr ,',','"');
        
        $cbc = CBC;



        $invo = $xml->AdditionalDocumentReference->children($cbc);



        $put_arr = array(str_replace('_', ' ', 'Voucher_ID'),(string) $invo->ID);
        fputcsv($f, $put_arr ,',','"');

        $regname = $xml->AccountingSupplierParty->Party->PartyLegalEntity->children($cbc);
       
        $put_arr = array('Company Name',(string) $regname->RegistrationName);
        fputcsv($f, $put_arr ,',','"'); 

        $iden = $xml->AccountingSupplierParty->Party->PartyIdentification->children($cbc);
       
        $put_arr = array('VAT nr.',(string) $iden->ID);
        fputcsv($f, $put_arr ,',','"'); 

        $inv = $xml->children($cbc);
      
        $put_arr = array('Voucher Number',(string) $inv->ID);
        fputcsv($f, $put_arr ,',','"'); 

       
        $put_arr = array('Invoice Data',(string) date('d/m/Y', strtotime($inv->IssueDate)));
        fputcsv($f, $put_arr ,',','"'); 

        
        $put_arr = array('Currency',$inv->DocumentCurrencyCode);
        fputcsv($f, $put_arr ,',','"'); 

        $invline = $xml->InvoiceLine;

        $index = 1;

        foreach ($invline as $item)
        {

            $unit = (string) $item->children($cbc)->InvoicedQuantity->attributes()->{'unitCode'};

            $put_arr = array('Article Number-Item '.$index,$index-1);
            fputcsv($f, $put_arr ,',','"'); 

            $put_arr = array('Description-Item '.$index,(string) $item->Item->children($cbc)->Name);
            fputcsv($f, $put_arr ,',','"'); 
            
            $put_arr = array('Quantity-Item '.$index, str_replace('.', ',', (string) $item->children($cbc)->InvoicedQuantity));
            fputcsv($f, $put_arr ,',','"'); 

            $put_arr = array('Unit measure-Item '.$index, ($unit == 'EA' ? 'stk' : $unit));
            fputcsv($f, $put_arr ,',','"');

            $put_arr = array('Unit Price-Item  '.$index, str_replace('.', ',', (string) $item->Price->children($cbc)->PriceAmount));
            fputcsv($f, $put_arr ,',','"');

            $put_arr = array('Amount-Item '.$index, str_replace('.', ',', (string) $item->Price->children($cbc)->PriceAmount));
            fputcsv($f, $put_arr ,',','"');

            $put_arr = array('Line Sum-Item '.$index, str_replace('.', ',', (string) $item->children($cbc)->LineExtensionAmount));
            fputcsv($f, $put_arr ,',','"');

            $put_arr = array('Vat percentage '.$index, str_replace('.', ',', (string) $item->TaxTotal->TaxSubtotal->TaxCategory->children($cbc)->Percent));
            fputcsv($f, $put_arr ,',','"');
            
            $put_arr = array('VAT-Item '.$index, str_replace('.', ',', (string) $item->TaxTotal->children($cbc)->TaxAmount));
            fputcsv($f, $put_arr ,',','"');

            $index++;
        }

        $totalexl = $xml->LegalMonetaryTotal->children($cbc)->TaxExclusiveAmount;
        $put_arr = array('Total Amount Excl vat ', str_replace('.', ',', (string) $totalexl));
        fputcsv($f, $put_arr ,',','"');

        $totalinc = $xml->LegalMonetaryTotal->children($cbc)->TaxInclusiveAmount;
        $put_arr = array('Total amount incl vat ', str_replace('.', ',', (string) $totalinc));
        fputcsv($f, $put_arr ,',','"');


        $pay = $xml->PaymentMeans;
       
        $put_arr = array('Payment Date ', (string) date('d/m/Y', strtotime($pay->children($cbc)->PaymentDueDate)));
        fputcsv($f, $put_arr ,',','"');

      
        $put_arr = array('Payment code ID', (string) $pay->children($cbc)->PaymentID);
        fputcsv($f, $put_arr ,',','"');   

      
        $put_arr = array('Payment ID ', (string) ((int)$pay->children($cbc)->InstructionID));
        fputcsv($f, $put_arr ,',','"');   

        

        $put_arr = array('Join Payment ID ', (string)  ($pay->CreditAccount->length == 0 ? '' : (string) $pay->CreditAccount->children($cbc)->AccountID));
        

        fputcsv($f, $put_arr ,',','"');   

        foreach ($pay as $item)
        {
            if($item->children($cbc)->PaymentChannelCode == "DK:BANK"){

                $put_arr = array('Payment Reg Number ', (string) $item->PayeeFinancialAccount->FinancialInstitutionBranch->children($cbc)->ID);
                fputcsv($f, $put_arr ,',','"');    

                $put_arr = array('Payment Account Number ', (string) $item->PayeeFinancialAccount->children($cbc)->ID);
                fputcsv($f, $put_arr ,',','"'); 
            }

            if($item->children($cbc)->PaymentChannelCode == "IBAN"){

                $put_arr = array('Payment IBAN ', (string) $item->PayeeFinancialAccount->children($cbc)->ID);
                fputcsv($f, $put_arr ,',','"');

                $put_arr = array('Payment SWIFT Bic ', (string) $item->PayeeFinancialAccount->FinancialInstitutionBranch->FinancialInstitution->children($cbc)->ID);
                fputcsv($f, $put_arr ,',','"');
            }
        }

    }

?>