import datetime as date 
import yfinance as yf
import matplotlib.pyplot as plt
from  tkinter import ttk
import tkinter as tk
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
main_window=tk.Tk()
main_window.geometry("700x500")
main_window.title("Welcome")
Stock_name={
     "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Tesla": "TSLA",
    "Amazon": "AMZN",
    "Google": "GOOGL"
}
time_frame={
        "1 minute":"1m",
        "5 minutes":"5m",
        "15 minutes":"15m",
        "1 hour":"1h",
        "4 hour":"4h",
        "1 day":"1d"
}
combo_box_name=ttk.Combobox(
    # main_window,
    state="readonly",
    values=list(Stock_name.keys())
)

combo_box_name.set("Select the company name ")
combo_box_name.place(x=50,y=50)
write=tk.Label(main_window,font=("Arial", 20, "bold"))
write.pack()
def getting_output_Cname(event=None):
    selection=combo_box_name.get()
    global company_name
    company_name=selection 
    write.config(text=Stock_name[company_name])

combo_box_name.bind("<<ComboboxSelected>>",getting_output_Cname)

combo_box_interval=ttk.Combobox(
    main_window,
    state="readonly",
    values=list(time_frame.keys())
)
combo_box_interval.place(x=50,y=100)
combo_box_interval.set("Slect time ")
interval_name=""
def getting_output_Iname(event=None):
    selection=combo_box_interval.get()
    write.config(text=selection)
    global interval_name
    interval_name=time_frame[selection]
    

combo_box_interval.bind("<<ComboboxSelected>>",getting_output_Iname)

day=date.date.today()-date.timedelta(days=1)
def data():
    data=yf.download(Stock_name[company_name],end=day,interval=interval_name)

    data["EMA50"]=data["Close"].rolling(50).mean()
    data.to_csv("Data/"+Stock_name[company_name]+f"from {day} with {interval_name}.csv")
    chart=plt.figure(figsize=(12,6))

    plt.plot(data.index, data["Close"], label="Close Price", alpha=0.7)

    plt.plot(data.index, data["EMA50"], label="50-min EMA", color="red",alpha=0.2, linewidth=5)

    current_price=data["Close"].iloc[-1][-1]
    ema=data["EMA50"].iloc[-1]


# chart.figtext(0.15,0.5,"Trend is bullist "if current_price >ema else " Trend is bullist " if current_price >decision_ema  else " Overll trend is breaish")
   
    canvas = FigureCanvasTkAgg(chart, master=main_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
btn = tk.Button(main_window, text="Click Me",command=data)
btn.place(x=50, y=200)   
main_window.mainloop()


