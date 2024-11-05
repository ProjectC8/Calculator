import tkinter as tk
from tkinter import ttk   

#Main Windows  
root = tk.Tk()
root.title("Калькулятор от Project_C8")
root.geometry("1000x500")
root.configure(bg='Blue Violet')
root.attributes('-alpha',0.9)


# Строка ответа
otv = ttk.Label(text="Ответ",font=('Arial',20))
otv.pack(pady=10)
otv.place(x=100,y=400)

a = tk.IntVar()
b = tk.IntVar()


def pcc():
  a.set(int(entry.get()))  # Преобразовываем текст из entry в целое число и сохраняем в a
def dcc():
  b.set(int(entrys.get()))  # Преобразовываем текст из entrys в целое число и сохраняем в b

   
def slozenie():
 pcc()
 dcc()
 result = a.get() + b.get()    
 otv.config(text="Ответ: " + str(result))
     
def vicitanije():
 pcc()
 dcc()
 result = a.get() - b.get()    
 otv.config(text="Ответ: " + str(result))

def umnoz():
 pcc()
 dcc()
 result = a.get() * b.get()    
 otv.config(text="Ответ: " + str(result))
 
def delen():
 pcc()
 dcc()
 result = a.get() / b.get()    
 otv.config(text="Ответ: " + str(result))

def step():
 pcc()
 dcc()
 result = a.get() ** b.get()    
 otv.config(text="Ответ: " + str(result))

#Первое число
entry = ttk.Entry(root, width=15, font=('Arial',20))
entry.pack(pady=10)
entry.place(x=100,y=80)

#Второе число 
entrys = ttk.Entry(root, width=15, font=('Arial',20))
entrys.pack(pady=10)
entrys.place(x=400,y=80)
    
# Кнопка для подсчета сложения

pluss = ttk.Button(root, text="Сложение", command=slozenie)
pluss.pack(pady=10)
pluss.place(x=100,y=200)

#Кп для вычит
minus = ttk.Button(root, text="Вычитание", command=vicitanije)
minus.pack(pady=10)
minus.place(x=200,y=200)

#Кп для умножения
x =ttk.Button(root, text="Умножение", command=umnoz)
x.pack(pady=10)
x.place(x=300,y=200)

#Кп для деление
y =ttk.Button(root, text="Деление", command=delen)
y.pack(pady=10)
y.place(x=400,y=200)


#Кп для степень
z =ttk.Button(root, text="Возвести в степень", command=step)
z.pack(pady=10)
z.place(x=500,y=200)


#zaciklit
root.mainloop()