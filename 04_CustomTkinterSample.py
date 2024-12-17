"""
CustomTkinterサンプルコード
https://customtkinter.tomschimansky.com/
簡単なGUI画面を作成
"""
import customtkinter

def button_callback():
    print("button pressed")

if __name__ == '__main__':
    app = customtkinter.CTk()
    app.title("my app")
    app.geometry("400x150")
    app.grid_columnconfigure((0), weight=1)
    button = customtkinter.CTkButton(app, text="my button", command=button_callback)
    button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
    checkbox_1 = customtkinter.CTkCheckBox(app, text="チェックボックス 1")
    checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
    checkbox_2 = customtkinter.CTkCheckBox(app, text="チェックボックス 2")
    checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

    app.mainloop()