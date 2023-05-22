import tkinter
from PIL import Image, ImageTk
import result

class App:
    def __init__(self):
        self.root = tkinter.Tk()

        self.frame = tkinter.Frame(self.root)
        self.frame.grid()

        self.label = tkinter.Label(self.frame, text="Введите путь к изображению").grid(row=1, column=1)
        self.enter = tkinter.Entry(self.frame, width=70)
        self.enter.grid(row=2, column=1)

        self.but = tkinter.Button(self.frame, text="Поменять изображение", command=self.button_press).grid(row=3, column=1)

        self.canvas = tkinter.Canvas(self.root, height=300, width=350)
        self.canvas.grid(row=1, column=2)
        self.root.mainloop()

    def button_press(self):
        self.path = self.enter.get()
        print(self.path)
        self.image = Image.fromarray(result.image_to_res(self.path))    
        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=2, column=1)

app= App()