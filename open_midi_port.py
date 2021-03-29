import time
import rtmidi

midiout = rtmidi.MidiOut()
midiin = rtmidi.MidiIn()

available_ports = midiout.get_ports()

#select APC Key 25 port

for i in range(len(available_ports)):
    if 'APC Key 25' in available_ports[i]:
        midiout.open_port(i)
        midiin.open_port(i)
        

