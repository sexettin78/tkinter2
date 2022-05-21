#tkinteri import ettik
from tkinter import *

#pencere
pencere = Tk()

#Pencere Başlığı
pencere.title("Pencere Başlığı")

#pencere boyutu bide pencerenin konumu xlerde ilk yazılan genişlik sonraki yükseklik    +larda ise ilk ekranın sol tarafına,sağdaki değer ekranın sağ tarafına olan uzaklık
pencere.geometry("500x500+300+100")

#kullanıcının pencereyi büyültmesini veya küçültmesini engelleme (ilk değer en,son değer boy)
pencere.resizable(False,True)

#pencere maximum boyutu 
pencere.maxsize(800,800)

#pencere minimum boyutu
pencere.minsize(150,150)

#pencere değerlerini güncellemek
pencere.update()

#konsola pencere boyutu ve konumunu yazdırmak
print("Pencere boyutu hazırlanıyor...")
en = pencere.winfo_width()
boy = pencere.winfo_height()
sol = pencere.winfo_x()
ust = pencere.winfo_y()
pencere_ici_sol = pencere.winfo_rootx()
pencere_ici_ust = pencere.winfo_rooty()
print("En : "+str(en))
print("Boy : "+str(boy))
print("Sol : "+str(sol))
print("Üst : "+str(ust))
print("Pencere içi sol : "+str(pencere_ici_sol))
print("Pencere içi üst : "+str(pencere_ici_ust))
#Ekran Çözünürlüğünü bulmak
print("Genişlik : "+str(pencere.winfo_screenwidth()))
print("Yükseklik : "+str(pencere.winfo_screenheight()))

#pencerenin açık kalmasını sağladık
mainloop()


#Pencere Türleri,Pencere durumunu ayarlamak için stateyi kullanıyoruz.

#Normal pencere
#pencere.state("normal")

#Büyütülmüş pencere
#pencere.state("zoomed")

#Görev çubuğunda açılan pencere
#pencere.state("iconic")

#Arkaplanda Çalışan/Hiç Gözükmeyen pencere
#pencere.state("withdraw")

#Pencere özelliklerini ayarlamak için wm_attributes'i kullanıyoruz.

#Saydam Pencere 0.5 = %50 saydamlık
#pencere.wm_attributes("-alpha",0.5)

#Her zaman diğer programların önünde olan pencere
#pencere.wm_attributes("-topmost",1)

#Tam Ekran Pencere 
#pencere.wm_attributes("-fullscreen",1)