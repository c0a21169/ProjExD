import tkinter as tk
import tkinter.messagebox as tkm

#3
def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        siki = entry.get()
        res = eval(siki)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res) 
    else:
        #tkm.showinfo("",f"{num}ボタンがクリックされました")

        #6
        entry.insert(tk.END, num)


#1
root = tk.Tk()
root.title("電卓")
root.geometry("400x500")

#4
entry = tk.Entry(root,justify = "right",width=10,font=("",40))
entry.grid(row=0,column=0,columnspan=3)

#2
r, c = 1 ,0
operands = [7,8,9,4,5,6,1,2,3,0]
for num in operands:
    button = tk.Button(root, text=f"{num}",width=4,height=2,font=("",30))
    button.grid(row=r, column=c)
    button.bind("<1>",button_click)
    c += 1
    if c%3 ==0:
        r += 1
        c=0
        

#5
operators = ["+","="]
for ope in operators:
    button = tk.Button(root, text=f"{ope}",width=4,height=2,font=("",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c+=1
    if c%3 ==0:
        r += 1
        c=0
    
        

#functions = ["C","AC"]
#r,c = 4,1
#for fnc in functions:
    #button = tk.Button(root, text=f"{fnc}",width=4,height=2,font=("",30))
    #button.grid(row=r,column=c)
    #button.bind("<1>",button_click)
    #c += 1

root.mainloop()