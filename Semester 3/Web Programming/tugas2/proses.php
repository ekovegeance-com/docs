<?php
include 'koneksi.php'; 
// Membuat proses untuk menginput data ke database
if(isset($_POST['input'])){
    $nim			= $_POST['nim'];
    $nama			= $_POST['nama'];    
    $tempat_lahir	= $_POST['tempat_lahir'];
    $tgl_lahir  	= $_POST['tgl_lahir'];
    $alamat         = $_POST['alamat'];
    $input			= "INSERT INTO mahasiswa (nim,nama,tempat_lahir,tgl_lahir,alamat) VALUES ('$nim', '$nama', '$tempat_lahir', '$tgl_lahir', '$alamat')";
    $query			= mysqli_query($koneksi, $input);
    if($query){            
        echo "<script>alert('Data berhasil diinputkan!'); window.location='index.html'</script>";
    }else{
        echo "<script>alert('Data gagal diinputkan!'); window.location='index.html'</script>";
    }
}

?>