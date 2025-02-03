import tkinter as tk
import speedtest_cli as speedtest


def speedcheck():
    st = speedtest.Speedtest()  
    st.get_servers()  
    down = str(round(st.download() / (10**6), 3)) + " Mbps"  
    up = str(round(st.upload() / (10**6), 3)) + " Mbps"  
    
    lab_down.config(text=down)  
    lab_up.config(text=up) 
    


sp = tk.Tk()
sp.title("Internet Speed Test")
sp.geometry("500x600")
sp.config(bg='pink')


lab_title = tk.Label(sp, text="Internet Speed Test", font=("Times New Roman", 30, "bold"), bg="pink", fg="black")
lab_title.place(x=90, y=40, height=50, width=380)



lab_download = tk.Label(sp, text="Download Speed", font=("Times New Roman", 30, "bold"))
lab_download.place(x=90, y=130, height=50, width=380)


lab_down = tk.Label(sp, text="00", font=("Times New Roman", 30, "bold"))
lab_down.place(x=90, y=200, height=50, width=380)


lab_upload = tk.Label(sp, text="Upload Speed", font=("Times New Roman", 30, "bold"))
lab_upload.place(x=90, y=290, height=50, width=380)



lab_up = tk.Label(sp, text="00", font=("Times New Roman", 30, "bold"))
lab_up.place(x=90, y=360, height=50, width=380)

button = tk.Button(sp, text="Check Speed", font=("Times New Roman", 30, "bold"), relief="raised", bg="red", command=speedcheck)
button.place(x=90, y=460, height=50, width=380)

sp.mainloop()

