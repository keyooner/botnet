import datetime
import customtkinter as ctk

def test_return_variable():
        return 'return variable'

def input_message_in_textbox(textbox, entry):
        date_time = datetime.datetime.now()
        textbox.configure(state="normal")
        textbox.insert("0.0", f"[{date_time}] $: {entry.get()}" + f" {test_return_variable()}" "\n\n")
        entry.delete(0, ctk.END)
        textbox.configure(state="disabled")