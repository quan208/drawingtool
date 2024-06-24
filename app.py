import customtkinter as ctk


class DrawingTool(ctk.CTk):
    ver = "1.0.0"

    def __init__(self):
        super().__init__()
        self.title("Drawing Tool 1.0")
        self.geometry("960x640")
        f1 = ctk.CTkFont(family="JetBrains Mono", size=13)
        text1 = ctk.CTkLabel(
            self, font=f1, text=f"CurrentVer: {self.ver}", text_color="white"
        )
        text1.pack(anchor="sw", padx=10)


if __name__ == "__main__":
    app = DrawingTool()
    app.mainloop()
