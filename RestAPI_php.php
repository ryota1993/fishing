<?php

$data = array(
    'feature'=> array(
              'season'=> 1,

    )
);
$data_json = json_encode($data);

$ch = curl_init();
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
curl_setopt($ch, CURLOPT_POSTFIELDS, $data_json);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_URL, 'http://192.168.128.215:5000/fish');
curl_setopt($ch, CURLOPT_PORT, 5000);
$result=curl_exec($ch);
$res_json = json_decode($result , true );
echo 'Testing:'.$res_json;
curl_close($ch);

?>
