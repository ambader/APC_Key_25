# APC_Key_25
Control the Apc Key 25 pad


## Preview
![sample_gif](https://raw.githubusercontent.com/ambader/APC_Key_25/main/sample.gif)
![Dwld Vid](https://raw.githubusercontent.com/ambader/APC_Key_25/main/apc_key_25.webm)

## Background
The APC Key 25 has colorful buttons which can be turned on and off by Midi-Messages.
By reading the output of the keyboard, I identified the 5x8 Matrix buttons to be eqal to [144, x, 0], where x is between 0 and 39.
To change the light of a particular button, one has to send a Midi-Message [144, x, y], where y determines the color:

0 - off\
1 - green\
2 - green flashing\
3 - red\
4 - red flashing\
5 - yellow\
6 - yellow flashing

Other DAW controller may work the same way

## How to use
```python
 pip install rtmidi-python
 # there are several modules called rtmidi, you may have to uninstall the other version 
```

open_midi_port.py
```python
import rtmidi

midiout = rtmidi.MidiOut()
midiin = rtmidi.MidiIn()

available_ports = midiout.get_ports()

#select APC Key 25 port

for i in range(len(available_ports)):
    if 'APC Key 25' in available_ports[i]:
        midiout.open_port(i)
        midiin.open_port(i)
```

send_midi_sample.py
```python
import numpy as np
import time

middle=[9,10,11,12,13,14,17,18,21,22,25,26,27,28,29,30]
core=[19,20]
surround=[0,1,2,3,4,5,6,7,8,15,16,23,24,31,32,33,34,35,36,37,38,39]

def colorize(inp):
    for i in middle:
        midiout.send_message([144, i, inp[0]])
    for i in surround:
        midiout.send_message([144, i, inp[1]])
    for i in core:
        midiout.send_message([144, i, inp[2]])
        
def alive_col(inp,timer):
    nn=1
    for i in range(timer*5):
        inpp=np.roll(inp,nn)
        colorize(inpp)
        nn+=1
        time.sleep(0.2)
        for j in range(40):
            midiout.send_message([144, j, 0])
    
```

```python
alive_col([1,3,5],3)
alive_col([1,1,5],3)
alive_col([3,3,5],3)
alive_col([3,3,1],3)
alive_col([1,3,5],3)
```
