import tkinter as tk

def main():
   master = tk.Tk()
   tk.Label(master, text="Type your username: ").grid(row=0)
   tk.Label(master, text="Type your password: ").grid(row=1)
   tk.Button(master, text = "Send", command = getValues)
   username = tk.Entry(master, bd=5)
   password = tk.Entry(master, bd=5, show="*")

   username.grid(row=0, column=1)
   password.grid(row=1, column=1)


   info = tk.Tk()
   tk.Label(info, text= password.get()).grid(row=0)
   master.mainloop()
if __name__ == "__main__":
    main()