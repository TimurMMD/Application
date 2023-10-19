import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('800x800')
        self.window.title("What to wear")
        #Starting label with the text
        self.label = tk.Label(self.window,
                              text="Pick the appropriate parameters",
                              font=('Times New Roman', 18))
        self.label.pack(padx=15, pady=15)

        #Making radio button for gender
        self.label = tk.Label(self.window,
                              text="Choose your gender",
                              font=('Times New Roman', 16))
        self.label.pack(padx=15, pady=15)

        self.radio_gender_state = tk.IntVar()
        self.radio_men = tk.Radiobutton(self.window,
                                        text="Male",
                                        font=('Times New Roman', 14),
                                        variable=self.radio_gender_state,
                                        value=0)
        self.radio_men.pack()

        self.radio_women = tk.Radiobutton(self.window,
                                        text="Female",
                                        font=('Times New Roman', 14),
                                        variable=self.radio_gender_state,
                                        value=1)
        self.radio_women.pack(padx=10)
        #Making the choose of the period
        self.label = tk.Label(self.window,
                              text="Choose the period",
                              font=('Times New Roman', 16))
        self.label.pack(padx=15, pady=15)

        self.radio_period_state = tk.IntVar()
        self.radio_winter = tk.Radiobutton(self.window,
                                           text="Winter",
                                           font=('Times New Roman', 14),
                                           variable=self.radio_period_state,
                                           value=0)
        self.radio_summer = tk.Radiobutton(self.window,
                                           text="Summer",
                                           font=('Times New Roman', 14),
                                           variable=self.radio_period_state,
                                           value=1)
        self.radio_inter_season = tk.Radiobutton(self.window,
                                           text="Inter-Season",
                                           font=('Times New Roman', 14),
                                           variable=self.radio_period_state,
                                           value=2)
        self.radio_winter.pack()
        self.radio_summer.pack()
        self.radio_inter_season.pack()
        #Making the choose of the age
        self.label = tk.Label(self.window,
                              text="Choose the age",
                              font=('Times New Roman', 16))
        self.label.pack(padx=15, pady=15)

        #Making a list of age groups
        self.age_list = ["15-29", "30-48", "48+"]
        self.radio_age_state = tk.IntVar()
        for i in range(len(self.age_list)):
            self.radio_age = tk.Radiobutton(self.window,
                                            text=self.age_list[i],
                                            font=('Times New Roman', 14),
                                            variable=self.radio_age_state,
                                            value=i)
            self.radio_age.pack()

        #Making a button
        self.button = tk.Button(self.window,
                                text="Show",
                                font=('Times New Roman', 16),
                                width=8,
                                height=2,
                                command=self.click)
        self.button.pack()
        self.canvas = tk.Canvas(width = 300, height = 300)
        self.canvas.pack()
        #Images
        try:
            self.image_000 = ImageTk.PhotoImage(Image.open("m15_000.jpg").resize((300, 300)))
            self.image_001 = ImageTk.PhotoImage(Image.open("m30_001.jpg").resize((300, 300)))
            self.image_002 = ImageTk.PhotoImage(Image.open("m48_002.jpg").resize((300, 300)))
            self.image_010 = ImageTk.PhotoImage(Image.open("m15_010.jpg").resize((300, 300)))
            self.image_011 = ImageTk.PhotoImage(Image.open("m30_011.jpg").resize((300, 300)))
            self.image_012 = ImageTk.PhotoImage(Image.open("m48_012.jpg").resize((300, 300)))
            self.image_020 = ImageTk.PhotoImage(Image.open("m15_020.jpg").resize((300, 300)))
            self.image_021 = ImageTk.PhotoImage(Image.open("m30_021.png").resize((300, 300)))
            self.image_022 = ImageTk.PhotoImage(Image.open("m48_022.jpg").resize((300, 300)))
            self.image_100 = ImageTk.PhotoImage(Image.open("w15_100.jpg").resize((300, 300)))
            self.image_101 = ImageTk.PhotoImage(Image.open("w30_101.jpg").resize((300, 300)))
            self.image_102 = ImageTk.PhotoImage(Image.open("w48_102.jpg").resize((300, 300)))
            self.image_110 = ImageTk.PhotoImage(Image.open("w15_110.jpg").resize((300, 300)))
            self.image_111 = ImageTk.PhotoImage(Image.open("w30_111.jpg").resize((300, 300)))
            self.image_112 = ImageTk.PhotoImage(Image.open("w48_112.jpg").resize((300, 300)))
            self.image_120 = ImageTk.PhotoImage(Image.open("w15_120.jpg").resize((300, 300)))
            self.image_121 = ImageTk.PhotoImage(Image.open("w30_121.jpg").resize((300, 300)))
            self.image_122 = ImageTk.PhotoImage(Image.open("w48_122.jpg").resize((300, 300)))
        except FileNotFoundError:
            print("Error loading image")

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    #Condition to decide what image should be shown
    def click(self):
        if self.radio_gender_state.get() == 0 and self.radio_period_state.get() == 0 and self.radio_age_state.get() == 0:

            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_000)
        elif self.radio_gender_state.get() == 0 and self.radio_period_state.get() == 0 and self.radio_age_state.get() == 1:

            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_001)
        elif self.radio_gender_state.get() == 0 and self.radio_period_state.get() == 0 and self.radio_age_state.get() == 2:

            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_002)
        elif self.radio_gender_state.get() == 0 and self.radio_period_state.get() == 1 and self.radio_age_state.get() == 0:

            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_010)
        elif self.radio_gender_state.get() == 0 and self.radio_period_state.get() == 1 and self.radio_age_state.get() == 1:

            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_011)
        elif self.radio_gender_state.get() == 0 and self.radio_period_state.get() == 1 and self.radio_age_state.get() == 2:

            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_012)
        elif self.radio_gender_state.get() == 0 and self.radio_period_state.get() == 2 and self.radio_age_state.get() == 0:

            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_020)
        elif self.radio_gender_state.get() == 0 and self.radio_period_state.get() == 2 and self.radio_age_state.get() == 1:

            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_021)
        elif self.radio_gender_state.get() == 0 and self.radio_period_state.get() == 2 and self.radio_age_state.get() == 2:

            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_022)
        elif self.radio_gender_state.get() == 1 and self.radio_period_state.get() == 0 and self.radio_age_state.get() == 0:

            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_100)
        elif self.radio_gender_state.get() == 1 and self.radio_period_state.get() == 0 and self.radio_age_state.get() == 1:

            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_101)
        elif self.radio_gender_state.get() == 1 and self.radio_period_state.get() == 0 and self.radio_age_state.get() == 2:

            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_102)
        elif self.radio_gender_state.get() == 1 and self.radio_period_state.get() == 1 and self.radio_age_state.get() == 0:
            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_110)
        elif self.radio_gender_state.get() == 1 and self.radio_period_state.get() == 1 and self.radio_age_state.get() == 1:
            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_111)
        elif self.radio_gender_state.get() == 1 and self.radio_period_state.get() == 1 and self.radio_age_state.get() == 2:
            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_112)
        elif self.radio_gender_state.get() == 1 and self.radio_period_state.get() == 2 and self.radio_age_state.get() == 0:
            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_120)
        elif self.radio_gender_state.get() == 1 and self.radio_period_state.get() == 2 and self.radio_age_state.get() == 1:
            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_121)
        elif self.radio_gender_state.get() == 1 and self.radio_period_state.get() == 2 and self.radio_age_state.get() == 2:
            self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image_122)
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.window.destroy()

Application()
