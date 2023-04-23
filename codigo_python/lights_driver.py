import serial
import time
import tkinter
from arduino_lights_driver import ArduinoLightsDriver

# Funciones para editar la GUI
def set_enable_label_laser(driver, enabled_label):
    if driver.laser_is_enabled:
        text = "Enabled"
    else:
        text = "Disabled"
    enabled_label.config(text=text)

def set_enable_label_led(driver, enabled_label):
    if driver.led_is_enabled:
        text = "Enabled"
    else:
        text = "Disabled"
    enabled_label.config(text=text)

def set_always_on_label_laser(driver, enabled_label):
    if driver.laser_is_always_on:
        text = "Always On"
    else:
        text = "Not Always On"
    enabled_label.config(text=text)

def set_always_on_label_led(driver, enabled_label):
    if driver.led_is_always_on:
        text = "Always On"
    else:
        text = "Not Always On"
    enabled_label.config(text=text)

def enable_laser(driver, enabled_label):
    driver.enable_laser()
    set_enable_label_laser(driver, enabled_label)

def disable_laser(driver, enabled_label):
    driver.disable_laser()
    set_enable_label_laser(driver, enabled_label)

def always_on_laser(driver, enabled_label):
    driver.always_on_laser()
    set_always_on_label_laser(driver, enabled_label)

def always_off_laser(driver, enabled_label):
    driver.always_off_laser()
    set_always_on_label_laser(driver, enabled_label)

def enable_led(driver, enabled_label):
    driver.enable_led()
    set_enable_label_led(driver, enabled_label)

def disable_led(driver, enabled_label):
    driver.disable_led()
    set_enable_label_led(driver, enabled_label)

def always_on_led(driver, enabled_label):
    driver.always_on_led()
    set_always_on_label_led(driver, enabled_label)

def always_off_led(driver, enabled_label):
    driver.always_off_led()
    set_always_on_label_led(driver, enabled_label)

def set_current_laser(driver, new_current, current_label):
    driver.set_current_laser(new_current)
    current_label.config(text=driver.current)

WIN_WIDTH = 800
WIN_HEIGHT = 600

tk_top = tkinter.Tk()
tk_top.protocol("WM_DELETE_WINDOW", lambda: quit(tk_top))
tk_top.geometry(str(WIN_WIDTH) + 'x' + str(WIN_HEIGHT))
tk_top.resizable(height=False, width=False)
tk_top.title("Ilumination controller")
tk_top.counter = 0

light_driver = ArduinoLightsDriver('com14')

laser_group = tkinter.LabelFrame(tk_top, text="Laser")
laser_group.pack()

laser_current_frame = tkinter.Frame(laser_group)
laser_current_text_label = tkinter.Label(laser_current_frame, text="Current")
laser_current_label = tkinter.Label(laser_current_frame, text=str(light_driver.current))
laser_current_text_label.grid(column=0, row=0)
laser_current_label.grid(column=1, row=0)
laser_current_frame.pack()

laser_enabled_frame = tkinter.Frame(laser_group)
laser_enabled_label = tkinter.Label(laser_enabled_frame)
set_enable_label_laser(light_driver, laser_enabled_label)
laser_always_label = tkinter.Label(laser_enabled_frame)
set_always_on_label_laser(light_driver, laser_always_label)
laser_enabled_label.grid(column=0, row=0)
laser_always_label.grid(column=1, row=0)
laser_enabled_frame.pack()

laser_new_current = tkinter.Frame(laser_group)
laser_new_current_label = tkinter.Label(laser_new_current, text="New current")
laser_new_current_entry = tkinter.Entry(laser_new_current)
laser_new_current_label.grid(column=0, row=0)
laser_new_current_entry.grid(column=1, row=0)
laser_new_current.pack()

laser_buttons_frame = tkinter.Frame(laser_group)

button_set = tkinter.Button(laser_buttons_frame,
    text="Set",
    command=lambda: set_current_laser(light_driver, float(laser_new_current_entry.get()), laser_current_label),
    height = 2,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button_set.grid(column=0, row=0)

laser_button_enable = tkinter.Button(laser_buttons_frame,
    text="Enable",
    command=lambda: enable_laser(light_driver, laser_enabled_label),
    height = 2,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
laser_button_enable.grid(column=1, row=0)

laser_button_disable = tkinter.Button(laser_buttons_frame,
    text="Disable",
    command=lambda: disable_laser(light_driver, laser_enabled_label),
    height = 2,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
laser_button_disable.grid(column=2, row=0)

laser_button_always_on = tkinter.Button(laser_buttons_frame,
    text="Always On",
    command=lambda: always_on_laser(light_driver, laser_always_label),
    height = 2,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
laser_button_always_on.grid(column=3, row=0)

laser_button_always_off = tkinter.Button(laser_buttons_frame,
    text="Not Always On",
    command=lambda: always_off_laser(light_driver, laser_always_label),
    height = 2,
    fg = "black",
    width = 10,
    bd = 5,
    activebackground='green'
)
laser_button_always_off.grid(column=4, row=0)

laser_buttons_frame.pack()

# Led
led_group = tkinter.LabelFrame(tk_top, text="Led")
led_group.pack()

led_enabled_frame = tkinter.Frame(led_group)
led_enabled_label = tkinter.Label(led_enabled_frame)
set_enable_label_led(light_driver, led_enabled_label)
led_always_label = tkinter.Label(led_enabled_frame)
set_always_on_label_led(light_driver, led_always_label)
led_enabled_label.grid(column=0, row=0)
led_always_label.grid(column=1, row=0)
led_enabled_frame.pack()

led_buttons_frame = tkinter.Frame(led_group)

led_button_enable = tkinter.Button(led_buttons_frame,
    text="Enable",
    command=lambda: enable_led(light_driver, led_enabled_label),
    height = 2,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
led_button_enable.grid(column=0, row=0)

led_button_disable = tkinter.Button(led_buttons_frame,
    text="Disable",
    command=lambda: disable_led(light_driver, led_enabled_label),
    height = 2,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
led_button_disable.grid(column=1, row=0)

led_button_always_on = tkinter.Button(led_buttons_frame,
    text="Always On",
    command=lambda: always_on_led(light_driver, led_always_label),
    height = 2,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
led_button_always_on.grid(column=2, row=0)

led_button_always_off = tkinter.Button(led_buttons_frame,
    text="Not Always On",
    command=lambda: always_off_led(light_driver, led_always_label),
    height = 2,
    fg = "black",
    width = 10,
    bd = 5,
    activebackground='green'
)
led_button_always_off.grid(column=3, row=0)

tkButtonQuit = tkinter.Button(
    tk_top,
    text="Quit",
    command=lambda: quit(tk_top),
    height = 2,
    fg = "black",
    width = 8,
    bg = 'yellow',
    bd = 5
)

led_buttons_frame.pack()

tkButtonQuit.pack(side='top', ipadx=10, padx=10, pady=15)

tkinter.mainloop()