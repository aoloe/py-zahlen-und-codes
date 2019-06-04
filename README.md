# py-zahlen-und-codes

Kleine Python / Tk Applikation um Werte aus zwei Dateien zusammen zu fügen

## Assets

The icon is from

<http://www.iconarchive.com/show/blue-bits-icons-by-icojam/database-icon.html>

but the downloaded files did not work with pyinstaller.

I've uploaded the png to <https://icoconvert.com/> and the resulting file did work.

## Crate the EXE


```
pip install pyinstaller
pyinstaller --onefile --windowed --name zahlen-und-code main.py
```

The exe will be in the `dist` directory

```
--icon FILE.ico
```

This does not work correctly: <https://github.com/pyinstaller/pyinstaller/issues/3944>
