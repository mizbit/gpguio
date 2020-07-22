import guizero
import sys
import time
filewrite = open("script.py", "w")
filewrite.write("import time\n")
filewrite.write("import gpiozero\n")

#windows
mainwindow = guizero.App(title = "gpguio by arnitdo", width = 960, height = 600)
mainwindow.hide()
LEDwindow = guizero.Window(mainwindow, width = 960, height = 600, title = "New LED")
LEDwindow.hide()
PWMLEDwindow = guizero.Window(mainwindow, width = 960, height = 600, title = "New PWM LED")
PWMLEDwindow.hide()
Sleepwindow = guizero.Window(mainwindow, width = 960, height = 600, title = "Add Sleep Timer")
Sleepwindow.hide()
LEDcontrolwindow = guizero.Window(mainwindow, width = 960, height = 600, title = "LED controls")
LEDcontrolwindow.hide()
PWMLEDcontrolwindow = guizero.Window(mainwindow, width = 960, height = 600, title = "PWMLED controls")
PWMLEDcontrolwindow.hide()
Buttonwindow  = guizero.Window(mainwindow, width = 960, height = 600, title = "New Button")
Buttonwindow.hide()
Buttoncontrolwindow = guizero.Window(mainwindow, width = 960, height = 600, title = "Button controls")
Buttoncontrolwindow.hide()
Disclaimerwindow = guizero.Window(mainwindow, width = 960, height = 600, title = "Disclaimer")
exitappwindow = guizero.Window(mainwindow, width = 240, height = 120, title = "Exit App")
exitappwindow.hide()

#Function definitions are in no particular order
def exitapppopup():
    exitappwindow.show()

def updateButtonname():
    Buttonname = Buttonnamebox.value
    Buttonpinnumber = Buttonpinnumberbox.value
    if Buttonnamebox.value !="" and Buttonpinnumber.value != "":
        Buttoncontrolbuttonselect.append(str(Buttonname))
        Buttonnamebox.clear
        Buttonwindow.hide()
        Actionlog.append("Added Button with name " + str(Buttonname) + " at GPIO pin " + str(Buttonpinnumber))
    else:
        NoButtonwarntext = guizero.Text(Buttonwindow, text = "No input given", align = "top")
def Buttonwindowexit():
    Buttonnamebox.clear()
    Buttonpinnumberbox.clear()
    Buttonwindow.hide()


def LEDwindowexit():
    LEDnamebox.clear()
    LEDpinnumberbox.clear()
    LEDwindow.hide()

def updateLEDname():
    LEDname = LEDnamebox.value
    LEDpinnumber = LEDpinnumberbox.value
    if LEDnamebox.value != "" and LEDpinnumberbox.value != "":
        LEDpowerselect.append(str(LEDname))
        filewrite.write(str(LEDname) + " = LED(" + str(LEDpinnumber) + ")\n")
        LEDnamebox.clear()
        LEDpinnumberbox.clear()
        LEDwindow.hide()
        Actionlog.append("Added LED with name " + str(LEDname) + " at GPIO pin " + str(LEDpinnumber))
    else:
        NoLEDwarntext = guizero.Text(LEDwindow, text = "No input given", align = "top")
def PWMLEDwindowexit():
    PWMLEDnamebox.clear()
    PWMLEDpinnumberbox.clear()
    PWMLEDwindow.hide()

def updatePWMLEDname():
    PWMLEDname = PWMLEDnamebox.value
    PWMLEDpinnumber = PWMLEDpinnumberbox.value
    if PWMLEDname != "" and PWMLEDpinnumber != "":
        PWMLEDpowerselect.append(str(PWMLEDname))
        filewrite.write(str(PWMLEDname) + " = PWMLED(" + str(PWMLEDpinnumber) + ")\n")
        PWMLEDnamebox.clear()
        PWMLEDpinnumberbox.clear()
        PWMLEDwindow.hide()
        Actionlog.append("Added PWMLED with name " + str(PWMLEDname) + " at GPIO pin " + str(PWMLEDpinnumber))
    else:
        NoPWMLEDwarntext = guizero.Text(PWMLEDwindow, text = "No input given", align = "top")
def PWMLEDcontrolbrightness():
    PWMbrightinput = float(PWMbrightinputbox.value)
    if ((PWMLEDpowerselect.value !=None ) and (PWMbrightinputbox.value != "")):
        filewrite.write("while True:\n" + "   " + str(PWMLEDpowerselect.value) + ".value = " + str(PWMbrightinput) + "\n")
        #added a permanent while loop. More functionality later :-)
        PWMLEDcontrolwindow.hide()
    else:
        pass
    if PWMLEDpowerselect.value == None:
        NoLEDselect = guizero.Text(LEDcontrolwindow, text = "No PWMLED selected", align = "top")
    else:
        Actionlog.append("PWMLED " + str(PWMLEDpowerselect.value) + " brightness set to " + str(PWMbrightinput))

