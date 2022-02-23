// Program OOP - C#


//Class Program
internal class Program{
    //Main Method
    public static void Main(string[] args){
        //Object dari Class Mahasiswa
        mahasiswa mhs = new mahasiswa();
        mhs.nama = "Eko";
        mhs.nim = "201420001";
        mhs.alamat = "Jl. Binawaluya";
        mhs.matkul = "Object Oriented Programming";
        mhs.hari = "Selasa - Rabu";
        mhs.dataMhs();
    }
}

// Class mahasiswa
public class mahasiswa {
    //Atribut
    public string nama;
    public string nim;
    public string alamat;
    public string hari;
    public string matkul;

    //Method
    public void dataMhs(){
        Console.WriteLine("Nama : "+ nama);
        Console.WriteLine("NIM : "+ nim);
        Console.WriteLine("Alamat : "+ alamat);
        Console.WriteLine("Sedang belajar : "+ matkul +" "+ "pada hari :"+ hari);
        Console.ReadKey();
    }
}
