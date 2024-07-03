#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pulp import *
import random
from PIL import ImageTk, Image


def WindowCreation():
    global entry1_value, entry2_value, entry3_value, entry4_value, entry5_value, entry6_value, entry7_value, entry8_value, entry9_value, entry10_value, \
        entry11_value, entry12_value, entry13_value, entry14_value, entry15_value, entry16_value, entry17_value, entry18_value, entry19_value, entry20_value, \
        entry21_value, entry22_value, entry23_value, entry24_value, entry25_value, entry26_value, entry27_value, entry28_value, entry29_value, entry30_value, \
        entry31_value, entry32_value, entry71_value, entry72_value, entry73_value, entry74_value, entry75_value, entry76_value, entry77_value, MainWindow

    MainWindow = tk.Tk()
    MainWindow.configure(height=500, width=500)
    MainWindow.geometry("900x800")
    message1 = tk.Message(MainWindow)
    message1.configure(background="#d3d3d3")
    message1.place(anchor="nw", relheight=0.22, relwidth=0.221, relx=0.03, rely=0.03, x=0, y=0)
    label1 = ttk.Label(MainWindow)
    label1.configure(background="#e5e5e5", text='Дані "пацієнта":')
    label1.place(anchor="nw", relheight=0.02, relx=0.092, rely=0.035, x=0, y=0)
    label2 = ttk.Label(MainWindow)
    label2.configure(background="#e5e5e5", text='S1_in:')
    label2.place(anchor="nw", relx=0.07, rely=0.081, x=0, y=0)
    label3 = ttk.Label(MainWindow)
    label3.configure(background="#e5e5e5", text='S2_in:')
    label3.place(anchor="nw", relx=0.07, rely=0.121, x=0, y=0)
    label4 = ttk.Label(MainWindow)
    label4.configure(background="#e5e5e5", text='S3_in:')
    label4.place(anchor="nw", relx=0.07, rely=0.161, x=0, y=0)
    label5 = ttk.Label(MainWindow)
    label5.configure(background="#e5e5e5", text='Q_in:')
    label5.place(anchor="nw", relx=0.07, rely=0.201, x=0, y=0)
    entry1_value = tk.DoubleVar()
    entry1 = ttk.Entry(MainWindow, textvariable=entry1_value)
    entry1.place(anchor="nw", relwidth=0.095, relx=0.11, rely=0.08, x=0, y=0)
    entry2_value = tk.DoubleVar()
    entry2 = ttk.Entry(MainWindow, textvariable=entry2_value)
    entry2.place(anchor="nw", relwidth=0.095, relx=0.11, rely=0.12, x=0, y=0)
    entry3_value = tk.DoubleVar()
    entry3 = ttk.Entry(MainWindow, textvariable=entry3_value)
    entry3.place(anchor="nw", relwidth=0.095, relx=0.11, rely=0.16, x=0, y=0)
    entry4_value = tk.DoubleVar()
    entry4 = ttk.Entry(MainWindow, textvariable=entry4_value)
    entry4.place(anchor="nw", relwidth=0.095, relx=0.11, rely=0.20, x=0, y=0)
    message2 = tk.Message(MainWindow)
    message2.configure(background="#d3d3d3")
    message2.place(anchor="nw", relheight=0.34, relwidth=0.233, relx=0.26, rely=0.03, x=0, y=0)
    label7 = ttk.Label(MainWindow)
    label7.configure(background="#e5e5e5", text='Обмеження:')
    label7.place(anchor="nw", relheight=0.02, relx=0.34, rely=0.035, x=0, y=0)
    label8 = ttk.Label(MainWindow)
    label8.configure(background="#e5e5e5", text='S1_in')
    label8.place(anchor="nw", relx=0.36, rely=0.1, x=0, y=0)
    label9 = ttk.Label(MainWindow)
    label9.configure(background="#e5e5e5", text='S2_in')
    label9.place(anchor="nw", relx=0.36, rely=0.14, x=0, y=0)
    label10 = ttk.Label(MainWindow)
    label10.configure(background="#e5e5e5", text='S3_in')
    label10.place(anchor="nw", relx=0.36, rely=0.18, x=0, y=0)
    label12 = ttk.Label(MainWindow)
    label12.configure(background="#e5e5e5", text='U1')
    label12.place(anchor="nw", relx=0.367, rely=0.22, x=0, y=0)
    label13 = ttk.Label(MainWindow)
    label13.configure(background="#e5e5e5", text='U2')
    label13.place(anchor="nw", relx=0.367, rely=0.26, x=0, y=0)
    label14 = ttk.Label(MainWindow)
    label14.configure(background="#e5e5e5", text='U3')
    label14.place(anchor="nw", relx=0.367, rely=0.30, x=0, y=0)
    entry5 = ttk.Entry(MainWindow)
    entry5_value = tk.DoubleVar()
    entry5.configure(textvariable=entry5_value)
    entry5.place(anchor="nw", relwidth=0.07, relx=0.283, rely=0.1, x=0, y=0)
    entry6 = ttk.Entry(MainWindow)
    entry6_value = tk.DoubleVar()
    entry6.configure(textvariable=entry6_value)
    entry6.place(anchor="nw", relwidth=0.07, relx=0.283, rely=0.14, x=0, y=0)
    entry7 = ttk.Entry(MainWindow)
    entry7_value = tk.DoubleVar()
    entry7.configure(textvariable=entry7_value)
    entry7.place(anchor="nw", relwidth=0.07, relx=0.283, rely=0.18, x=0, y=0)
    entry8 = ttk.Entry(MainWindow)
    entry8_value = tk.DoubleVar()
    entry8.configure(textvariable=entry8_value)
    entry8.place(anchor="nw", relwidth=0.07, relx=0.283, rely=0.22, x=0, y=0)
    entry9 = ttk.Entry(MainWindow)
    entry9_value = tk.DoubleVar()
    entry9.configure(textvariable=entry9_value)
    entry9.place(anchor="nw", relwidth=0.07, relx=0.283, rely=0.26, x=0, y=0)
    entry10 = ttk.Entry(MainWindow)
    entry10_value = tk.DoubleVar()
    entry10.configure(textvariable=entry10_value)
    entry10.place(anchor="nw", relwidth=0.07, relx=0.283, rely=0.30, x=0, y=0)
    entry11 = ttk.Entry(MainWindow)
    entry11_value = tk.DoubleVar()
    entry11.configure(textvariable=entry11_value)
    entry11.place(anchor="nw", relwidth=0.07, relx=0.40, rely=0.1, x=0, y=0)
    entry12 = ttk.Entry(MainWindow)
    entry12_value = tk.DoubleVar()
    entry12.configure(textvariable=entry12_value)
    entry12.place(anchor="nw", relwidth=0.07, relx=0.4, rely=0.14, x=0, y=0)
    entry13 = ttk.Entry(MainWindow)
    entry13_value = tk.DoubleVar()
    entry13.configure(textvariable=entry13_value)
    entry13.place(anchor="nw", relwidth=0.07, relx=0.4, rely=0.18, x=0, y=0)
    entry14 = ttk.Entry(MainWindow)
    entry14_value = tk.DoubleVar()
    entry14.configure(textvariable=entry14_value)
    entry14.place(anchor="nw", relwidth=0.07, relx=0.4, rely=0.22, x=0, y=0)
    entry15 = ttk.Entry(MainWindow)
    entry15_value = tk.DoubleVar()
    entry15.configure(textvariable=entry15_value)
    entry15.place(anchor="nw", relwidth=0.07, relx=0.4, rely=0.26, x=0, y=0)
    entry16 = ttk.Entry(MainWindow)
    entry16_value = tk.DoubleVar()
    entry16.configure(textvariable=entry16_value)
    entry16.place(anchor="nw", relwidth=0.07, relx=0.4, rely=0.3, x=0, y=0)
    label15 = ttk.Label(MainWindow)
    label15.configure(background="#e5e5e5", text='min:')
    label15.place(anchor="nw", relx=0.304, rely=0.07, x=0, y=0)
    label17 = ttk.Label(MainWindow)
    label17.configure(background="#e5e5e5", text='max:')
    label17.place(anchor="nw", relx=0.42, rely=0.07, x=0, y=0)
    message4 = tk.Message(MainWindow)
    message4.configure(background="#e4e4e4")
    message4.place(anchor="nw", relheight=0.34, relwidth=0.465, relx=0.503, rely=0.03, x=0, y=0)
    label18 = ttk.Label(MainWindow)
    label18.configure(background="#d3d3d3", text='Примітка:')
    label18.place(anchor="nw", relheight=0.02, relx=0.7, rely=0.035, x=0, y=0)
    label19 = ttk.Label(MainWindow)
    label19.configure(background="#e5e5e5", text='S1_in - Індекси цін виробництва легкої промисловості')
    label19.place(anchor="nw", relx=0.56, rely=0.075, x=0, y=0)
    label20 = ttk.Label(MainWindow)
    label20.configure(background="#e5e5e5", text='S2_in - Індекси цін виробництва промисловості')
    label20.place(anchor="nw", relheight=0.02, relx=0.56, rely=0.115, x=0, y=0)
    label21 = ttk.Label(MainWindow)
    label21.configure(background="#e5e5e5", text='S3_in - Обсяг виробництва легкої промисловості')
    label21.place(anchor="nw", relheight=0.02, relx=0.56, rely=0.155, x=0, y=0)
    label22 = ttk.Label(MainWindow)
    label22.configure(background="#e5e5e5", text='Q_in - Зайнятість у легкій промисловості')
    label22.place(anchor="nw", relheight=0.02, relx=0.56, rely=0.195, x=0, y=0)
    label23 = ttk.Label(MainWindow)
    label23.configure(background="#e5e5e5", text='U1 - Заробітна плата у легкій промисловості')
    label23.place(anchor="nw", relheight=0.02, relx=0.56, rely=0.235, x=0, y=0)
    label24 = ttk.Label(MainWindow)
    label24.configure(background="#e5e5e5", text='U2 - Роздрібний товарообіг всього')
    label24.place(anchor="nw", relheight=0.02, relx=0.56, rely=0.275, x=0, y=0)
    label25 = ttk.Label(MainWindow)
    label25.configure(background="#e5e5e5", text='U3 - Індекс реальної зарплати')
    label25.place(anchor="nw", relheight=0.02, relx=0.56, rely=0.315, x=0, y=0)
    button1 = ttk.Button(MainWindow, command=SetAveragePatient)
    button1.configure(text='Середній')
    button1.place(anchor="nw", relheight=0.07, relwidth=0.1103, relx=0.029, rely=0.30, x=0, y=0)
    label26 = ttk.Label(MainWindow)
    label26.configure(anchor="center", background="#d3d3d3", justify="center",
                      text='Заповнити середнім або \nвипадковим пацієнтом:')
    label26.place(anchor="nw", relheight=0.041, relwidth=0.221, relx=0.03, rely=0.255, x=0, y=0)
    message5 = tk.Message(MainWindow)
    message5.configure(background="#e4e4e4")
    message5.place(anchor="nw", relheight=0.598, relwidth=0.505, relx=0.03, rely=0.38, x=0, y=0)
    label27 = ttk.Label(MainWindow)
    label27.configure(background="#d3d3d3", text='Коефіцієнти:')
    label27.place(anchor="nw", relheight=0.02, relx=0.25, rely=0.385, x=0, y=0)
    label28 = ttk.Label(MainWindow)
    label28.configure(background="#d3d3d3", text='Q_out')
    label28.place(anchor="nw", relx=0.075, rely=0.43, x=0, y=0)
    label29 = ttk.Label(MainWindow)
    label29.configure(background="#d3d3d3", text='S1_out')
    label29.place(anchor="nw", relx=0.20, rely=0.43, x=0, y=0)
    label30 = ttk.Label(MainWindow)
    label30.configure(background="#d3d3d3", text='S2_out')
    label30.place(anchor="nw", relx=0.32, rely=0.43, x=0, y=0)
    label31 = ttk.Label(MainWindow)
    label31.configure(background="#d3d3d3", text='S3_out')
    label31.place(anchor="nw", relx=0.44, rely=0.43, x=0, y=0)
    message3 = tk.Message(MainWindow)
    message3.configure(background="#e4e4e4")
    message3.place(anchor="nw", relheight=0.25, relwidth=0.423, relx=0.545, rely=0.38, x=0, y=0)
    message6 = tk.Message(MainWindow)
    message6.configure(background="#e4e4e4")
    message6.place(anchor="nw", relheight=0.338, relwidth=0.185, relx=0.545, rely=0.64, x=0, y=0)
    label6 = ttk.Label(MainWindow)
    label6.configure(background="#d3d3d3", text='Результати:')
    label6.place(anchor="nw", relheight=0.02, relx=0.605, rely=0.645, x=0, y=0)
    label11 = ttk.Label(MainWindow)
    label11.configure(background="#e5e5e5", text='U1:')
    label11.place(anchor="nw", relx=0.56, rely=0.705, x=0, y=0)
    label16 = ttk.Label(MainWindow)
    label16.configure(background="#e5e5e5", text='U2:')
    label16.place(anchor="nw", relx=0.56, rely=0.745, x=0, y=0)
    label32 = ttk.Label(MainWindow)
    label32.configure(background="#e5e5e5", text='U3:')
    label32.place(anchor="nw", relx=0.56, rely=0.785, x=0, y=0)
    label33 = ttk.Label(MainWindow)
    label33.configure(background="#e5e5e5", text='S1_out:')
    label33.place(anchor="nw", relx=0.56, rely=0.825, x=0, y=0)
    label34 = ttk.Label(MainWindow)
    label34.configure(background="#e5e5e5", text='S2_out:')
    label34.place(anchor="nw", relx=0.56, rely=0.865, x=0, y=0)
    label35 = ttk.Label(MainWindow)
    label35.configure(background="#e5e5e5", text='S3_out:')
    label35.place(anchor="nw", relx=0.56, rely=0.905, x=0, y=0)
    label36 = ttk.Label(MainWindow)
    label36.configure(background="#e5e5e5", text='Q_out:')
    label36.place(anchor="nw", relx=0.56, rely=0.945, x=0, y=0)
    entry71 = ttk.Entry(MainWindow)
    entry71_value = tk.DoubleVar()
    entry71.configure(state="readonly", textvariable=entry71_value)
    entry71.place(anchor="nw", relwidth=0.1, relx=0.614, rely=0.704, x=0, y=0)
    entry72 = ttk.Entry(MainWindow)
    entry72_value = tk.DoubleVar()
    entry72.configure(state="readonly", textvariable=entry72_value)
    entry72.place(anchor="nw", relwidth=0.1, relx=0.614, rely=0.744, x=0, y=0)
    entry73 = ttk.Entry(MainWindow)
    entry73_value = tk.DoubleVar()
    entry73.configure(state="readonly", textvariable=entry73_value)
    entry73.place(anchor="nw", relwidth=0.1, relx=0.614, rely=0.784, x=0, y=0)
    entry74 = ttk.Entry(MainWindow)
    entry74_value = tk.DoubleVar()
    entry74.configure(state="readonly", textvariable=entry74_value)
    entry74.place(anchor="nw", relwidth=0.1, relx=0.614, rely=0.824, x=0, y=0)
    entry75 = ttk.Entry(MainWindow)
    entry75_value = tk.DoubleVar()
    entry75.configure(state="readonly", textvariable=entry75_value)
    entry75.place(anchor="nw", relwidth=0.1, relx=0.614, rely=0.864, x=0, y=0)
    entry76 = ttk.Entry(MainWindow)
    entry76_value = tk.DoubleVar()
    entry76.configure(state="readonly", textvariable=entry76_value)
    entry76.place(anchor="nw", relwidth=0.1, relx=0.614, rely=0.904, x=0, y=0)
    entry77 = ttk.Entry(MainWindow)
    entry77_value = tk.DoubleVar()
    entry77.configure(state="readonly", textvariable=entry77_value)
    entry77.place(anchor="nw", relwidth=0.1, relx=0.614, rely=0.944, x=0, y=0)
    label37 = ttk.Label(MainWindow)
    label37.configure(background="#d3d3d3", text='Коефіцієнти:')
    label37.place(anchor="nw", relheight=0.02, relx=0.71, rely=0.385, x=0, y=0)
    label38 = ttk.Label(MainWindow)
    label38.configure(background="#e5e5e5", text='S1_out')
    label38.place(anchor="nw", relheight=0.02, relx=0.55, rely=0.45, x=0, y=0)
    label39 = ttk.Label(MainWindow)
    label39.configure(background="#e5e5e5", text='U1')
    label39.place(anchor="nw", relheight=0.02, relx=0.63, rely=0.42, x=0, y=0)
    label40 = ttk.Label(MainWindow)
    label40.configure(background="#e5e5e5", text='S2_out')
    label40.place(anchor="nw", relheight=0.02, relx=0.55, rely=0.5, x=0, y=0)
    label41 = ttk.Label(MainWindow)
    label41.configure(background="#e5e5e5", text='S3_out')
    label41.place(anchor="nw", relheight=0.02, relx=0.55, rely=0.55, x=0, y=0)
    label42 = ttk.Label(MainWindow)
    label42.configure(background="#e5e5e5", text='Q_out')
    label42.place(anchor="nw", relheight=0.02, relx=0.55, rely=0.6, x=0, y=0)
    label43 = ttk.Label(MainWindow)
    label43.configure(background="#e5e5e5", text='U2')
    label43.place(anchor="nw", relheight=0.02, relx=0.72, rely=0.42, x=0, y=0)
    label44 = ttk.Label(MainWindow)
    label44.configure(background="#e5e5e5", text='U3')
    label44.place(anchor="nw", relheight=0.02, relx=0.81, rely=0.42, x=0, y=0)
    label45 = ttk.Label(MainWindow)
    label45.configure(background="#e5e5e5", text='const')
    label45.place(anchor="nw", relheight=0.02, relx=0.89, rely=0.42, x=0, y=0)
    entry17 = ttk.Entry(MainWindow)
    entry17_value = tk.DoubleVar()
    entry17.configure(state="readonly", textvariable=entry17_value)
    entry17.place(anchor="nw", relwidth=0.075, relx=0.60, rely=0.448, x=0, y=0)
    entry18 = ttk.Entry(MainWindow)
    entry18_value = tk.StringVar()
    entry18.configure(state="disabled", textvariable=entry18_value)
    entry18.place(anchor="nw", relwidth=0.075, relx=0.60, rely=0.498, x=0, y=0)
    entry19 = ttk.Entry(MainWindow)
    entry19_value = tk.DoubleVar()
    entry19.configure(state="readonly", textvariable=entry19_value)
    entry19.place(anchor="nw", relwidth=0.075, relx=0.60, rely=0.548, x=0, y=0)
    entry20 = ttk.Entry(MainWindow)
    entry20_value = tk.DoubleVar()
    entry20.configure(state="readonly", textvariable=entry20_value)
    entry20.place(anchor="nw", relwidth=0.075, relx=0.60, rely=0.598, x=0, y=0)
    entry21 = ttk.Entry(MainWindow)
    entry21_value = tk.DoubleVar()
    entry21.configure(state="readonly", textvariable=entry21_value)
    entry21.place(anchor="nw", relwidth=0.075, relx=0.69, rely=0.448, x=0, y=0)
    entry22 = ttk.Entry(MainWindow)
    entry22_value = tk.DoubleVar()
    entry22.configure(state="readonly", textvariable=entry22_value)
    entry22.place(anchor="nw", relwidth=0.075, relx=0.69, rely=0.498, x=0, y=0)
    entry23 = ttk.Entry(MainWindow)
    entry23_value = tk.DoubleVar()
    entry23.configure(state="readonly", textvariable=entry23_value)
    entry23.place(anchor="nw", relwidth=0.075, relx=0.69, rely=0.548, x=0, y=0)
    entry24 = ttk.Entry(MainWindow)
    entry24_value = tk.DoubleVar()
    entry24.configure(state="readonly", textvariable=entry24_value)
    entry24.place(anchor="nw", relwidth=0.075, relx=0.69, rely=0.598, x=0, y=0)
    entry25 = ttk.Entry(MainWindow)
    entry25_value = tk.DoubleVar()
    entry25.configure(state="readonly", textvariable=entry25_value)
    entry25.place(anchor="nw", relwidth=0.075, relx=0.78, rely=0.448, x=0, y=0)
    entry29 = ttk.Entry(MainWindow)
    entry29_value = tk.DoubleVar()
    entry29.configure(state="readonly", textvariable=entry29_value)
    entry29.place(anchor="nw", relwidth=0.075, relx=0.87, rely=0.448, x=0, y=0)
    entry26 = ttk.Entry(MainWindow)
    entry26_value = tk.DoubleVar()
    entry26.configure(state="readonly", textvariable=entry26_value)
    entry26.place(anchor="nw", relwidth=0.075, relx=0.78, rely=0.498, x=0, y=0)
    entry27 = ttk.Entry(MainWindow)
    entry27_value = tk.DoubleVar()
    entry27.configure(state="readonly", textvariable=entry27_value)
    entry27.place(anchor="nw", relwidth=0.075, relx=0.78, rely=0.548, x=0, y=0)
    entry28 = ttk.Entry(MainWindow)
    entry28_value = tk.DoubleVar()
    entry28.configure(state="readonly", textvariable=entry28_value)
    entry28.place(anchor="nw", relwidth=0.075, relx=0.78, rely=0.598, x=0, y=0)
    entry30 = ttk.Entry(MainWindow)
    entry30_value = tk.DoubleVar()
    entry30.configure(state="readonly", textvariable=entry30_value)
    entry30.place(anchor="nw", relwidth=0.075, relx=0.87, rely=0.498, x=0, y=0)
    entry31 = ttk.Entry(MainWindow)
    entry31_value = tk.DoubleVar()
    entry31.configure(state="readonly", textvariable=entry31_value)
    entry31.place(anchor="nw", relwidth=0.075, relx=0.87, rely=0.548, x=0, y=0)
    entry32 = ttk.Entry(MainWindow)
    entry32_value = tk.DoubleVar()
    entry32.configure(state="readonly", textvariable=entry32_value)
    entry32.place(anchor="nw", relwidth=0.075, relx=0.87, rely=0.598, x=0, y=0)
    button3 = ttk.Button(MainWindow, command=calculate)
    button3.configure(text='Розрахунок')
    button3.place(anchor="nw", relheight=0.165, relwidth=0.23, relx=0.7378, rely=0.64, x=0, y=0)
    entry33 = ttk.Entry(MainWindow)
    entry33_value = tk.StringVar(value='352,605')
    entry33.configure(state="readonly", textvariable=entry33_value)
    _text_ = '352,605'
    entry33["state"] = "normal"
    entry33.delete("0", "end")
    entry33.insert("0", _text_)
    entry33["state"] = "readonly"
    entry33.place(anchor="nw", relwidth=0.07, relx=0.085, rely=0.47, x=0, y=0)
    entry34 = ttk.Entry(MainWindow)
    entry34_value = tk.StringVar(value='0,872')
    entry34.configure(state="readonly", textvariable=entry34_value)
    _text_ = '0,872'
    entry34["state"] = "normal"
    entry34.delete("0", "end")
    entry34.insert("0", _text_)
    entry34["state"] = "readonly"
    entry34.place(anchor="nw", relwidth=0.07, relx=0.085, rely=0.511, x=0, y=0)
    entry35 = ttk.Entry(MainWindow)
    entry35_value = tk.StringVar(value='0,0004')
    entry35.configure(state="readonly", textvariable=entry35_value)
    _text_ = '0,0004'
    entry35["state"] = "normal"
    entry35.delete("0", "end")
    entry35.insert("0", _text_)
    entry35["state"] = "readonly"
    entry35.place(anchor="nw", relwidth=0.07, relx=0.085, rely=0.551, x=0, y=0)
    label46 = ttk.Label(MainWindow)
    label46.configure(background="#e5e5e5", text='const:')
    label46.place(anchor="nw", relx=0.04, rely=0.471, x=0, y=0)
    label47 = ttk.Label(MainWindow)
    label47.configure(background="#e5e5e5", text='Q_in:')
    label47.place(anchor="nw", relx=0.04, rely=0.512, x=0, y=0)
    label48 = ttk.Label(MainWindow)
    label48.configure(background="#e5e5e5", text='X24:')
    label48.place(anchor="nw", relx=0.04, rely=0.552, x=0, y=0)
    label49 = ttk.Label(MainWindow)
    label49.configure(background="#e5e5e5", text='const:')
    label49.place(anchor="nw", relx=0.165, rely=0.471, x=0, y=0)
    entry44 = ttk.Entry(MainWindow)
    entry44_value = tk.StringVar(value='12,668')
    entry44.configure(state="readonly", textvariable=entry44_value)
    _text_ = '12,668'
    entry44["state"] = "normal"
    entry44.delete("0", "end")
    entry44.insert("0", _text_)
    entry44["state"] = "readonly"
    entry44.place(anchor="nw", relwidth=0.07, relx=0.21, rely=0.47, x=0, y=0)
    label50 = ttk.Label(MainWindow)
    label50.configure(background="#e5e5e5", text='S2_in:')
    label50.place(anchor="nw", relx=0.165, rely=0.512, x=0, y=0)
    label51 = ttk.Label(MainWindow)
    label51.configure(background="#e5e5e5", text='X51:')
    label51.place(anchor="nw", relx=0.165, rely=0.552, x=0, y=0)
    entry45 = ttk.Entry(MainWindow)
    entry45_value = tk.StringVar(value='0,862')
    entry45.configure(state="readonly", textvariable=entry45_value)
    _text_ = '0,862'
    entry45["state"] = "normal"
    entry45.delete("0", "end")
    entry45.insert("0", _text_)
    entry45["state"] = "readonly"
    entry45.place(anchor="nw", relwidth=0.07, relx=0.21, rely=0.511, x=0, y=0)
    entry46 = ttk.Entry(MainWindow)
    entry46_value = tk.StringVar(value='-0,063')
    entry46.configure(state="readonly", textvariable=entry46_value)
    _text_ = '-0,063'
    entry46["state"] = "normal"
    entry46.delete("0", "end")
    entry46.insert("0", _text_)
    entry46["state"] = "readonly"
    entry46.place(anchor="nw", relwidth=0.07, relx=0.21, rely=0.551, x=0, y=0)
    label52 = ttk.Label(MainWindow)
    label52.configure(background="#e5e5e5", text='const:')
    label52.place(anchor="nw", relx=0.289, rely=0.471, x=0, y=0)
    entry51 = ttk.Entry(MainWindow)
    entry51_value = tk.StringVar(value='114,541')
    entry51.configure(state="readonly", textvariable=entry51_value)
    _text_ = '114,541'
    entry51["state"] = "normal"
    entry51.delete("0", "end")
    entry51.insert("0", _text_)
    entry51["state"] = "readonly"
    entry51.place(anchor="nw", relwidth=0.07, relx=0.334, rely=0.47, x=0, y=0)
    label53 = ttk.Label(MainWindow)
    label53.configure(background="#e5e5e5", text='S2_in:')
    label53.place(anchor="nw", relx=0.289, rely=0.512, x=0, y=0)
    label54 = ttk.Label(MainWindow)
    label54.configure(background="#e5e5e5", text='X42:')
    label54.place(anchor="nw", relx=0.289, rely=0.552, x=0, y=0)
    entry52 = ttk.Entry(MainWindow)
    entry52_value = tk.StringVar(value='13,728')
    entry52.configure(state="readonly", textvariable=entry52_value)
    _text_ = '13,728'
    entry52["state"] = "normal"
    entry52.delete("0", "end")
    entry52.insert("0", _text_)
    entry52["state"] = "readonly"
    entry52.place(anchor="nw", relwidth=0.07, relx=0.334, rely=0.511, x=0, y=0)
    entry53 = ttk.Entry(MainWindow)
    entry53_value = tk.StringVar(value='0,016')
    entry53.configure(state="readonly", textvariable=entry53_value)
    _text_ = '0,016'
    entry53["state"] = "normal"
    entry53.delete("0", "end")
    entry53.insert("0", _text_)
    entry53["state"] = "readonly"
    entry53.place(anchor="nw", relwidth=0.07, relx=0.334, rely=0.551, x=0, y=0)
    label55 = ttk.Label(MainWindow)
    label55.configure(background="#e5e5e5", text='const:')
    label55.place(anchor="nw", relx=0.412, rely=0.471, x=0, y=0)
    entry61 = ttk.Entry(MainWindow)
    entry61_value = tk.StringVar(value='-4418,322')
    entry61.configure(state="readonly", textvariable=entry61_value)
    _text_ = '-4418,322'
    entry61["state"] = "normal"
    entry61.delete("0", "end")
    entry61.insert("0", _text_)
    entry61["state"] = "readonly"
    entry61.place(anchor="nw", relwidth=0.07, relx=0.457, rely=0.47, x=0, y=0)
    label56 = ttk.Label(MainWindow)
    label56.configure(background="#e5e5e5", text='X12:')
    label56.place(anchor="nw", relx=0.412, rely=0.512, x=0, y=0)
    label57 = ttk.Label(MainWindow)
    label57.configure(background="#e5e5e5", text='X53:')
    label57.place(anchor="nw", relx=0.412, rely=0.552, x=0, y=0)
    entry62 = ttk.Entry(MainWindow)
    entry62_value = tk.StringVar(value='2,057')
    entry62.configure(state="readonly", textvariable=entry62_value)
    _text_ = '2,057'
    entry62["state"] = "normal"
    entry62.delete("0", "end")
    entry62.insert("0", _text_)
    entry62["state"] = "readonly"
    entry62.place(anchor="nw", relwidth=0.07, relx=0.457, rely=0.511, x=0, y=0)
    entry63 = ttk.Entry(MainWindow)
    entry63_value = tk.StringVar(value='43,318')
    entry63.configure(state="readonly", textvariable=entry63_value)
    _text_ = '43,318'
    entry63["state"] = "normal"
    entry63.delete("0", "end")
    entry63.insert("0", _text_)
    entry63["state"] = "readonly"
    entry63.place(anchor="nw", relwidth=0.07, relx=0.457, rely=0.551, x=0, y=0)
    button2 = ttk.Button(MainWindow, command=SetRandomPatient)
    button2.configure(text='Випадковий')
    button2.place(anchor="nw", relheight=0.07, relwidth=0.1105, relx=0.141, rely=0.30, x=0, y=0)
    label58 = ttk.Label(MainWindow)
    label58.configure(background="#e5e5e5", text='X28:')
    label58.place(anchor="nw", relx=0.04, rely=0.592, x=0, y=0)
    label59 = ttk.Label(MainWindow)
    label59.configure(background="#e5e5e5", text='U3:')
    label59.place(anchor="nw", relx=0.04, rely=0.632, x=0, y=0)
    label60 = ttk.Label(MainWindow)
    label60.configure(background="#e5e5e5", text='X8:')
    label60.place(anchor="nw", relx=0.04, rely=0.672, x=0, y=0)
    label61 = ttk.Label(MainWindow)
    label61.configure(background="#e5e5e5", text='X36:')
    label61.place(anchor="nw", relx=0.04, rely=0.712, x=0, y=0)
    label62 = ttk.Label(MainWindow)
    label62.configure(background="#e5e5e5", text='X2:')
    label62.place(anchor="nw", relx=0.04, rely=0.752, x=0, y=0)
    label63 = ttk.Label(MainWindow)
    label63.configure(background="#e5e5e5", text='X10:')
    label63.place(anchor="nw", relx=0.04, rely=0.792, x=0, y=0)
    label64 = ttk.Label(MainWindow)
    label64.configure(background="#e5e5e5", text='X9:')
    label64.place(anchor="nw", relx=0.04, rely=0.832, x=0, y=0)
    label65 = ttk.Label(MainWindow)
    label65.configure(background="#e5e5e5", text='U2:')
    label65.place(anchor="nw", relx=0.04, rely=0.872, x=0, y=0)
    entry36 = ttk.Entry(MainWindow)
    entry36_value = tk.StringVar(value='0,007')
    entry36.configure(state="readonly", textvariable=entry36_value)
    _text_ = '0,007'
    entry36["state"] = "normal"
    entry36.delete("0", "end")
    entry36.insert("0", _text_)
    entry36["state"] = "readonly"
    entry36.place(anchor="nw", relwidth=0.07, relx=0.085, rely=0.591, x=0, y=0)
    entry37 = ttk.Entry(MainWindow)
    entry37_value = tk.StringVar(value='-12,510')
    entry37.configure(state="readonly", textvariable=entry37_value)
    _text_ = '-12,510'
    entry37["state"] = "normal"
    entry37.delete("0", "end")
    entry37.insert("0", _text_)
    entry37["state"] = "readonly"
    entry37.place(anchor="nw", relwidth=0.07, relx=0.085, rely=0.631, x=0, y=0)
    entry38 = ttk.Entry(MainWindow)
    entry38_value = tk.StringVar(value='-0,367')
    entry38.configure(state="readonly", textvariable=entry38_value)
    _text_ = '-0,367'
    entry38["state"] = "normal"
    entry38.delete("0", "end")
    entry38.insert("0", _text_)
    entry38["state"] = "readonly"
    entry38.place(anchor="nw", relwidth=0.07, relx=0.085, rely=0.671, x=0, y=0)
    entry39 = ttk.Entry(MainWindow)
    entry39_value = tk.StringVar(value='-0,001')
    entry39.configure(state="readonly", textvariable=entry39_value)
    _text_ = '-0,001'
    entry39["state"] = "normal"
    entry39.delete("0", "end")
    entry39.insert("0", _text_)
    entry39["state"] = "readonly"
    entry39.place(anchor="nw", relwidth=0.07, relx=0.085, rely=0.711, x=0, y=0)
    entry40 = ttk.Entry(MainWindow)
    entry40_value = tk.StringVar(value='-293,851')
    entry40.configure(state="readonly", textvariable=entry40_value)
    _text_ = '-293,851'
    entry40["state"] = "normal"
    entry40.delete("0", "end")
    entry40.insert("0", _text_)
    entry40["state"] = "readonly"
    entry40.place(anchor="nw", relwidth=0.07, relx=0.085, rely=0.751, x=0, y=0)
    entry41 = ttk.Entry(MainWindow)
    entry41_value = tk.StringVar(value='-0,204')
    entry41.configure(state="readonly", textvariable=entry41_value)
    _text_ = '-0,204'
    entry41["state"] = "normal"
    entry41.delete("0", "end")
    entry41.insert("0", _text_)
    entry41["state"] = "readonly"
    entry41.place(anchor="nw", relwidth=0.07, relx=0.085, rely=0.791, x=0, y=0)
    entry42 = ttk.Entry(MainWindow)
    entry42_value = tk.StringVar(value='10,081')
    entry42.configure(state="readonly", textvariable=entry42_value)
    _text_ = '10,081'
    entry42["state"] = "normal"
    entry42.delete("0", "end")
    entry42.insert("0", _text_)
    entry42["state"] = "readonly"
    entry42.place(anchor="nw", relwidth=0.07, relx=0.085, rely=0.831, x=0, y=0)
    entry43 = ttk.Entry(MainWindow)
    entry43_value = tk.StringVar(value='0,520')
    entry43.configure(state="readonly", textvariable=entry43_value)
    _text_ = '0,520'
    entry43["state"] = "normal"
    entry43.delete("0", "end")
    entry43.insert("0", _text_)
    entry43["state"] = "readonly"
    entry43.place(anchor="nw", relwidth=0.07, relx=0.085, rely=0.871, x=0, y=0)
    label66 = ttk.Label(MainWindow)
    label66.configure(background="#e5e5e5", text='X19:')
    label66.place(anchor="nw", relx=0.165, rely=0.592, x=0, y=0)
    entry47 = ttk.Entry(MainWindow)
    entry47_value = tk.StringVar(value='0,117')
    entry47.configure(state="readonly", textvariable=entry47_value)
    _text_ = '0,117'
    entry47["state"] = "normal"
    entry47.delete("0", "end")
    entry47.insert("0", _text_)
    entry47["state"] = "readonly"
    entry47.place(anchor="nw", relwidth=0.07, relx=0.21, rely=0.591, x=0, y=0)
    label67 = ttk.Label(MainWindow)
    label67.configure(background="#e5e5e5", text='X52:')
    label67.place(anchor="nw", relx=0.165, rely=0.632, x=0, y=0)
    entry48 = ttk.Entry(MainWindow)
    entry48_value = tk.StringVar(value='0,701')
    entry48.configure(state="readonly", textvariable=entry48_value)
    _text_ = '0,701'
    entry48["state"] = "normal"
    entry48.delete("0", "end")
    entry48.insert("0", _text_)
    entry48["state"] = "readonly"
    entry48.place(anchor="nw", relwidth=0.07, relx=0.21, rely=0.631, x=0, y=0)
    label68 = ttk.Label(MainWindow)
    label68.configure(background="#e5e5e5", text='X17:')
    label68.place(anchor="nw", relx=0.165, rely=0.672, x=0, y=0)
    entry49 = ttk.Entry(MainWindow)
    entry49_value = tk.StringVar(value='0,017')
    entry49.configure(state="readonly", textvariable=entry49_value)
    _text_ = '0,017'
    entry49["state"] = "normal"
    entry49.delete("0", "end")
    entry49.insert("0", _text_)
    entry49["state"] = "readonly"
    entry49.place(anchor="nw", relwidth=0.07, relx=0.21, rely=0.671, x=0, y=0)
    label69 = ttk.Label(MainWindow)
    label69.configure(background="#e5e5e5", text='X15:')
    label69.place(anchor="nw", relx=0.165, rely=0.712, x=0, y=0)
    entry50 = ttk.Entry(MainWindow)
    entry50_value = tk.StringVar(value='-0,242')
    entry50.configure(state="readonly", textvariable=entry50_value)
    _text_ = '-0,242'
    entry50["state"] = "normal"
    entry50.delete("0", "end")
    entry50.insert("0", _text_)
    entry50["state"] = "readonly"
    entry50.place(anchor="nw", relwidth=0.07, relx=0.21, rely=0.711, x=0, y=0)
    label70 = ttk.Label(MainWindow)
    label70.configure(background="#e5e5e5", text='X31:')
    label70.place(anchor="nw", relx=0.289, rely=0.592, x=0, y=0)
    entry54 = ttk.Entry(MainWindow)
    entry54_value = tk.StringVar(value='0,001')
    entry54.configure(state="readonly", textvariable=entry54_value)
    _text_ = '0,001'
    entry54["state"] = "normal"
    entry54.delete("0", "end")
    entry54.insert("0", _text_)
    entry54["state"] = "readonly"
    entry54.place(anchor="nw", relwidth=0.07, relx=0.334, rely=0.591, x=0, y=0)
    label71 = ttk.Label(MainWindow)
    label71.configure(background="#e5e5e5", text='X12:')
    label71.place(anchor="nw", relx=0.289, rely=0.632, x=0, y=0)
    entry55 = ttk.Entry(MainWindow)
    entry55_value = tk.StringVar(value='-0,228')
    entry55.configure(state="readonly", textvariable=entry55_value)
    _text_ = '-0,228'
    entry55["state"] = "normal"
    entry55.delete("0", "end")
    entry55.insert("0", _text_)
    entry55["state"] = "readonly"
    entry55.place(anchor="nw", relwidth=0.07, relx=0.334, rely=0.631, x=0, y=0)
    label72 = ttk.Label(MainWindow)
    label72.configure(background="#e5e5e5", text='S1_in:')
    label72.place(anchor="nw", relx=0.289, rely=0.672, x=0, y=0)
    entry56 = ttk.Entry(MainWindow)
    entry56_value = tk.StringVar(value='-26,176')
    entry56.configure(state="readonly", textvariable=entry56_value)
    _text_ = '-26,176'
    entry56["state"] = "normal"
    entry56.delete("0", "end")
    entry56.insert("0", _text_)
    entry56["state"] = "readonly"
    entry56.place(anchor="nw", relwidth=0.07, relx=0.334, rely=0.671, x=0, y=0)
    label73 = ttk.Label(MainWindow)
    label73.configure(background="#e5e5e5", text='X86:')
    label73.place(anchor="nw", relx=0.289, rely=0.712, x=0, y=0)
    entry57 = ttk.Entry(MainWindow)
    entry57_value = tk.StringVar(value='12,974')
    entry57.configure(state="readonly", textvariable=entry57_value)
    _text_ = '12,974'
    entry57["state"] = "normal"
    entry57.delete("0", "end")
    entry57.insert("0", _text_)
    entry57["state"] = "readonly"
    entry57.place(anchor="nw", relwidth=0.07, relx=0.334, rely=0.711, x=0, y=0)
    label74 = ttk.Label(MainWindow)
    label74.configure(background="#e5e5e5", text='X24:')
    label74.place(anchor="nw", relx=0.289, rely=0.752, x=0, y=0)
    entry58 = ttk.Entry(MainWindow)
    entry58_value = tk.StringVar(value='-3,762')
    entry58.configure(state="readonly", textvariable=entry58_value)
    _text_ = '-3,762'
    entry58["state"] = "normal"
    entry58.delete("0", "end")
    entry58.insert("0", _text_)
    entry58["state"] = "readonly"
    entry58.place(anchor="nw", relwidth=0.07, relx=0.334, rely=0.751, x=0, y=0)
    label75 = ttk.Label(MainWindow)
    label75.configure(background="#e5e5e5", text='X6:')
    label75.place(anchor="nw", relx=0.289, rely=0.792, x=0, y=0)
    entry59 = ttk.Entry(MainWindow)
    entry59_value = tk.StringVar(value='-41,659')
    entry59.configure(state="readonly", textvariable=entry59_value)
    _text_ = '-41,659'
    entry59["state"] = "normal"
    entry59.delete("0", "end")
    entry59.insert("0", _text_)
    entry59["state"] = "readonly"
    entry59.place(anchor="nw", relwidth=0.07, relx=0.334, rely=0.791, x=0, y=0)
    label76 = ttk.Label(MainWindow)
    label76.configure(background="#e5e5e5", text='S3_in:')
    label76.place(anchor="nw", relx=0.289, rely=0.832, x=0, y=0)
    entry60 = ttk.Entry(MainWindow)
    entry60_value = tk.StringVar(value='-0,255')
    entry60.configure(state="readonly", textvariable=entry60_value)
    _text_ = '-0,255'
    entry60["state"] = "normal"
    entry60.delete("0", "end")
    entry60.insert("0", _text_)
    entry60["state"] = "readonly"
    entry60.place(anchor="nw", relwidth=0.07, relx=0.334, rely=0.831, x=0, y=0)
    label77 = ttk.Label(MainWindow)
    label77.configure(background="#e5e5e5", text='X1:')
    label77.place(anchor="nw", relx=0.412, rely=0.592, x=0, y=0)
    entry64 = ttk.Entry(MainWindow)
    entry64_value = tk.StringVar(value='-0,431')
    entry64.configure(state="readonly", textvariable=entry64_value)
    _text_ = '-0,431'
    entry64["state"] = "normal"
    entry64.delete("0", "end")
    entry64.insert("0", _text_)
    entry64["state"] = "readonly"
    entry64.place(anchor="nw", relwidth=0.07, relx=0.457, rely=0.591, x=0, y=0)
    label78 = ttk.Label(MainWindow)
    label78.configure(background="#e5e5e5", text='X18:')
    label78.place(anchor="nw", relx=0.412, rely=0.632, x=0, y=0)
    entry65 = ttk.Entry(MainWindow)
    entry65_value = tk.StringVar(value='-8,435')
    entry65.configure(state="readonly", textvariable=entry65_value)
    _text_ = '-8,435'
    entry65["state"] = "normal"
    entry65.delete("0", "end")
    entry65.insert("0", _text_)
    entry65["state"] = "readonly"
    entry65.place(anchor="nw", relwidth=0.07, relx=0.457, rely=0.631, x=0, y=0)
    label79 = ttk.Label(MainWindow)
    label79.configure(background="#e5e5e5", text='X44:')
    label79.place(anchor="nw", relx=0.412, rely=0.672, x=0, y=0)
    entry66 = ttk.Entry(MainWindow)
    entry66_value = tk.StringVar(value='15,807')
    entry66.configure(state="readonly", textvariable=entry66_value)
    _text_ = '15,807'
    entry66["state"] = "normal"
    entry66.delete("0", "end")
    entry66.insert("0", _text_)
    entry66["state"] = "readonly"
    entry66.place(anchor="nw", relwidth=0.07, relx=0.457, rely=0.671, x=0, y=0)
    label80 = ttk.Label(MainWindow)
    label80.configure(background="#e5e5e5", text='X4:')
    label80.place(anchor="nw", relx=0.412, rely=0.712, x=0, y=0)
    entry67 = ttk.Entry(MainWindow)
    entry67_value = tk.StringVar(value='-209,704')
    entry67.configure(state="readonly", textvariable=entry67_value)
    _text_ = '-209,704'
    entry67["state"] = "normal"
    entry67.delete("0", "end")
    entry67.insert("0", _text_)
    entry67["state"] = "readonly"
    entry67.place(anchor="nw", relwidth=0.07, relx=0.457, rely=0.711, x=0, y=0)
    label81 = ttk.Label(MainWindow)
    label81.configure(background="#e5e5e5", text='X38:')
    label81.place(anchor="nw", relx=0.412, rely=0.752, x=0, y=0)
    entry68 = ttk.Entry(MainWindow)
    entry68_value = tk.StringVar(value='-1,780')
    entry68.configure(state="readonly", textvariable=entry68_value)
    _text_ = '-1,780'
    entry68["state"] = "normal"
    entry68.delete("0", "end")
    entry68.insert("0", _text_)
    entry68["state"] = "readonly"
    entry68.place(anchor="nw", relwidth=0.07, relx=0.457, rely=0.751, x=0, y=0)
    label82 = ttk.Label(MainWindow)
    label82.configure(background="#e5e5e5", text='X3:')
    label82.place(anchor="nw", relx=0.412, rely=0.792, x=0, y=0)
    entry69 = ttk.Entry(MainWindow)
    entry69_value = tk.StringVar(value='0,006')
    entry69.configure(state="readonly", textvariable=entry69_value)
    _text_ = '0,006'
    entry69["state"] = "normal"
    entry69.delete("0", "end")
    entry69.insert("0", _text_)
    entry69["state"] = "readonly"
    entry69.place(anchor="nw", relwidth=0.07, relx=0.457, rely=0.791, x=0, y=0)
    label83 = ttk.Label(MainWindow)
    label83.configure(background="#e5e5e5", text='X51:')
    label83.place(anchor="nw", relx=0.412, rely=0.832, x=0, y=0)
    entry70 = ttk.Entry(MainWindow)
    entry70_value = tk.StringVar(value='-0,133')
    entry70.configure(state="readonly", textvariable=entry70_value)
    _text_ = '-0,133'
    entry70["state"] = "normal"
    entry70.delete("0", "end")
    entry70.insert("0", _text_)
    entry70["state"] = "readonly"
    entry70.place(anchor="nw", relwidth=0.07, relx=0.457, rely=0.831, x=0, y=0)
    button4 = ttk.Button(MainWindow, command=SecondWindow)
    button4.configure(text='Пояснення змінних')
    button4.place(anchor="nw", relheight=0.165, relwidth=0.23, relx=0.7378, rely=0.8135, x=0, y=0)

    MainWindow.mainloop()


