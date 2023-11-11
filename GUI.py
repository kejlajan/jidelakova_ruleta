def OpenFileOpenDialog():
    file_path = filedialog.askopenfilename(initialdir="./", title="Select a file")
    if file_path:
        inspect_file_BTN.config(state=tk.NORMAL)
        global selected_file_STR
        selected_file_STR = file_path
        UpdateSelectedFilepath()

def InspectFile():
    if 'selected_file_STR' in globals():
        with open(selected_file_STR, 'r') as file:
            file_contents = file.read()
            display_window = tk.Toplevel(root_WIN)
            display_window.title("File Contents")
            text_widget = tk.Text(display_window)
            text_widget.insert(tk.END, file_contents)
            text_widget.pack()

def UpdateSelectedFilepath():
    path_to_file_LBL.config(text = f"selcted file is: {selected_file_STR}")

def LaunchKucharka():
    root_WIN.destroy()
