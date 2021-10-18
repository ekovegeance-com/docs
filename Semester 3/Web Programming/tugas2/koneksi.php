<!-- Membuat koneksi ke database localhost -->
<?php
$host = "localhost";
$user = "root";
$pass = "";
$db = "webprogramming";


$koneksi = mysqli_connect($host, $user, $pass, $db);


if(!$koneksi){
    die("Koneksi Gagal".mysqli_connect_error());
}
?>