import os
import time
import tkinter as tk
form = tk.Tk()

form.title('TULPAR SOFTWARE')
form.geometry('500x100')

def bul_wrapper():
    def bul():
        while True:
            if os.path.isfile(str(dosya_entry.get())) == True:
                break
    bul()
    time.sleep(120)
    os.system("shutdown /s /t 1")
    

dosya_label = tk.Label(text='Dosya yolunu giriniz :')
dosya_label.place(x=20, y=15)

dosya_entry = tk.Entry(form, width = 50)
dosya_entry.place(x=138, y=15)

buton = tk.Button(form,text='Başlat', command=bul_wrapper)
buton.place(x=230, y=60)

form.mainloop()