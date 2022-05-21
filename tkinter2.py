'''

pencere.overriderefirect(1) yazarsan pencere çubuğunu kaldırmış olursun
pencere.winfo_pointerx() = fare imlecinin x eksenindeki konumu
pencere.winfo_pointery() = fare imlecinin y eksenindeki konumu
yazi = Label(text="merhaba tkinter", fg="red") yazıyı kırmızı yapar
yazi = Label(text="merhaba tkinter", bg="red") yazı arkaplanını kırmızı yapar
yazi = Label(text="merhaba tkinter", fg="red", bg="blue", width=15,height=15) yazının kapladığı alanı 15'e 15 olarak belirler
yazi = Label(text="merhaba tkinter", font = ("Open Sans","30","bold")) yazının fontunu ayarlayan parametre
örneğin yazı ekrana sığmıyorsa ve alt satıra geçmesini istiyorsak wraplength = 10 yazarak 10 sınırı koyduk ve sığmayan yerde aşağı geçir dedik
yazıyı sağa yaslamak için justify="right" sola yaslamak için justify="left" ortalamak için justify="center"

yazıyı taşımak için anchor parametresi kullanıyoruz. anchor parametresi değerleri: 
{
    n : yukarı
    s : aşağı
    e : sağ
    w : sol
    ne: yukarı sağ
    nw: yukarı sol
    se: aşağı sağ
    sw: aşağı sol
    center: orta
}

label üstüne gelindiğinde fare imleci değiştirmek : yazi parametresi içine cursor = "ne istersek örneğin cross"

bu kodlar ile arkaplana resim ekleyebilirsin ====>>>>   resim = PhotoImage(file="resim.jpg") /n yazi = Label(text="merhaba tkinter", font = ("Open Sans","30","bold"), cursor="cross",image=resim)

resim ve yazı hizalamak için kullanılan parametre = compound // bu parametreyi compound = "left" vs gibi kullanabilirsin

tuş eklemek için tus = Button(text="tus yazisi", command= mesaj_yaz) yazıyoruz. tuşa basılınca ne olacağını ayarlamak için command parametresine kendi fonksiyonlarımızı atıyoruz.

def yazi_degistir():
    yazi["text"] = "merhabalar" //bu fonksiyonu tuşa atarsak, tuşa basılınca yazıyı değiştirir

bileşen aktifliğini değiştirmek için state parametresi veriyoruz. örneğin state = "disabled" veya da state = "active"

tus.invoke() fonksiyonu yazıldığı yerde, otomatik olarak tuşa basar. mesela program açılışında yazarsak, otomatik olarak program açıldığında tuşa basmış olur

quit() fonksiyonu programı kapatır. tuşa aktarım için kullanılabilir

yazi = Entry() yazarak bir yazı alanı oluşturduk
veri aktarmak için get() fonksiyonunu kullanıyoruz. mesela yazılan değeri tuşa basınca değişkene aktarmak için, yazi.get() = degisken = etiket["text"]

tüm yazı alanını silmek için = yazi.delete(0, "end")
sadece farenin seçildiği alanı silmek = yazi.delete("sel.first","sel.last")
yanıp sönen imleçten yazı sonuna kadar silmek = yazi.delete("insert","end")

kullanıcı yazı girerken veriyi şifrelemek için * ile değiştiriyoruz ya. işte o şöyle yapılıyor ====>>>> yazi = Entry(show="*")

tab ile form elemanları arası geçiş (focus) yapmak için ====>>> yazi = Entry( takefocus = 1 ) yaparız. eğer geçişi engellemek istersek 0 yerine 1 yazarız

liste oluşturmak için >>>> list = Listbox()

listeye eleman eklemek için >> list.insert(END, "eleman1")
burada end yerine 0 yazarsak başa, 3 yazarsak 3.elemanın yerine eklenir
birden çok eleman seçme hakkı için ====>>>> list=Listbox(selectmode = MULTIPLE) 
tek eleman seçme için ====>>>>> list=Listbox(selectmode = BROWSE)

checkbutton oluşturmak için == onay = Checkbutton(text="Onayla")
tuşa basınca işlem yapılması için onay tuşunun değerini bir tuşta depoluyoruz = x=IntVar()
sonra kontrol fonksiyonu içerisine x.get() == 0 ise şunu yap diye koşula bağlıyoruz. 0=seçilmemişse,1=seçilmişse
onay = Chechkbutton(text = "onayla", variable = x, command = kontrol) şeklinde bir atama yapabiliriz.


variable parametresi=burada değeri sakladığımız değişkeni bağlıyoruz
value parametresi=burada buton seçildiğinde değişkene atanacak değeri belirliyoruz
mesela python,php diye 2 tuş oluşturacaksak
python = Radiobutton(text="python",value="python",variable=x,command=yazdir)
python.pack()
php = Radiobutton(text="php",value="php",variable=x,command=yazdir)
php.pack()
şeklinde oluşturabiliriz






'''