from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from form import Form
from tkinter import messagebox

root = Tk()

# inisialisasi list yang dibutuhkan
data = []
location = []

# isi data pertama
data.append(Form("Dinda", "089678848274", 20,
                 "notebook", "Plain", "Hard Cover", "images/chinese_tom.jpg"))


# function untuk membuka gambar
def open():
    global my_image
    root.filename = filedialog.askopenfilename(
        initialdir="/", title="Select a File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    location.append(root.filename)
    my_label = Label(frame, text=location).grid(
        row=9, column=3, padx=8)


# menyimpan data
def submit():

    # gabung untuk isi checkbox
    gabung = ""

    # kondisi awal cek
    cek = 1

    # pengecekan jika masih ada yang belum terisi
    if(var1.get() != '0'):
        gabung = var1.get()
        cek = 0

    if(var2.get() != '0'):
        gabung += ", " + var2.get()
        cek = 0

    if(var3.get() != '0'):
        gabung += ", " + var3.get()
        cek = 0

    if(en1.get() == "" or en2.get() == "" or en3.get() == "" or (not location)):
        cek = 1

    # kalo data nya udah keisi semua cek nya adalah 0
    if cek == 0:
        data.append(Form(en1.get(), en2.get(), en3.get(),
                         clicked.get(), gabung, rb.get(), location[-1]))

        # membuat message box
        response = messagebox.showinfo(
            "Info", "Data berhasil di simpan")
    else:
        # kalo ada data yang kosong
        response = messagebox.showinfo(
            "Warning", "Ada data yang masing kosong")


# ketika button klik semua submissions
def seeAll():
    top = Toplevel()
    d_frame = LabelFrame(top, text="All Submissions", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # buat nampilin judul
    a1 = Label(d_frame, text="No", width=5,
               borderwidth=1, relief="solid")
    a1.grid(row=0, column=0)

    a2 = Label(d_frame, text="Nama", width=15,
               borderwidth=1, relief="solid")
    a2.grid(row=0, column=1)

    telp = Label(d_frame, text="Telp", width=15,
                 borderwidth=1, relief="solid")
    telp.grid(row=0, column=2)

    jumlah = Label(d_frame, text="Jumlah", width=5,
                   borderwidth=1, relief="solid")
    jumlah.grid(row=0, column=3)

    jenis = Label(d_frame, text="Jenis", width=15,
                  borderwidth=1, relief="solid")
    jenis.grid(row=0, column=4)

    kertas = Label(d_frame, text="Kertas", width=30,
                   borderwidth=1, relief="solid")
    kertas.grid(row=0, column=5)

    cover = Label(d_frame, text="Cover", width=15,
                  borderwidth=1, relief="solid")
    cover.grid(row=0, column=6)

    image = Label(d_frame, text="Lokasi Gambar", width=30,
                  borderwidth=1, relief="solid")
    image.grid(row=0, column=7)

    # perulangan sebanyak data
    index = 1
    for h in data:
        # menampilkan data
        idx = Label(d_frame, text=str(index), width=5,
                    borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        nama = Label(d_frame, text=h.get_nama(), width=15,
                     borderwidth=1, relief="solid")
        nama.grid(row=index, column=1)

        telp = Label(d_frame, text=h.get_telp(), width=15,
                     borderwidth=1, relief="solid")
        telp.grid(row=index, column=2)

        jumlah = Label(d_frame, text=h.get_jumlah(), width=5,
                       borderwidth=1, relief="solid")
        jumlah.grid(row=index, column=3)

        jenis = Label(d_frame, text=h.get_jenis(), width=15,
                      borderwidth=1, relief="solid")
        jenis.grid(row=index, column=4)

        kertas = Label(d_frame, text=h.get_kertas(), width=30,
                       borderwidth=1, relief="solid")
        kertas.grid(row=index, column=5)

        cover = Label(d_frame, text=h.get_cover(), width=15,
                      borderwidth=1, relief="solid")
        cover.grid(row=index, column=6)

        image = Label(d_frame, text=h.get_gambar(), width=30,
                      borderwidth=1, relief="solid")
        image.grid(row=index, column=7)

        index += 1

    # btn exit
    dasar = LabelFrame(top, padx=10, pady=10)
    dasar.pack(padx=10, pady=10)

    btn_exit = Button(dasar, text="Exit", command=top.destroy)
    btn_exit.grid(row=0, column=0)


# menampilkan about aplikasi dan pembuat aplikasi
def about():
    top = Toplevel()
    d_frame = LabelFrame(top, text="About", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="C U S T O M  Y O U R  B O O K !!\n Aplikasi untuk memesan buku secara custom.\n\n Nama : Dinda Wahyu Rahmadani \n NIM : 1901012",
                      anchor="w").grid(row=0, column=0, sticky="w")

    dasar = LabelFrame(top, padx=10, pady=10)
    dasar.pack(padx=10, pady=10)

    btn_exit = Button(dasar, text="Exit", command=top.destroy)
    btn_exit.grid(row=0, column=0)


# menghapus semua data
def clear():
    response = messagebox.showinfo(
        "Warning", "Yakin ingin menghapus semua data?")
    print("ini respon " + response)
    if response == "ok":
        del data[:]
        response = messagebox.showinfo(
            "Info", "Seluruh data berhasil dihapus")


# keluar program
def exit():
    response = messagebox.showinfo("Exit", "Yakin ingin keluar?")
    if response == "ok":
        root.quit()


# buat wadah form namanya frame
frame = LabelFrame(root, text="Form", padx=10, pady=10)
frame.pack(padx=10, pady=10)

# input 1
lbl1 = Label(frame, text="Nama : ", anchor="w", width=10).grid(
    row=0, column=0, sticky="w")
en1 = Entry(frame, width=35, borderwidth=5)
en1.insert(0, "")
en1.grid(
    row=0, column=1, pady=2, columnspan=3, sticky="w")

# input 2
lbl2 = Label(frame, text="Telp : ", anchor="w").grid(
    row=1, column=0, sticky="w")
en2 = Entry(frame, width=35, borderwidth=5)
en2.insert(0, "")
en2.grid(
    row=1, column=1, pady=2, columnspan=3, sticky="w")

# input3
lbl3 = Label(frame, text="Jumlah : ", anchor="w").grid(
    row=2, column=0, sticky="w")
en3 = Entry(frame, width=35, borderwidth=5)
en3.insert(0, "")
en3.grid(
    row=2, column=1, pady=2, columnspan=3, sticky="w")

options = [
    "Binder",
    "Diary",
    "Notebook",
    "Notes"
]

clicked = StringVar()
clicked.set(options[0])

lbl3 = Label(frame, text="Jenis : ", anchor="w").grid(
    row=3, column=0, sticky="w")

drop = OptionMenu(frame, clicked, *options)
drop.grid(row=3, column=1, sticky="w",  pady=2)

# check box
lbl4 = Label(frame, text="Kertas : ", anchor="w").grid(
    row=4, column=0, sticky="w",  pady=2)

var1 = StringVar()
c = Checkbutton(frame, text="Plain",
                variable=var1, onvalue="Plain")
c.deselect()
c.grid(row=4, column=1, sticky="w")

var2 = StringVar()
c2 = Checkbutton(frame, text="Grid",
                 variable=var2, onvalue="Grid")
c2.deselect()
c2.grid(row=4, column=2, sticky="w")

var3 = StringVar()
c3 = Checkbutton(frame, text="Dooted",
                 variable=var3, onvalue="Dooted")
c3.deselect()
c3.grid(row=4, column=3, sticky="w")


# radio button
JENIS = [
    ("Hard Cover", "Hard Cover"),
    ("Kulit", "Kulit"),
]

rb = StringVar()
rb.set("Hard Cover")

lbl5 = Label(frame, text="Cover : ", anchor="w").grid(
    row=5, column=0, sticky="w",  pady=2)

i = 1
for text, cover, in JENIS:
    Radiobutton(frame, text=text, variable=rb,
                value=cover).grid(row=5, column=i, sticky="w", pady=4)
    i += 1

# btn image
btnImage = Button(frame, text="O P E N  F O T O  F I L E",
                  width=35, command=open)
btnImage.grid(row=9, column=0, columnspan=3, sticky="w", padx=8)
my_label = Label(frame, text="location").grid(
    row=9, column=3, padx=8)

# btn submit
myButton = Button(frame, text="S U B M I T", width=45, command=submit)
myButton.grid(row=10, column=0, columnspan=4, pady=8)

# ---------------------------------------------------------------------------------------
kanan = LabelFrame(root, padx=10, pady=10)
kanan.pack(padx=10, pady=10)

lbl5 = Label(kanan, text="C U S T O M  Y O U R  B O O K !!", anchor="w").grid(
    row=1, column=0, sticky="w",  pady=2)

lbl5 = Label(kanan, text="Aplikasi untuk memesan buku secara custom.", anchor="w").grid(
    row=2, column=0, sticky="w",  pady=(2, 30))

# btn see all
btnSeeAll = Button(kanan, text="S E E  A L L  S U B M I S S I O N S",
                   width=45, command=seeAll)
btnSeeAll.grid(row=3, column=0, columnspan=4, padx=8)

# btn clear
btnClear = Button(kanan, text="C L E A R  S U B M I S S I O N S",
                  width=45, command=clear)
btnClear.grid(row=4, column=0, columnspan=4, pady=8)

# btn about
btnAbout = Button(kanan, text="A B O U T",
                  width=45, command=about)
btnAbout.grid(row=5, column=0, columnspan=4, padx=8)

# btn exit
btnExit = Button(kanan, text="E X I T", width=45, command=exit)
btnExit.grid(row=6, column=0, columnspan=4, pady=8)


root.mainloop()
