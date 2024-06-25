import customtkinter as ctk
from PIL import Image
import os

# Directory icon:
icon_dir = os.path.join("icon")
light_ico = os.path.join(icon_dir, "sun.ico")
dark_ico = os.path.join(icon_dir, "black.ico")


class DrawingTool(ctk.CTk):
    ver = "1.0.0"

    def __init__(self):
        super().__init__()
        self.title("Drawing Tool 1.0")
        self.geometry("960x640")
        self.font1 = ctk.CTkFont(family="JetBrains Mono", size=13, weight="bold")
        self.text1 = ctk.CTkLabel(
            self, font=self.font1, text=f"CurrentVer: {self.ver}", text_color="white"
        )
        self.text1.pack(anchor="sw", padx=10)
        self.bgbutton = ctk.CTkButton(
            self,
            text=None,
            corner_radius=32,
            width=32,
            height=32,
            fg_color="pink",
            image=ctk.CTkImage(dark_image=Image.open(dark_ico)),
            command=self.changebg,
        )
        self.bgbutton.pack(anchor="sw", padx=20)

    def changebg(self):
        curcolor = ctk.get_appearance_mode()
        newcolor = "Light" if curcolor == "Dark" else "Dark"
        newtcolor = "white" if self.text1._text_color == "black" else "black"
        newicon = (
            ctk.CTkImage(light_image=Image.open(light_ico))
            if newcolor == "Light"
            else ctk.CTkImage(dark_image=Image.open(dark_ico))
        )
        self.bgbutton.configure(image=newicon)
        self.text1.configure(text_color=newtcolor)
        ctk.set_appearance_mode(newcolor)


if __name__ == "__main__":
    app = DrawingTool()
    app.mainloop()