def SecondWindow():
    MinorWindow = tk.Toplevel(MainWindow)

    image = Image.open('CreatedVariables.png')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(MinorWindow, image=photo)
    label.pack()

    MinorWindow.wait_window()


def ChooseRandomPatient():
    patients = [
        [104.00, 104.20, 358.00, 162.30],
        [103.90, 102.60, 354.00, 146.80],
        [102.50, 103.40, 354.00, 110.60],
        [101.60, 102.90, 344.00, 127.90],
        [102.30, 101.20, 310.00, 106.50],
        [100.40, 99.80, 283.00,	88.90],
        [100.70, 100.10, 314.00, 120.00],
        [100.30, 100.70, 275.00, 90.40],
        [101.50, 101.10, 259.00, 95.60]
    ]

    random_patient = random.choice(patients)

    return random_patient[0], random_patient[1], random_patient[3], random_patient[2]


def SetAveragePatient():
    entry1_value.set(101.27)
    entry2_value.set(101.51)
    entry3_value.set(100.45)
    entry4_value.set(292.20)
    #min
    entry5_value.set(98.8)
    entry6_value.set(99.8)
    entry7_value.set(69.3)
    entry8_value.set(55.99)
    entry9_value.set(1121.8)
    entry10_value.set(79.2)
    #max
    entry11_value.set(110.1)
    entry12_value.set(110.7)
    entry13_value.set(162.3)
    entry14_value.set(115.94)
    entry15_value.set(1936.6)
    entry16_value.set(111.8)


