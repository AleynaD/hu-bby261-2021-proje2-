from random import randint
from tkinter import *
from tkinter import messagebox

class sayisalLoto:
    count=0
    def __init__(self, anasayfa):
        self.anasayfa = anasayfa
        anasayfa.title("Sayısal Loto")
        anasayfa.geometry("380x340+500+200")
        anasayfa.resizable(False,False)
        anasayfa.config(bg="#e59e60")
        self.baslik = Label(anasayfa, text="---::: Şanslı Numaraların :::---")
        self.baslik.config(font=("Arial", 22))
        self.baslik.grid(row=0,column=0)

        
        self.listeBox = Listbox(anasayfa)
        self.listeBox.config(width=63,bg="white")
        self.listeBox.grid(row=8)

        self.textKutusu = Entry(anasayfa, text="Numaralar oluşturuluyor...",justify='center')
        self.textKutusu.config(width=63,bg="#dfef00")
        self.textKutusu.grid(row=1,column=0)
        
        self.olusturucu = Button(anasayfa, text="Yeni Numara Oluştur", command=self.createNumbers)
        self.olusturucu.config(width=53,bg="#75c407")
        self.olusturucu.grid(row=2,column=0)
        
        self.saveNumber = Button(anasayfa, text="Sayıları Kaydet", command=self.saveNumbers)
        self.saveNumber.grid(row=3,column=0)
        self.saveNumber.config(width=53,bg="#75c407")

        self.kapat = Button(anasayfa, text="Kapat", command=anasayfa.quit)
        self.kapat.grid(row=7,column=0)
        self.kapat.config(width=53,bg="#9b419b")
        
        self.deleteNumbers = Button(anasayfa, text="Seçili Satır Silme", command=self.removeItem)
        self.deleteNumbers.grid(row=4,column=0)
        self.deleteNumbers.config(width=53,bg="red")
        
        self.deleteAllNumbers = Button(anasayfa, text="Bütün Kayıtları Temizle", command=self.allDelete)
        self.deleteAllNumbers.grid(row=5,column=0)
        self.deleteAllNumbers.config(width=53,bg="red")
        
        self.info=Button(anasayfa,text="Bilgilendirme", command=self.information)
        self.info.grid(row=6,column=0)
        self.info.config(width=53)
                                  
    def createNumbers(self):
        i = 0
        self.textKutusu.delete(0, 'end')
        secilenler = [0, 0, 0, 0, 0, 0]
        while i < len(secilenler):
            secilen = randint(1, 49)
            if secilen not in secilenler:
                secilenler[i] = secilen
                i += 1
        sansliNumaralar = str((sorted(secilenler)))
        self.textKutusu.insert(0, sansliNumaralar)
        
    def saveNumbers(self):
        liste =[] 
        liste.append(self.textKutusu.get())
        if self.count<6:
            self.listeBox.insert(self.count+1," ".join(liste))
            self.count+=1
        else:
            messagebox.showinfo("Uyarı","Bu Liste en fazla 6 değer alabilir.")
            pass
        
    def removeItem(self):
        self.listeBox.delete(ANCHOR)
        self.count-=1
    
    def information(self):
        messagebox.showinfo("Yardım Mesajı", message= " Süper Loto, 1 ve 60 arasından 6 adet sayı seçmene dayalı bir oyundur. Seçtiğin her 6 sayı, bir kolon oluşturur. \n Listeleme aracılığıyla geçmiş lotolara bakabilirsiniz. ")
    def allDelete(self):
        self.listeBox.delete(0,'end')
        self.count=0
        
root = Tk()
sayisalLotom = sayisalLoto(root)
root.mainloop()