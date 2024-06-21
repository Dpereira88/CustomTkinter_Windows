from tkinter import *
import customtkinter

from PIL import Image, ImageTk, ImageOps
from pylibdmtx.pylibdmtx import encode
import socket
from rich import print as rprint
"""
class DataMatrixApp(customtkinter.CTk()):
    def __init__(self):
        super().__init__()

        self.title("Data Matrix Generator")
        self.geometry("600x500")

        self.label = tk.Label(self, text="Enter text to generate Data Matrix:")
        self.label.pack(pady=20)

        # Validate function to allow only numbers
        vcmd = self.register(self.validate_numbers)

        self.text_entry = tk.Entry(self, validate="key", validatecommand=(vcmd, "%P"))
        self.text_entry1 = tk.Entry(self)
        self.text_entry.pack(pady=10)
        self.text_entry1.pack(pady=10)

        #self.print_button = tk.Button(self, text="Print Data Matrix", command=self.print_data_matrix)
        #self.print_button.pack(pady=10)

        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.pack(pady=20)

        self.dm_image = None

        # Bind the KeyRelease event to the text entry
        #self.text_entry.bind("<KeyRelease>", self.generate_data_matrix)
        # Bind the Return key to the print button
        #self.print_button.bind('<Return>', lambda event: self.print_button.invoke())

    def validate_numbers(self, new_text):
        # Allow only digits and empty string
        return new_text.isdigit() or new_text == ""



    def generate_data_matrix(self, event=None):
        text = self.text_entry.get()
        text_length = len(text)

        if text:
            if text_length == 32:
                size = ('18x18')
            elif text_length == 34:
                size = ('20x20')
            else:
                messagebox.showwarning("Input Error", "Text length must be 32 or 34 characters.")
                return

            encoded = encode(text.encode('utf-8'), size=size)

            img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)

            # Invert colors
            img = ImageOps.invert(img.convert('L')).convert('RGB')

            img = img.resize((150, 150), Image.LANCZOS)  # Resize for better display in Tkinter

            self.dm_image = ImageTk.PhotoImage(img)
            self.canvas.create_image(150, 150, image=self.dm_image)
        else:
            messagebox.showwarning("Input Error", "Please enter some text to generate Data Matrix")


    def print_data_matrix(self):
        text = self.text_entry.get()

        # Define the Datamax O'Neil printer IP and port
        printer_ip = '10.121.112.40'
        printer_port = 9100

        # Data Matrix printing command example with placeholder @Text1@
        dpl_command = "\nm" \
                      "\nKcLW1057" \
                      "\nKcFE0" \
                      "\nV0" \
                      "\nL" \
                      "\nJL" \
                      "\nPC" \
                      "\nPC" \
                      "\nA2" \
                      "\nz" \
                      "\nH22" \
                     f"\n3W1C330000056056600422000018018{text}" \
                      "\nA1" \
                      "\n1X1100100000507P0010001007005070070057700000577" \
                      "\nA2" \
                      "\nQ0001" \
                      "\nE"
        
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                rprint(s.connect((printer_ip, printer_port)))
                rprint(s.send(dpl_command.encode()))
            #messagebox.showinfo("Print", "Data Matrix printed successfully.")
        except Exception as e:
            messagebox.showerror("Print Error", f"Failed to print Data Matrix:\n{e}")

    def generate_data_matrix(self):
        text = self.text_entry.get()
        text_length = len(text)

        if text:
            if text_length == 32:
                size = ('18x18')
            elif text_length == 34:
                size = ('20x20')
            else:
                messagebox.showwarning("Input Error", "Text length must be 32 or 34 characters.")
                return

            encoded = encode(text.encode('utf-8'), size=size)

            img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)

            # Invert colors
            img = ImageOps.invert(img.convert('L')).convert('RGB')

            img = img.resize((150, 150), Image.LANCZOS)  # Resize for better display in Tkinter

            self.dm_image = ImageTk.PhotoImage(img)
            self.canvas.create_image(150, 150, image=self.dm_image)
        else:
            messagebox.showwarning("Input Error", "Please enter some text to generate Data Matrix")

if __name__ == "__main__":
    app = DataMatrixApp()
    app.mainloop()
"""





class App(customtkinter.CTk):
    #validate the value is not insert only with alpha numeric values
    def validate_numbers(self, new_text):
        # Allow only digits and empty string
        if new_text.isalnum() or new_text == "":
            return True
        else:
            return False
    #put the text always on Upper Case
    def on_text_change(self, *args):
        current_text = self.entry_var.get()
        if current_text.isalnum():
            # Convert the text to uppercase
            self.entry_var.set(current_text.upper())
        
    def change_color_frame(self, widget):
        text = self.text_entry.get()
        text_length = len(text)

        if text:
            if text_length == 32:
                pass
            elif text_length == 34:
                pass
            elif text_length == 1:
                self.frame1.configure(fg_color=("green"))
                pass
            else:
                self.frame1.configure(fg_color=('gray90', 'gray13'))
                #print(self.frame1.cget('fg_color'))
                return
        

    def tab1_content(self):
        #set frame to 
        self.frame1 = customtkinter.CTkFrame(self.tabview.tab(self.text_tab_view1))
        self.frame1.grid()

        # StringVar to hold the text of the entry widget
        self.entry_var = customtkinter.StringVar()
        # Trace the StringVar for changes
        self.entry_var.trace_add("write", self.on_text_change)

        # Validate function to allow only numbers
        vcmd = self.register(self.validate_numbers)
        self.text_entry = customtkinter.CTkEntry(self.frame1, textvariable = self.entry_var, font= self.my_font, validate="key", validatecommand=(vcmd, "%P"))
        self.text_entry.grid(row=0, column=0, padx=5, pady=5)
        
        self.label1 = customtkinter.CTkLabel(self.frame1, text = "", font= self.my_font)
        self.label1.grid(row=0, column=1, padx=5, pady=5)

        
        # Bind the KeyRelease event to the text entry
        self.text_entry.bind("<KeyRelease>", self.change_color_frame)



    def __init__(self):
        super().__init__()
        #* Colors and Font
        self.my_font = customtkinter.CTkFont(family="", size=12)
        self.text_tab_view1 = "My tab_view1"

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("dark-blue")# 'blue', 'dark-blue', 'green'
        self.geometry("600x350")
        self.title('My - Window')


        #*TabView
        self.tabview = customtkinter.CTkTabview(master = self, width=580, height=340, anchor="w")
        self.tabview._segmented_button.configure(font= self.my_font)
        self.tabview.grid(row=0, column=0, padx=5, pady=5) # position 

        #* create tabs
        self.tabview1 = self.tabview.add(self.text_tab_view1)
        self.tab1_content()

        self.tabview.add("Copy tab_view2")
        self.tabview.add("Copy tab_view3")










        #self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callbck)
        #self.button.pack(padx=20, pady=20)

     #def button_callbck(self):
     #   print("button clicked")
    


#loop app
app = App()
app.mainloop()



