#soal 1:
Nama=input("Masukkan nama mahasiswa:")
NIM=input("Masukkan NIM-nya:")
c=int(NIM[2:4])
if ((int(str(NIM)[2:4]) ==20 or 21 or 22 ) and ((int(str(NIM)[:2]) ==71))):
    print(Nama+(" merupakan mahasiswa informatika angkatan 20 hingga 22"))
else:
    print(Nama+(" bukan mahasiswa informatika angkatan 20 hingga 22"))
