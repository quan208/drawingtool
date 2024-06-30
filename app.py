import customtkinter as ctk
from PIL import Image, ImageTk
import os
import buttondata as bdt

# Directory icon:
icon_dir = os.path.join("icon")
light_ico = os.path.join(icon_dir, "sun.ico")
dark_ico = os.path.join(icon_dir, "black.ico")
# logo_path = os.path.join(icon_dir, "icon.ico")


class DrawingTool(ctk.CTk):
    ver = "1.0.0"

    def __init__(self):
        super().__init__()
        self.title("Drawing Tool 1.0")
        self.geometry("960x640")
        # self.iconpath = ImageTk.PhotoImage(file=logo_path)
        self.font1 = ctk.CTkFont(family="JetBrains Mono", size=13, weight="bold")
        self.text1 = ctk.CTkLabel(
            self, font=self.font1, text=f"CurrentVer: {self.ver}", text_color="white"
        )
        self.text1.pack(anchor="sw", side="left", pady=2)
        self.zoom = ctk.CTkSlider(self, from_=50, to=175, command=self.updateZoom)
        self.zoom.pack(anchor="sw", side="right", padx=5, pady=5)
        self.textzoom = ctk.CTkLabel(
            self,
            font=self.font1,
            text=f"Zoom: 100%",
            text_color="white",
        )
        self.textzoom.pack(anchor="sw", side="right")
        self.bgbutton = ctk.CTkButton(
            self,
            text="Theme",
            font=self.font1,
            text_color="black",
            corner_radius=8,
            width=32,
            height=32,
            fg_color="pink",
            hover_color="white",
            border_width=5,
            border_color="white",
            image=ctk.CTkImage(dark_image=Image.open(light_ico)),
            command=self.changebg,
        )
        self.bgbutton.pack(anchor="sw", padx=10, side="left", pady=2)
        self.createButton()
        self.drawcanvas(self.font1)
        self.saveUI()

    def changebg(self):
        curcolor = ctk.get_appearance_mode()
        newcolor = "Light" if curcolor == "Dark" else "Dark"
        newtcolor = "white" if self.text1._text_color == "black" else "black"
        newicon = (
            ctk.CTkImage(light_image=Image.open(light_ico))
            if newcolor == "Dark"
            else ctk.CTkImage(dark_image=Image.open(dark_ico))
        )
        newhovercolor = "#D3D3D3" if newtcolor == "black" else "#D1E4E4"
        self.bgbutton.configure(
            image=newicon,
            hover_color=newhovercolor,
            border_color=newtcolor,
        )
        self.text1.configure(text_color=newtcolor)
        self.textzoom.configure(text_color=newtcolor)
        ctk.set_appearance_mode(newcolor)

    def drawcanvas(self, font1):
        self.canvaswidth = 800
        self.canvasheight = 500
        self.sizecout = ctk.CTkLabel(
            self,
            text=str(self.canvaswidth) + " x " + str(self.canvasheight) + "px",
            font=font1,
        )
        self.sizecout.pack(anchor="sw", side=ctk.BOTTOM, padx=50)
        self.canvas = ctk.CTkCanvas(
            self,
            width=self.canvaswidth,
            height=self.canvasheight,
            bg="white",
            borderwidth=5,
        )
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

    def updateZoom(self, value):
        zoom_factor = int(value) / 100
        new_width = int(self.canvaswidth * zoom_factor)
        new_height = int(self.canvasheight * zoom_factor)
        self.canvas.configure(width=new_width, height=new_height)
        self.sizecout.configure(text=f"{new_width} x {new_height}px")
        self.textzoom.configure(text=f"Zoom: {int(value)}%")

    # Create buttons :
    def createButton(self):
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.place(anchor="n", relx=0.5, rely=0.01)
        button_width = 32
        button_height = 32
        for idx, (text, command) in enumerate(bdt.button_data):
            button = ctk.CTkButton(
                button_frame,
                text=text,
                command=command,
                width=button_width,
                height=button_height,
                corner_radius=8,
                hover_color="#A438BA",
                fg_color="white",
                bg_color="transparent",
            )
            button.pack(side=ctk.LEFT, padx=2, pady=15)

    def saveUI(self):
        FileUi = ctk.CTkOptionMenu(self, corner_radius=8)
        FileUi.place(anchor="nw", relx=0, rely=0)


if __name__ == "__main__":
    app = DrawingTool()
    app.mainloop()