def updateSleeptime():
    Sleeptime = Sleeptimebox.value
    filewrite.write("time.sleep(" + str(Sleeptime) + ")\n" )
    Sleeptimebox.clear()
    Sleepwindow.hide()
    Actionlog.append("Added sleep timer for "+ str(Sleeptime) + " seconds")

def Sleeptimeexit():
    Sleeptimebox.clear()
    Sleepwindow.hide()

def LEDpowerON():
    if LEDpowerselect.value != None:
        filewrite.write(str(LEDpowerselect.value) + ".on()\n")
        LEDcontrolwindow.hide()
    else:
        pass
    if LEDpowerselect.value == None:
        NoLEDselect = guizero.Text(LEDcontrolwindow, text = "No LED selected", align = "top")
    else:
        Actionlog.append("LED " + str(LEDpowerselect.value) + " will turn ON")

def LEDpowerOFF():
    if LEDpowerselect.value != None:
        filewrite.write(str(LEDpowerselect.value) + ".on()\n")
        LEDcontrolwindow.hide()
    else:
        pass
    if LEDpowerselect.value == None:
        NoLEDselect = guizero.Text(LEDcontrolwindow, text = "No LED selected", align = "top")
    else:
        Actionlog.append("LED " + str(LEDpowerselect.value) + " will turn OFF")

def Disclaimeraccept():
    Disclaimerwindow.destroy()
    mainwindow.show()

def Disclaimerdecline():
    Disclaimerwindow.destroy()
    mainwindow.destroy()

#All widgets based on window

#Disclaimerwindow
Disclaimerdeclinebutton = guizero.PushButton(Disclaimerwindow, command = Disclaimerdecline, text = "Exit", align = "bottom", padx = 38)
Disclaimeracceptbutton = guizero.PushButton(Disclaimerwindow, command = Disclaimeraccept, text = "I understand", align = "bottom")
Disclaimertext1 = guizero.Text(Disclaimerwindow, text = "The creator of this program is not responsible for :\n1)Damage caused to electrical components\n2)Harm caused to the user by electrical components\n3)Loss of functionality of electrical components\n")
Disclaimertext2 = guizero.Text(Disclaimerwindow, text = "Note that the program does not interact with any components\nIt merely creates code which the user can run at their own risk\n")
Disclaimertext3 = guizero.Text(Disclaimerwindow, text = "Program made by arnitdo\ngithub.com/arnitdo")

#Buttonwindow
Buttonnametext = guizero.Text(Buttonwindow, text = "\nName of new Button")
Buttonnamebox = guizero.TextBox(Buttonwindow)
Buttonpinnumbertext = guizero.Text(Buttonwindow, text = "\nPin to which button is connedted")
Buttonpinnumberbox = guizero.TextBox(Buttonwindow)
Buttonselectexitbutton = guizero.PushButton(Buttonwindow, command = Buttonwindowexit, text = "Cancel", align = "bottom", padx = 14)
Buttonnameconfirmbutton = guizero.PushButton(Buttonwindow, command = updateButtonname, text = "Confirm", align = "bottom")

#Buttoncontrolwindow
Buttoncontrolbuttonselect = guizero.ListBox(Buttoncontrolwindow, items = [], scrollbar = True, height = 150, width = 150, align = "left")
Buttoncontrolactionselect = guizero.ListBox(Buttoncontrolwindow, items = ["TURN LED ON WHEN PRESSED", "TURN LED ON WHILE PRESSED", "TURN LED ON WHEN PRESSED", "TURN LED OFF WHEN PRESSED"], scrollbar = True, height = 150, width = 150, align = "left")
ButtoncontrolLEDselect = guizero.ListBox(Buttoncontrolwindow, items = [], scrollbar = True, height = 150, width = 150, align = "left")
#mainwindow

LEDselectbutton = guizero.PushButton(mainwindow, command = LEDwindow.show, text = "New LED", padx = 39)
PWMLEDselectbutton = guizero.PushButton(mainwindow, command = PWMLEDwindow.show, text = "New PWMLED", padx = 22)
Sleepwindowbutton = guizero.PushButton(mainwindow, command = Sleepwindow.show, text = "Add Sleep Timer", padx = 14)
LEDcontrolwindowbutton = guizero.PushButton(mainwindow, command = LEDcontrolwindow.show, text = "LED Controls", padx = 26)
PWMLEDcontrolwindowbutton = guizero.PushButton(mainwindow, command = PWMLEDcontrolwindow.show, text = "PWMLED Controls", padx = 10)
Buttonwindowbutton = guizero.PushButton(mainwindow, command = Buttonwindow.show, text = "New Button", padx = 30)
mainwindowexitbutton = guizero.PushButton(mainwindow, command = exitapppopup, text = "Save and Quit", align = "top", padx = 22)
Actionlogtext = guizero.Text(mainwindow, text = "\nLog :")
Actionlog = guizero.ListBox(mainwindow, items = [], scrollbar = True, height = 150, width = 400)
#LEDwindow

