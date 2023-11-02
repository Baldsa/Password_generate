import customtkinter as cT
import tkinter
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from PIL import Image
import password



class App(cT.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.title("Password Generator")
        self.resizable(False, False)

        self.logo = cT.CTkImage(light_image=Image.open("1.png"), size=(300, 200))
        self.logo_label = cT.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)

        self.password_frame = cT.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row = 1, column = 0, padx = (20,20), sticky = "nsew")


        self.entry_password = cT.CTkEntry(master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=0, padx=(20,20))


        self.button = cT.CTkButton(master=self.password_frame, text="Generate", width=100, 
                                   command=self.set_password)
        
        self.button.grid(row=0, column=1)
        
        self.settings_frame = cT.CTkFrame(master=self)
        self.settings_frame.grid(row = 2, column = 0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.password_lenght_slider = cT.CTkSlider(master=self.settings_frame, from_=0, to=100,
                                                   number_of_steps=100,command=self.slider_event)

        self.password_lenght_slider.grid(row=1, column = 0, columnspan=3, pady=(20, 20), sticky="ew")
        self.password_lenght_entry = cT.CTkEntry(master=self.settings_frame, width=50)
        self.password_lenght_entry.grid(row=1, column=3, padx=(20,10), sticky="we")
        
        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = cT.CTkCheckBox(master=self.settings_frame, text="0-9", variable=self.cb_digits_var
                                        , onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10)

        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = cT.CTkCheckBox(master=self.settings_frame, text="a-z", variable=self.cb_lower_var
                                       , onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = cT.CTkCheckBox(master=self.settings_frame, text="A-Z", variable=self.cb_upper_var
                                       , onvalue=ascii_uppercase, offvalue="")
        
        self.cb_upper.grid(row=2, column=2)


        self.cb_symbol_var = tkinter.StringVar()
        self.cb_symbol = cT.CTkCheckBox(master=self.settings_frame, text="@#$%", variable=self.cb_symbol_var
                                       , onvalue=punctuation, offvalue="")
        
        self.cb_symbol.grid(row=2, column=3)




    def slider_event(self, value):
        self.password_lenght_entry.delete(0, "end")
        self.password_lenght_entry.insert(0, int(value))
    def get_character(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get() + self.cb_upper_var.get()
                       + self.cb_symbol_var.get())
        return chars
    def set_password(self):
        self.entry_password.delete(0, "end")
        self.entry_password.insert(0, password.create_new(lenght=int(self.password_lenght_slider.get()), 
                                                          characters=self.get_character()))
        

if __name__ == "__main__":
    app = App()
    app.mainloop()