def SetRandomPatient():
    X1, X2, X3, X4 = ChooseRandomPatient()
    entry1_value.set(X1)
    entry2_value.set(X2)
    entry3_value.set(X3)
    entry4_value.set(X4)
    # min
    entry5_value.set(98.8)
    entry6_value.set(99.8)
    entry7_value.set(69.3)
    entry8_value.set(55.99)
    entry9_value.set(1121.8)
    entry10_value.set(79.2)
    # max
    entry11_value.set(110.1)
    entry12_value.set(110.7)
    entry13_value.set(162.3)
    entry14_value.set(115.94)
    entry15_value.set(1936.6)
    entry16_value.set(111.8)


def calculate():
    S1_in = entry1_value.get()
    S2_in = entry2_value.get()
    S3_in = entry3_value.get()
    Q_in = entry4_value.get()
    #min
    min_S1_in = entry5_value.get()
    min_S2_in = entry6_value.get()
    min_S3_in = entry7_value.get()
    min_U1 = entry8_value.get()
    min_U2 = entry9_value.get()
    min_U3 = entry10_value.get()
    #max
    max_S1_in = entry11_value.get()
    max_S2_in = entry12_value.get()
    max_S3_in = entry13_value.get()
    max_U1 = entry14_value.get()
    max_U2 = entry15_value.get()
    max_U3 = entry16_value.get()

    _Q_out_coeff1 = -0.204 * (S1_in / S3_in)
    _Q_out_coeff2 = 0.0004 * S1_in + 0.0004 * Q_in + 0.520 - 0.367 * (S1_in / S2_in)
    _Q_out_coeff3 = 0.007 * S2_in + 0.007 * Q_in + 10.081 * (S1_in / S2_in) - 12.510
    _Q_out_const = 352.605 + 0.872 * Q_in - 293.851 * (S1_in / S2_in) - 0.001 * (S3_in * Q_in)

    _S1_out_coeff1 = 0.117 * (S3_in / Q_in)
    _S1_out_coeff2 = -0.063 * ((S3_in ** 2) / (Q_in ** 2)) + 0.017 * (S2_in / Q_in)
    _S1_out_coeff3 = 0.701 * ((S3_in ** 2) / (Q_in ** 2)) - 0.242 * (S1_in / Q_in)
    _S1_out_const = 12.668 + 0.862 * S1_in

    _S2_out_coeff1 = 0.0
    _S2_out_coeff2 = 0.016 * ((S1_in ** 2) / (S3_in ** 2)) - 3.761 * (S1_in + Q_in)
    _S2_out_coeff3 = 0.001 * (S3_in + Q_in) - 0.228 * (S1_in / S3_in)
    _S2_out_const = 114.451 + 13.728 * S2_in - 26.176 * S1_in + 12.974 * ((S1_in / S2_in) * S1_in) \
                    - 41.659 * (S2_in / S3_in) - 0.255 * S3_in

    _S3_out_coeff1 = 15.807 * ((S1_in ** 2) / (Q_in ** 2)) - 1.780 * ((S1_in ** 2) / (S2_in ** 2))
    _S3_out_coeff2 = -0.133 * ((S3_in ** 2) / (Q_in ** 2))
    _S3_out_coeff3 = 2.057 * (S1_in / S3_in) - 8.435 * (S2_in / Q_in)
    _S3_out_const = -4418.322 + 45.318 * (S1_in + S2_in) - 0.431 * (S1_in * S2_in) \
                    - 209.704 * (S1_in / S3_in) + 0.006 * (S1_in * S3_in)

    U1 = LpVariable("U1", min_U1, max_U1)
    U2 = LpVariable("U2", min_U2, max_U2)
    U3 = LpVariable("U3", min_U3, max_U3)

    prob = LpProblem("Max", LpMaximize)
    prob += U1 >= min_U1
    prob += U1 <= max_U1
    prob += U2 >= min_U2
    prob += U2 <= max_U2
    prob += U3 >= min_U3
    prob += U3 <= max_U3

    # Q
    prob += _Q_out_const + _Q_out_coeff1 * U1 + _Q_out_coeff2 * U2 + _Q_out_coeff3 * U3
    # S1
    prob += _S1_out_const + _S1_out_coeff1 * U1 + _S1_out_coeff2 * U2 + _S1_out_coeff3 * U3 >= min_S1_in
    prob += _S1_out_const + _S1_out_coeff1 * U1 + _S1_out_coeff2 * U2 + _S1_out_coeff3 * U3 <= max_S1_in
    # S2
    prob += _S2_out_const + _S2_out_coeff1 * U1 + _S2_out_coeff2 * U2 + _S2_out_coeff3 * U3 >= min_S2_in
    prob += _S2_out_const + _S2_out_coeff1 * U1 + _S2_out_coeff2 * U2 + _S2_out_coeff3 * U3 <= max_S2_in
    # S3
    prob += _S3_out_const + _S3_out_coeff1 * U1 + _S3_out_coeff2 * U2 + _S3_out_coeff3 * U3 >= min_S3_in
    prob += _S3_out_const + _S3_out_coeff1 * U1 + _S3_out_coeff2 * U2 + _S3_out_coeff3 * U3 <= max_S3_in

    Status = prob.solve()
    U1 = U1.varValue
    U2 = U2.varValue
    U3 = U3.varValue

    _Q_out = _Q_out_coeff1 * U1 + _Q_out_coeff2 * U2 + _Q_out_coeff3 * U3 + _Q_out_const
    _S1_out = _S1_out_coeff1 * U1 + _S1_out_coeff2 * U2 + _S1_out_coeff3 * U3 + _S1_out_const
    _S2_out = _S2_out_coeff1 * U1 + _S2_out_coeff2 * U2 + _S2_out_coeff3 * U3 + _S2_out_const
    _S3_out = _S3_out_coeff1 * U1 + _S3_out_coeff2 * U2 + _S3_out_coeff3 * U3 + _S3_out_const

    entry71_value.set(round(U1, 3))
    entry72_value.set(round(U2, 3))
    entry73_value.set(round(U3, 3))
    entry74_value.set(round(_S1_out, 3))
    entry75_value.set(round(_S2_out, 3))
    entry76_value.set(round(_S3_out, 3))
    entry77_value.set(round(_Q_out, 3))

    entry17_value.set(round(_S1_out_coeff1, 4))
    entry21_value.set(round(_S1_out_coeff2, 4))
    entry25_value.set(round(_S1_out_coeff3, 4))
    entry29_value.set(round(_S1_out_const, 4))

    entry18_value.set("-")
    entry22_value.set(round(_S2_out_coeff2, 4))
    entry26_value.set(round(_S2_out_coeff3, 4))
    entry30_value.set(round(_S2_out_const, 4))

    entry19_value.set(round(_S3_out_coeff1, 4))
    entry23_value.set(round(_S3_out_coeff2, 4))
    entry27_value.set(round(_S3_out_coeff3, 4))
    entry31_value.set(round(_S3_out_const, 4))

    entry20_value.set(round(_Q_out_coeff1, 4))
    entry24_value.set(round(_Q_out_coeff2, 4))
    entry28_value.set(round(_Q_out_coeff3, 4))
    entry32_value.set(round(_Q_out_const, 4))


if __name__ == "__main__":
    WindowCreation()