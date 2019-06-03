import zahlen_code
import os
from tkinter import Tk, Button, Label, filedialog

print()

def codes_clicked(ignore = None):
    # print(os.environ)
    if 'PWD' in os.environ:
        initialdir = os.environ['PWD']
    elif 'HOME' in os.environ:
        initialdir = os.environ['HOME']
    filename = filedialog.askopenfilename(
        initialdir = os.path.expanduser(initialdir),
        title = 'Codes-Datei auswählen',
        filetypes = [('text-Dateien', '*.txt')],
        parent = window)
    if filename:
        codes_label.configure(text = filename)
        names_btn.configure(state = 'normal')
        window.bind('<space>', names_clicked)

def names_clicked(ignore = None):
    filename = filedialog.askopenfilename(
        title = 'Namen-Datei auswählen',
        filetypes = [('text-Dateien', '*.txt')],
        parent = window)
    if filename:
        names_label.configure(text = filename)
        output_btn.configure(state = 'normal')
        window.bind('<space>', output_clicked)

def output_clicked(ignore = None):
    filename = filedialog.asksaveasfilename(
        title = 'Output-Datei auswählen',
        filetypes = [('text-Dateien', '*.txt')],
        parent = window)
    if filename:
        output_label.configure(text = filename)
        process_btn.configure(state = 'normal')
        window.bind('<space>', process_clicked)

def process_clicked(ignore = None):
    zahlen_code.process_names_and_codes(
        codes_label.cget('text'),
        names_label.cget('text'),
        output_label.cget('text')
    )
        
    process_label.configure(text = '✓')
    codes_btn.configure(state = 'disabled')
    names_btn.configure(state = 'disabled')
    output_btn.configure(state = 'disabled')
    process_btn.configure(state = 'disabled')

def quit(ignore = None):
    window.destroy()

window = Tk()
 
window.title('Zahlen und Codes')
window.geometry('640x480')
window.attributes('-type', 'dialog')

# todo: does not work
window.bind('<Control-q>', quit)
window.bind('<Escape>', quit)
window.bind('<space>', codes_clicked)

codes_btn  =  Button(window, text = 'Codes-Datei',
    command = codes_clicked)
codes_btn.grid(column = 0, row = 0)
codes_label  =  Label(window, text = '...')
codes_label.grid(column = 1, row = 0, sticky = 'W')
 
names_btn  =  Button(window, text = 'Namen-Datei',
    state = 'disabled', command = names_clicked)
names_btn.grid(column = 0, row = 1)
names_label  =  Label(window, text = '...')
names_label.grid(column = 1, row = 1, sticky = 'W')

output_btn  =  Button(window, text = 'Output-Datei',
    state = 'disabled', command = output_clicked)
output_btn.grid(column = 0, row = 2)
output_label  =  Label(window, text = '...')
output_label.grid(column = 1, row = 2, sticky = 'W')

process_btn  =  Button(window, text = 'Los!',
    state = 'disabled', command = process_clicked)
process_btn.grid(column = 0, row = 3, sticky = 'W')
process_label  =  Label(window, text = '...')
process_label.grid(column = 1, row = 3, sticky = 'W')

window.mainloop()


