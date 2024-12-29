from tkinter import *
from PIL import Image, ImageTk
import time

class IMS:
    def __init__(self, root):
        
        self.root = root
        self.root.geometry("1350x700")
        self.root.title("Inventory Management System Develop By Noura")
        self.root.config(bg='black')

        # Background image
        icon_image = Image.open("image.png")
        icon_image = icon_image.resize((50, 50), Image.Resampling.LANCZOS)
        self.icon_title = ImageTk.PhotoImage(icon_image)

        # Title Label
        title = Label(self.root, text="Inventory Management System", image=self.icon_title,
                      compound=LEFT, bg="black", fg="RED", font=("Times New Roman", 40, "bold"),
                      anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=80)

        # Logout Button
        btn_logout = Button(self.root, text="Logout", font=("Times New Roman", 15, 'bold'),
                            bg="yellow", cursor="hand2").place(x=1100, y=10, height=50, width=150)

        # Clock Label
        self.lbl_clock = Label(self.root, text="Welcome to our Website\t\t Date: DD-MM-YYYY\t\t Time:HH:MM:SS",
                               font=("Times New Roman", 15, "bold"), bg='black', fg='yellow', anchor='center', padx=20)
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.time_and_date()  # Call to update the clock

        # Left Menu
        self.MenuLogo = Image.open("image copy.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.Resampling.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        lbl_menu = Label(LeftMenu, text="Menu", font=("Times New Roman", 20, 'bold'), fg="yellow", bg="black",
                         cursor="hand2").pack(side=TOP, fill=X)

        btn_employee = Button(LeftMenu, text="Employees", font=("Times New Roman", 20, 'bold'), fg="yellow", bg='black',
                              bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier = Button(LeftMenu, text="Supplier", font=("Times New Roman", 20, 'bold'), fg="yellow", bg='black',
                              bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_category = Button(LeftMenu, text="Item", font=("Times New Roman", 20, 'bold'), fg="yellow", bg='black',
                              bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_sales = Button(LeftMenu, text="Product", font=("Times New Roman", 20, 'bold'), fg="yellow", bg='black',
                           bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_Exit = Button(LeftMenu, text="Exit", font=("Times New Roman", 20, 'bold'), fg="yellow", bg='black',
                          bd=3, cursor="hand2").pack(side=TOP, fill=X)

        # Category Information
        self.lbl_employee = Label(self.root, text="Total Employee\n[0]", bd=4, bg='yellow', fg='black',
                                  font=("Times New Roman", 20, 'bold'))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_supplier = Label(self.root, text="Total Employee\n[4]", bd=4, bg='yellow', fg='black',
                                  font=("Times New Roman", 20, 'bold'))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Total Employee\n[5]", bd=4, bg='yellow', fg='black',
                                  font=("Times New Roman", 20, 'bold'))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total Employee\n[34]", bd=4, bg='yellow', fg='black',
                                 font=("Times New Roman", 20, 'bold'))
        self.lbl_product.place(x=300, y=300, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total Employee\n[0]", bd=4, bg='yellow', fg='black',
                               font=("Times New Roman", 20, 'bold'))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)

        # Footer
        lbl_footer = Label(self.root, text="IMS-Inventory Management System | Development By Noura")
        lbl_footer.place(x=0, y=650, relwidth=1, height=30)

    def time_and_date(self):
        string = time.strftime("Date: %d-%m-%Y \t Time: %H:%M:%S")
        self.lbl_clock.config(text=string)
        self.lbl_clock.after(1000, self.time_and_date)  # Update every second

# Create window and application instance
root = Tk()
obj = IMS(root)
root.mainloop()
