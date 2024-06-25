import customtkinter as ctk
from PIL import Image
import os
import buttondata as bdt

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
        self.text1.pack(anchor="sw", side="left")
        self.bgbutton = ctk.CTkButton(
            self,
            text=None,
            corner_radius=32,
            width=32,
            height=32,
            fg_color="pink",
            hover_color="white",
            image=ctk.CTkImage(dark_image=Image.open(dark_ico)),
            command=self.changebg,
        )
        self.bgbutton.pack(anchor="sw", padx=10, side="left")
        # self.createButton()
        self.drawcanvas()

    def changebg(self):
        curcolor = ctk.get_appearance_mode()
        newcolor = "Light" if curcolor == "Dark" else "Dark"
        newtcolor = "white" if self.text1._text_color == "black" else "black"
        newicon = (
            ctk.CTkImage(light_image=Image.open(light_ico))
            if newcolor == "Light"
            else ctk.CTkImage(dark_image=Image.open(dark_ico))
        )
        newhovercolor = "#D3D3D3" if newtcolor == "black" else "#D1E4E4"
        self.bgbutton.configure(image=newicon)
        self.bgbutton.configure(hover_color=newhovercolor)
        self.text1.configure(text_color=newtcolor)
        ctk.set_appearance_mode(newcolor)

    def drawcanvas(self):
        self.canvas = ctk.CTkCanvas(self, width=800, height=500, bg="white")
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

    # Create buttons :

    # def createButton(self):
    #     button_frame = ctk.CTkFrame(self)
    #     button_frame.place(anchor="n", relx=0.5, rely=0.01)
    #     button_width = 35
    #     button_height = 45
    #     for idx, (text, command) in enumerate(bdt.button_data):
    #         text.resize
    #         button = ctk.CTkButton(
    #             button_frame,
    #             text=text,
    #             command=command,
    #             width=button_width,
    #             height=button_height,
    #             corner_radius=15,
    #             hover_color="#A438BA",
    #             fg_color="white",
    #         )
    #         button.pack()


if __name__ == "__main__":
    app = DrawingTool()
    app.mainloop()
