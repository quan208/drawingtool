import customtkinter as ctk

class DrawingTool(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Drawing Tool 1.0")
        self.geometry("960x640")
        self._set_appearance_mode("light")     
    

if __name__ == "__main__":
    app = DrawingTool()
    app.mainloop()