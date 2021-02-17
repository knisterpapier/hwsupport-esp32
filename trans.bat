start /wait ampy --port COM6 put D:\Dokumente\Projekte\21-hwsupport-esp32\hwsupport-esp32\boot.py
start /wait ampy --port COM6 reset
start /wait ampy --port COM6 put D:\Dokumente\Projekte\21-hwsupport-esp32\hwsupport-esp32\main.py
start /wait ampy --port COM6 reset

::LIBARIES - once put, never change
::start /wait ampy --port COM6 put D:\Dokumente\Projekte\21-hwsupport-esp32\hwsupport-esp32\ssd1306.py
::start /wait ampy --port COM6 reset
