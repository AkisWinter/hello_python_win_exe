import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Hello World App")
    root.geometry("280x150")
    
    root.iconbitmap("icons/icon.ico")

    label = tk.Label(root, text="Hallo World!", font=("Arial", 24))
    label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    ok_button = tk.Button(button_frame, text="OK", command=root.destroy)
    ok_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 5))

    tk.Frame(button_frame, width=10).pack(side=tk.LEFT)

    close_button = tk.Button(button_frame, text="Close", command=root.destroy)
    close_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 10))

    root.mainloop()

if __name__ == '__main__':
    main()