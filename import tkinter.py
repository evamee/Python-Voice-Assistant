import tkinter

class calculator:
    def __int__(self):
        self.window = tkinter.Tk()
        self.window.geometry("335x665")
        self.window.resizable(0,0)
        self.window.title("calculator")

    def run(self):
        self.window.mainloop()

if  __name__  =="__main__":
    calc = calculator()
    calc.run()c