LEDselectexitbutton = guizero.PushButton(LEDwindow, command = LEDwindowexit, text = "Cancel", align = "bottom", padx = 14)
LEDnameconfirmbutton = guizero.PushButton(LEDwindow, command = updateLEDname, text = "Confirm", align = "bottom")

#PWM LED WINDOW
PWMLEDselectexitbutton = guizero.PushButton(PWMLEDwindow, command = PWMLEDwindowexit, text = "Cancel", align = "bottom", padx = 14)
PWMLEDnameconfirmbutton = guizero.PushButton(PWMLEDwindow, command = updatePWMLEDname, text = "Confirm", align = "bottom")
#Sleepwindow

Sleeptimeconfirmbutton = guizero.PushButton(Sleepwindow, command = updateSleeptime, text = "Confirm Sleep Timer", align ="bottom")
Sleeptimeexitbutton = guizero.PushButton(Sleepwindow, command = Sleeptimeexit, text = "Cancel", align = "bottom", padx = 55)

#LEDcontrolwindow
LEDPowertext = guizero.Text(LEDcontrolwindow, text = "Power ON / OFF LEDs.\nSelect LED from dropdown list.\nLEDs must be created first using the \nNew LED option in the main window")
LEDpowerselect = guizero.ListBox(LEDcontrolwindow, items = [], scrollbar = True, height = 150, width = 150)
PowerONbutton =  guizero.PushButton(LEDcontrolwindow, text = "Turn Selected LED ON", align = "top", command = LEDpowerON, padx = 13)
PowerOFFbutton =  guizero.PushButton(LEDcontrolwindow, text = "Turn Selected LED OFF", align = "top", command = LEDpowerOFF)
LEDcontrolwindowexitbutton = guizero.PushButton(LEDcontrolwindow, text = "Cancel", command = LEDcontrolwindow.hide, align = "top", padx = 62)

#PWMLEDcontrolwindow
PWMLEDPowertext = guizero.Text(PWMLEDcontrolwindow, text = "Control PWM LEDS.\nSelect LED from dropdown list.\nPWMLEDs must be created first using the \nNew PWMLED option in the main window")
PWMLEDpowerselect = guizero.ListBox(PWMLEDcontrolwindow, items = [], scrollbar = True, height = 150, width = 150)
PWMLEDbrighttext = guizero.Text(PWMLEDcontrolwindow, text = "Set PWM brightness\nMin value = 0 (OFF)\nMax value = 1 (Full Brightness)\nInput any decimal value from 0 to 1")
PWMbrightinputbox = guizero.TextBox(PWMLEDcontrolwindow)
PWMLEDbrightconfirmbutton = guizero.PushButton(PWMLEDcontrolwindow, command = PWMLEDcontrolbrightness, text = "Confirm")
PWMLEDcontrolwindowexitbutton = guizero.PushButton(PWMLEDcontrolwindow, text = "Cancel", command = PWMLEDcontrolwindow.hide, align = "top", padx = 15)

#user input fields

LEDnametext = guizero.Text(LEDwindow, text="\nLED name (can be anything reasonable)")
LEDnamebox = guizero.TextBox(LEDwindow)
LEDpinnumbertext = guizero.Text(LEDwindow, text = "\nPhysical pin number to which LED is connected.\nShould be any number from 1 to 40\nSee pinout.xyz for more info or\nrun command pinout on your raspberry pi")
LEDpinnumberbox = guizero.TextBox(LEDwindow)
PWMLEDnametext = guizero.Text(PWMLEDwindow, text="\nPWMLED name (can be anything reasonable)")
PWMLEDnamebox = guizero.TextBox(PWMLEDwindow)
PWMLEDpinnumbertext = guizero.Text(PWMLEDwindow, text = "\nPhysical pin number to which PWMLED is connected.\nShould be any number from 1 to 40\nSee pinout.xyz for more info or\nrun command pinout on your raspberry pi")
PWMLEDpinnumberbox = guizero.TextBox(PWMLEDwindow)
Sleeptimetext = guizero.Text(Sleepwindow, text = "\nSleep time (in seconds)")
Sleeptimebox = guizero.TextBox(Sleepwindow)


#Exit app popup
exitappwindowtext = guizero.Text(exitappwindow, text = "Thank you for using gpguio\nFile saved as script.py")
exitappconfirm = guizero.PushButton(exitappwindow, command = mainwindow.destroy, text = "OK", align = "bottom", padx = 20)
#End of file

mainwindow.display()
filewrite.close()
sys.exit()