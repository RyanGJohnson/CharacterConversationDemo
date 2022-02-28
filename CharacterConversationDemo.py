import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import WORD #enables word wrap functions
import os
import openai


#Testing Repair
#having a hard time with X and Y coordinates. They are swapped. So X is Y and Y is X 
class NPC:
  def __init__(self, name, description, roomX, roomY, icon):
    self.name = name
    self.description = description
    self.roomX = roomX
    self.roomY = roomY
    self.mapIcon = icon

class Player:
  def __init__(self, userName, name, description, roomX, roomY, icon):
    self.userName = userName
    self.name = name
    self.description = description
    self.roomX = roomX
    self.roomY = roomY
    self.mapIcon = icon

class Room:
    def __init__(self, description, roomX, roomY, exitN, exitE, exitS, exitW, lookN, lookE, lookS, lookW, roomIcon):
        self.description = description
        self.roomX = roomX
        self.roomY = roomY
        self.exitN = exitN
        self.exitE = exitE
        self.exitS = exitS
        self.exitW = exitW
        self.lookN = lookN
        self.lookE = lookE
        self.lookS = lookS
        self.lookW = lookW
        self.roomIcon = roomIcon

#Create Bartender NPC
bartender = NPC("Brynn BattleBrew", "Before you stands a gruff looking Dwarf standing about five feet tall wearing a pristine bartenders apron. He has red braided hair and a thick beard and mustache. He looks short, sturdy, and strong. He looks about the bar with stern yet friendly eyes.", 2, 1, "J")

oldWizard =NPC("Fizzle Sprock", "Before you sits an old human wizard that is named Fizzle Sprock senile after years of adventures dozes lightly by the fire in a comfortable chair.", 1, 2, "J")
#Create default Player for testing only
playerCharacter = Player("Tester", "Traveler", "You are heavily cloaked. It is hard to tell who or what you are. ", 4, 1, "v")

#Room Initialized
room00 = Room("You see an outdoor grass at North West corner of the BattleBrew Tavern.", 0, 0, False, True, True, False, "A fence blocks your path showing rolling grass to infinity", "Grass along the back of the tavern.", "Grass along the side of the tavern.", "The tavern fence blocks your path.", "o")
room01 = Room("You see a grass area at back of the tavern.", 0, 1, False, True, False, True, "A fence blocks your path showing rolling grass to infinity", "Grass along the back of the tavern.", "Sturdy outer wall of tavern.", "Grass along back of the tavern.", "o")
room02 = Room("You see a grass area at back of the tavern.", 0, 2, False, True, False, True, "A fence blocks your path showing rolling grass to infinity", "Grass along the back of the tavern.", "Sturdy outer wall of tavern. You can tell see the stones of the fireplace and a window looking into the tavern.", "Grass along back of the tavern.", "o")
room03 = Room("You see a grass area at back of the tavern.", 0, 3, False, True, False, True, "A fence blocks your path showing rolling grass to infinity", "Grass along the back of the tavern.", "Sturdy outer wall of Tavern.", "Grass along back of the tavern.", "o")
room04 = Room("You see an outdoor grass at the Northeast corner of the BattleBrew Tavern.", 0, 4, False, False, True, True, "A fence blocks your path showing rolling grass to infinity.", "A fence blocks your path showing rolling grass to infinity.", "Grass along the eastern side of the tavern.", "Grass along the back of the tavern.", "o")
room10 = Room("You see an outdoor grass at West side of the BattleBrew Tavern.", 1, 0, True, False, True, False, "Grass along the back of the tavern.", "Sturdy outer wall of tavern.", "Grass along the side of the tavern.", "The tavern fence blocks your path.", "o")
room11 = Room("You see a tavern kitchen and pantry.", 1, 1, False, False, True, False, "A dirty kitchen wall.", "The pantry at the back of the kitchen.", "The tavern bar.", "Stacks of dishes pilled along the kitchen wall.", "o")
room12 = Room("You see a fireplace and comfortable chairs. A sleeping wizard warms himself by the fire.", 1, 2, False, True, True, False, "A roaring fire warms the tavern.", "A staircase leading upstairs.", "Dining tables and chairs.", "Kitchen wall extends near the fireplace.", "o")
room13 = Room("You see a stairs leading up to tavern rentable rooms.", 1, 3, False, False, True, True, "A picture of an elderly wall hangs above the stairs.", "The tavern wall.", "Dining tables and chairs.", "A wizard sleeps in a chair by the fire.", "o")
room14 = Room("You see an outdoor grass at the East side of the BattleBrew Tavern.", 1, 4, True, False, True, False, "Grass in the Northeast corner of the tavern.", " A fence blocks your path showing rolling grass to infinity.", "Grass along the side of the tavern.", " Sturdy outer wall of Tavern.", "o")
room20 = Room("You see an outdoor grass at the West side of the BattleBrew Tavern.", 2, 0, True, False, True, False, "Grass along the side of the tavern.", "Sturdy outer wall of Tavern. Inside the window you see the tavern bar.", "Grass along the side of the tavern.", "The tavern fence blocks your path.", "o")
room21 = Room("You see a tavern bar made of finely crafted wood. Fine bottles of alcohol and various drinks line the mirrored wall. Above the bar rests a well-used axe and shield. Finely crafted lanterns on the wall bath the bar with a rosy warm magical light.", 2, 1, True, True, True, False, "The door north leads to a kitchen. A counter built into the wall allows the cook to hand food through to the tavern staff behind the bar.", "Tables and comfortable chairs are in the middle of the tavern. Warm soft fire light fills the area. A wizard sleeps in a chair by the fire.", "The entrance to the Tavern with a sturdy well used wooden door engraved with dwarven runes.", "A window with stained glass, depicting a battle with a dragon, rests on a well-worn yet sturdy wooden wall crafted from some huge ancient tree. Beyond you can vaguely see the grassy fields outside.", "o")
room22 = Room("You see a center dining area of tavern with tables and comfortable chairs.", 2, 2, True, True, True, True, "A wizard sleeps in a chair by the fire.", "Dining tables and chairs.", "The tavern stage.", "The tavern bar and bartender.", "o")
room23 = Room("You see dining tables and chairs.", 2, 3, True, False, True, True, "The tavern stairs.", "The tavern wall.", "A dimly lit private table.", "The center of the dining area.", "o")
room24 = Room("You see an outdoor grass at the east side of the BattleBrew Tavern.", 2, 4, True, False, True, False, "Grass along the side of the tavern.", " A fence blocks your path showing rolling grass to infinity.", "Grass along the side of the tavern.", "Sturdy outer wall of Tavern.", "o")
room30 = Room("You see an outdoor grass at the west side of the BattleBrew Tavern.", 3, 0, True, False, True, False, "Grass along the side of the tavern.", "Sturdy outer wall of Tavern.", "Grass in the Southwest corner of the tavern.", "The tavern fence blocks your path.", "o")
room31 = Room("You see an inner entrance to BattleBrew Tavern.", 3, 1, True, False, True, False, "The tavern bar and bartender.", "The tavern stage.", "The tavern door and exit.", "The tavern wall.", "o")
room32 = Room("You see a tavern stage and fine dining.", 3, 2, True, False, False, False, "The center of the dining area.", "A dimly lit private table.", "The stage curtains and tavern wall.", "The inner entrance to the tavern.", "o")
room33 = Room("You see a quite dim private table in the southeast corner of the tavern.", 3, 3, True, False, False, False, "Dining tables and chairs.", "The tavern wall.", "The tavern wall.", "The tavern stage.", "o")
room34 = Room("You see an outdoor grass at east side of the BattleBrew Tavern.", 3, 4, True, False, True, False, "Grass along the side of the tavern.", " A fence blocks your path showing rolling grass to infinity.", "Grass in the Southeast corner of the tavern.", "Sturdy outer wall of Tavern.", "o")
room40 = Room("You see an outdoor grass at southwest Corner of the BattleBrew Tavern.", 4, 0, True, True, False, False, "Grass along the side of the tavern.", "The path and entrance of the tavern.", "The path leading to the entrance of the tavern.", " The tavern fence blocks your path.", "o")
room41 = Room("You see an outdoor entrance to the tavern.", 4, 1, True, True, False, True, "Tavern Entrance and old wooden door.", "Grass along the side of the tavern.", "Path leading to the entrance of the Tavern", "You see an outdoor grass at the Southwest Corner of the BattleBrew Tavern.", "o")
room42 = Room("You see an outdoor grass at the south side of the BattleBrew Tavern.", 4, 2, False, True, False, True, "Through the tavern window you can see the tavern stage. You can hear the music coming from inside.", "Grass along the side of the tavern.", "The path leading up to the tavern.", "The path ends at the entrance to the tavern.", "o")
room43 = Room("You see an outdoor grass and a pile of lumber at the south side of the BattleBrew Tavern.", 4, 3, False, True, False, True, "The sturdy tavern wall", "Grass along the side of the tavern.", "In the distance, you see a small town. The tavern’s fence blocks your path.", "Grass along the side of the tavern.", "o")
room44 = Room("You see an outdoor grass at the southeast corner of the BattleBrew Tavern.", 4, 4, True, False, False, True, "Grass along the side of the tavern.", "A fence blocks your path showing rolling grass to infinity.", " In the distance, you see a small town. The tavern’s fence blocks your path.", "Grass along the side of the tavern.", "o")


roomDescArry = [[room00.description, room01.description, room02.description, room03.description, room04.description], [room10.description, room11.description, room12.description, room13.description, room14.description], [room20.description, room21.description, room22.description, room23.description, room24.description], [room30.description, room31.description, room32.description, room33.description, room34.description], [room40.description, room41.description, room42.description, room43.description, room44.description]]
roomDescArryN = [[room00.lookN, room01.lookN, room02.lookN, room03.lookN, room04.lookN], [room10.lookN, room11.lookN, room12.lookN, room13.lookN, room14.lookN], [room20.lookN, room21.lookN, room22.lookN, room23.lookN, room24.lookN], [room30.lookN, room31.lookN, room32.lookN, room33.lookN, room34.lookN], [room40.lookN, room41.lookN, room42.lookN, room43.lookN, room44.lookN]]
roomDescArryS = [[room00.lookS, room01.lookS, room02.lookS, room03.lookS, room04.lookS], [room10.lookS, room11.lookS, room12.lookS, room13.lookS, room14.lookS], [room20.lookS, room21.lookS, room22.lookS, room23.lookS, room24.lookS], [room30.lookS, room31.lookS, room32.lookS, room33.lookS, room34.lookS], [room40.lookS, room41.lookS, room42.lookS, room43.lookS, room44.lookS]]
roomDescArryE = [[room00.lookE, room01.lookE, room02.lookE, room03.lookE, room04.lookE], [room10.lookE, room11.lookE, room12.lookE, room13.lookE, room14.lookE], [room20.lookE, room21.lookE, room22.lookE, room23.lookE, room24.lookE], [room30.lookE, room31.lookE, room32.lookE, room33.lookE, room34.lookE], [room40.lookE, room41.lookE, room42.lookE, room43.lookE, room44.lookE]]
roomDescArryW = [[room00.lookW, room01.lookW, room02.lookW, room03.lookW, room04.lookW], [room10.lookW, room11.lookW, room12.lookW, room13.lookW, room14.lookW], [room20.lookW, room21.lookW, room22.lookW, room23.lookW, room24.lookW], [room30.lookW, room31.lookW, room32.lookW, room33.lookW, room34.lookW], [room40.lookW, room41.lookW, room42.lookW, room43.lookW, room44.lookW]]


locationDesc= roomDescArry[playerCharacter.roomX][playerCharacter.roomY]
playerDescription = playerCharacter.name + ". " + playerCharacter.description
promptB = playerCharacter.description + room21.description + "\n" + bartender.description + " The Bartender introduces himself as " +bartender.name + ".\n"
promptW = playerCharacter.description + room12.description + "\n" + oldWizard.description + "\n"
reSubmitPlaceholder = ""

def setLocationDesc():
    locationDesc = roomDescArry[playerCharacter.roomX][playerCharacter.roomY]
def submitAI():

    if bartender.roomX == playerCharacter.roomX and bartender.roomY == playerCharacter.roomY:
        
        txt_conversation.delete("1.0",tk.END)
        global promptB
        global reSubmitPlaceholder
        reSubmitPlaceholder = promptB
        inputedText = txt_edit.get("1.0","end-1c")
        prompt1 =  promptB +"\n" + inputedText + "\n\n" + "BattleBrew:"
            
        
        #ai portion
        openai.api_key = ('API KEY GOES HERE')

        start_sequence = "\nBattleBrew:"
        restart_sequence = "\n" + playerCharacter.name + ":"

        response = openai.Completion.create(
          engine="davinci",
          prompt=prompt1,
          temperature=0.9,
          max_tokens=50,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0.6,
          stop=["\n", playerCharacter.name + ":", "BattleBrew:"]
        )
        prompt1 = prompt1 + response['choices'][0]['text'] + "\n\n"
        promptB = prompt1 + playerCharacter.name + ":"
        txt_conversation.insert(tk.INSERT, prompt1 )
        txt_edit.delete("1.0",tk.END)

    if oldWizard.roomX == playerCharacter.roomX and oldWizard.roomY == playerCharacter.roomY:
        
        txt_conversation.delete("1.0",tk.END)
        global promptW
        reSubmitPlaceholder = promptW
        inputedText = txt_edit.get("1.0","end-1c")
        prompt1 =  promptW +"\n" + inputedText + "\n\n" + "Fizzle:"
            
        
        #ai portion
        openai.api_key = ('API KEY GOES HERE')

        start_sequence = "\nFizzle:"
        restart_sequence = "\n" + playerCharacter.name + ":"

        response = openai.Completion.create(
          engine="davinci",
          prompt=prompt1,
          temperature=0.9,
          max_tokens=50,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0.6,
          stop=["\n", playerCharacter.name + ":", "Fizzle:"]
        )
        prompt1 = prompt1 + response['choices'][0]['text'] + "\n\n"
        promptW = prompt1 + playerCharacter.name + ":"
        txt_conversation.insert(tk.INSERT, prompt1 )
        txt_edit.delete("1.0",tk.END)
    txt_conversation.yview_moveto( 1 ) #forces textbox to scroll to bottom.

def reSubmit():
    global promptB
    global promptW
    global reSubmitPlaceholder
    if bartender.roomX == playerCharacter.roomX and bartender.roomY == playerCharacter.roomY:
        promptB= reSubmitPlaceholder
    if oldWizard.roomX == playerCharacter.roomX and oldWizard.roomY == playerCharacter.roomY:
        promptW = reSubmitPlaceholder
    submitAI()


#def checkResponse():
    #just for  testing appled to retry buton
    
    


def open_file():
    """Open a file for editing."""
    global promptB
    global promptW
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_conversation.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_conversation.insert(tk.END, text)
    if bartender.roomX == playerCharacter.roomX and bartender.roomY == playerCharacter.roomY:
        promptB= text
    if oldWizard.roomX == playerCharacter.roomX and oldWizard.roomY == playerCharacter.roomY:
        promptW= text
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_conversation.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")
    

def move_N():
    """move north button controls."""    
    #unlock map
    map.configure(state='normal')
    #Clear map to default
    map.delete("1.0",tk.END)
    mapArrayIcons = [[room00.roomIcon, room01.roomIcon, room02.roomIcon, room03.roomIcon, room04.roomIcon],[room10.roomIcon, room11.roomIcon, room12.roomIcon, room13.roomIcon, room14.roomIcon],[room20.roomIcon, room21.roomIcon, room22.roomIcon, room23.roomIcon, room24.roomIcon],[room30.roomIcon, room31.roomIcon, room32.roomIcon, room33.roomIcon, room34.roomIcon],[room40.roomIcon, room41.roomIcon, room42.roomIcon, room43.roomIcon, room44.roomIcon]]
    #update Bartender on Map
    mapArrayIcons[bartender.roomX][bartender.roomY] = bartender.mapIcon
    #update wizard on map
    mapArrayIcons[oldWizard.roomX][oldWizard.roomY] = oldWizard.mapIcon
    #update Player on Map
    moveNcheck = [[room00.exitN, room01.exitN, room02.exitN, room03.exitN, room04.exitN],[room10.exitN, room11.exitN, room12.exitN, room13.exitN, room14.exitN],[room20.exitN, room21.exitN, room22.exitN, room23.exitN, room24.exitN],[room30.exitN, room31.exitN, room32.exitN, room33.exitN, room34.exitN],[room40.exitN, room41.exitN, room42.exitN, room43.exitN, room44.exitN]]
    if moveNcheck[playerCharacter.roomX][playerCharacter.roomY] == True:
        playerCharacter.roomX = playerCharacter.roomX - 1
        #updates description text box
        txt_description.delete("1.0", tk.END)
        txt_description.insert(tk.INSERT, roomDescArry[playerCharacter.roomX][playerCharacter.roomY] + "\nTo the north you see:\n" + roomDescArryN[playerCharacter.roomX][playerCharacter.roomY] + "\nTo the east you see:\n" + roomDescArryE[playerCharacter.roomX][playerCharacter.roomY]+ "\nTo the south you see:\n" + roomDescArryS[playerCharacter.roomX][playerCharacter.roomY]+ "\nTo the west you see:\n" + roomDescArryW[playerCharacter.roomX][playerCharacter.roomY])
    #adds player icon
    mapArrayIcons[playerCharacter.roomX][playerCharacter.roomY] = playerCharacter.mapIcon
    #updates map 
    for row in mapArrayIcons:
        map.insert(tk.INSERT, "\n")
        for col in row:
            map.insert(tk.INSERT, col)
    #Locks Map
    map.configure(state='disabled')
    #check if NPC is present and start conversation.
    submitAI()
    
def move_E():
    """move East button controls."""
    #unlock map
    map.configure(state='normal')
    #Clear map to default
    map.delete("1.0",tk.END)
    mapArrayIcons = [[room00.roomIcon, room01.roomIcon, room02.roomIcon, room03.roomIcon, room04.roomIcon],[room10.roomIcon, room11.roomIcon, room12.roomIcon, room13.roomIcon, room14.roomIcon],[room20.roomIcon, room21.roomIcon, room22.roomIcon, room23.roomIcon, room24.roomIcon],[room30.roomIcon, room31.roomIcon, room32.roomIcon, room33.roomIcon, room34.roomIcon],[room40.roomIcon, room41.roomIcon, room42.roomIcon, room43.roomIcon, room44.roomIcon]]
    #update Bartender on Map
    mapArrayIcons[bartender.roomX][bartender.roomY] = bartender.mapIcon
    #update wizard on map
    mapArrayIcons[oldWizard.roomX][oldWizard.roomY] = oldWizard.mapIcon
    #update Player on Map
    moveScheck = [[room00.exitE, room01.exitE, room02.exitE, room03.exitE, room04.exitE],[room10.exitE, room11.exitE, room12.exitE, room13.exitE, room14.exitE],[room20.exitE, room21.exitE, room22.exitE, room23.exitE, room24.exitE],[room30.exitE, room31.exitE, room32.exitE, room33.exitE, room34.exitE],[room40.exitE, room41.exitE, room42.exitE, room43.exitE, room44.exitE]]
    if moveScheck[playerCharacter.roomX][playerCharacter.roomY] == True:
        playerCharacter.roomY = playerCharacter.roomY + 1
        #updates description text box
        txt_description.delete("1.0", tk.END)
        txt_description.insert(tk.INSERT, roomDescArry[playerCharacter.roomX][playerCharacter.roomY] + "\nTo the north you see:\n" + roomDescArryN[playerCharacter.roomX][playerCharacter.roomY] + "\nTo the east you see:\n" + roomDescArryE[playerCharacter.roomX][playerCharacter.roomY]+ "\nTo the south you see:\n" + roomDescArryS[playerCharacter.roomX][playerCharacter.roomY]+ "\nTo the west you see:\n" + roomDescArryW[playerCharacter.roomX][playerCharacter.roomY])
    #adds player icon
    mapArrayIcons[playerCharacter.roomX][playerCharacter.roomY] = playerCharacter.mapIcon
    #updates map 
    for row in mapArrayIcons:
        map.insert(tk.INSERT, "\n")
        for col in row:
            map.insert(tk.INSERT, col)
    #Locks Map
    map.configure(state='disabled')
    #check if bartender is present and start conversation.
    submitAI()
def move_S():
    """move South button controls."""
    #unlock map
    map.configure(state='normal')
    #Clear map to default
    map.delete("1.0",tk.END)
    mapArrayIcons = [[room00.roomIcon, room01.roomIcon, room02.roomIcon, room03.roomIcon, room04.roomIcon],[room10.roomIcon, room11.roomIcon, room12.roomIcon, room13.roomIcon, room14.roomIcon],[room20.roomIcon, room21.roomIcon, room22.roomIcon, room23.roomIcon, room24.roomIcon],[room30.roomIcon, room31.roomIcon, room32.roomIcon, room33.roomIcon, room34.roomIcon],[room40.roomIcon, room41.roomIcon, room42.roomIcon, room43.roomIcon, room44.roomIcon]]
    #update Bartender on Map
    mapArrayIcons[bartender.roomX][bartender.roomY] = bartender.mapIcon
    #update wizard on map
    mapArrayIcons[oldWizard.roomX][oldWizard.roomY] = oldWizard.mapIcon
    #update Player on Map
    moveScheck = [[room00.exitS, room01.exitS, room02.exitS, room03.exitS, room04.exitS],[room10.exitS, room11.exitS, room12.exitS, room13.exitS, room14.exitS],[room20.exitS, room21.exitS, room22.exitS, room23.exitS, room24.exitS],[room30.exitS, room31.exitS, room32.exitS, room33.exitS, room34.exitS],[room40.exitS, room41.exitS, room42.exitS, room43.exitS, room44.exitS]]
    if moveScheck[playerCharacter.roomX][playerCharacter.roomY] == True:
        playerCharacter.roomX = playerCharacter.roomX + 1
        #updates description text box
        txt_description.delete("1.0", tk.END)
        txt_description.insert(tk.INSERT, roomDescArry[playerCharacter.roomX][playerCharacter.roomY] + "\nTo the north you see:\n" + roomDescArryN[playerCharacter.roomX][playerCharacter.roomY] + "\nTo the east you see:\n" + roomDescArryE[playerCharacter.roomX][playerCharacter.roomY]+ "\nTo the south you see:\n" + roomDescArryS[playerCharacter.roomX][playerCharacter.roomY]+ "\nTo the west you see:\n" + roomDescArryW[playerCharacter.roomX][playerCharacter.roomY])
    #adds player icon
    mapArrayIcons[playerCharacter.roomX][playerCharacter.roomY] = playerCharacter.mapIcon
    #updates map 
    for row in mapArrayIcons:
        map.insert(tk.INSERT, "\n")
        for col in row:
            map.insert(tk.INSERT, col)
    #Locks Map
    map.configure(state='disabled')
    #check if bartender is present and start conversation.
    submitAI()
def move_W():
    """move East button controls."""
    #unlock map
    map.configure(state='normal')
    #Clear map to default
    map.delete("1.0",tk.END)
    mapArrayIcons = [[room00.roomIcon, room01.roomIcon, room02.roomIcon, room03.roomIcon, room04.roomIcon],[room10.roomIcon, room11.roomIcon, room12.roomIcon, room13.roomIcon, room14.roomIcon],[room20.roomIcon, room21.roomIcon, room22.roomIcon, room23.roomIcon, room24.roomIcon],[room30.roomIcon, room31.roomIcon, room32.roomIcon, room33.roomIcon, room34.roomIcon],[room40.roomIcon, room41.roomIcon, room42.roomIcon, room43.roomIcon, room44.roomIcon]]
    #update Bartender on Map
    mapArrayIcons[bartender.roomX][bartender.roomY] = bartender.mapIcon
    #update wizard on map
    mapArrayIcons[oldWizard.roomX][oldWizard.roomY] = oldWizard.mapIcon
    #update Player on Map
    moveScheck = [[room00.exitW, room01.exitW, room02.exitW, room03.exitW, room04.exitW],[room10.exitW, room11.exitW, room12.exitW, room13.exitW, room14.exitW],[room20.exitW, room21.exitW, room22.exitW, room23.exitW, room24.exitW],[room30.exitW, room31.exitW, room32.exitW, room33.exitW, room34.exitW],[room40.exitW, room41.exitW, room42.exitW, room43.exitW, room44.exitW]]
    if moveScheck[playerCharacter.roomX][playerCharacter.roomY] == True:
        playerCharacter.roomY = playerCharacter.roomY - 1
        #updates description text box
        txt_description.delete("1.0", tk.END)
        txt_description.insert(tk.INSERT, roomDescArry[playerCharacter.roomX][playerCharacter.roomY] + "\nTo the north you see:\n" + roomDescArryN[playerCharacter.roomX][playerCharacter.roomY] + "\nTo the east you see:\n" + roomDescArryE[playerCharacter.roomX][playerCharacter.roomY]+ "\nTo the south you see:\n" + roomDescArryS[playerCharacter.roomX][playerCharacter.roomY]+ "\nTo the west you see:\n" + roomDescArryW[playerCharacter.roomX][playerCharacter.roomY])
    #adds player icon
    mapArrayIcons[playerCharacter.roomX][playerCharacter.roomY] = playerCharacter.mapIcon
    #updates map 
    for row in mapArrayIcons:
        map.insert(tk.INSERT, "\n")
        for col in row:
            map.insert(tk.INSERT, col)
    #Locks Map
    map.configure(state='disabled')
    #check if bartender is present and start conversation.
    submitAI()

window = tk.Tk()
window.title("Text AI Game GUI")
window.configure(bg='Light Grey')


#conversation = top text field
#description = middle text field
#edit = lower text field
txt_conversation = tk.Text(window, height = 25, width = 100)
#.configure(wrap=WORD) enables word wrap had to include function at top.

txt_conversation.configure(wrap=WORD)
txt_description = tk.Text(window, height = 8, width = 100)
txt_description.configure(wrap=WORD)
txt_edit = tk.Text(window, height =3, width = 100)

txt_edit.configure(wrap=WORD)



#initilise room description
txt_description.insert(tk.INSERT, roomDescArry[playerCharacter.roomX][playerCharacter.roomY] + "\nTo the north you see:\n" + roomDescArryN[playerCharacter.roomX][playerCharacter.roomY] + "\nTo the east you see:\n" + roomDescArryE[playerCharacter.roomX][playerCharacter.roomY]+ "\nTo the south you see:\n" + roomDescArryS[playerCharacter.roomX][playerCharacter.roomY]+ "\nTo the west you see:\n" + roomDescArryW[playerCharacter.roomX][playerCharacter.roomY])

#Map is a textbox
map = tk.Text(window, height = 6, width = 5, font=("Wingdings", 32))
#Initilize Map
mapArrayIcons = [[room00.roomIcon, room01.roomIcon, room02.roomIcon, room03.roomIcon, room04.roomIcon],[room10.roomIcon, room11.roomIcon, room12.roomIcon, room13.roomIcon, room14.roomIcon],[room20.roomIcon, room21.roomIcon, room22.roomIcon, room23.roomIcon, room24.roomIcon],[room30.roomIcon, room31.roomIcon, room32.roomIcon, room33.roomIcon, room34.roomIcon],[room40.roomIcon, room41.roomIcon, room42.roomIcon, room43.roomIcon, room44.roomIcon]]
#initilize Bartender on Map
mapArrayIcons[bartender.roomX][bartender.roomY] = bartender.mapIcon
#initilize wizard on map
mapArrayIcons[oldWizard.roomX][oldWizard.roomY] = oldWizard.mapIcon
#initilize Player on Map
mapArrayIcons[playerCharacter.roomX][playerCharacter.roomY] = playerCharacter.mapIcon
#prints initial map 
for row in mapArrayIcons:
    map.insert(tk.INSERT, "\n")
    for col in row:
        map.insert(tk.INSERT, col)
#Locks Map
map.configure(state='disabled')

#function for moving north. Is applied to btn_north



#Button details
fr_buttons = tk.Frame(window, background="Grey", relief=tk.RAISED, bd=2)
fr_buttons2 = tk.Frame(window, background="Brown", relief=tk.RAISED, bd=2, pady=10)
fr_buttons3 = tk.Frame(window, background="Grey", relief=tk.RAISED, bd=2)

#Button creation and names
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_resubmit = tk.Button(fr_buttons3, text="Resubmit", command=reSubmit)
btn_submit = tk.Button(fr_buttons3, text="Submit Text", command=submitAI)

#Cardinal buttons
btn_north = tk.Button(fr_buttons2, text="\N{UPWARDS BLACK ARROW}", command=move_N)
btn_south = tk.Button(fr_buttons2, text="\N{DOWNWARDS BLACK ARROW}", command=move_S)
btn_east = tk.Button(fr_buttons2, text="\N{RIGHTWARDS BLACK ARROW}", command=move_E)
btn_west = tk.Button(fr_buttons2, text="\N{LEFTWARDS BLACK ARROW}", command=move_W)

#Grid placement for buttons, text and map
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

btn_resubmit.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_submit.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

btn_north.grid(row=2, column=2, sticky="ew", padx=5, pady=5)
btn_south.grid(row=4, column=2, sticky="ew", padx=5, pady=5)
btn_east.grid(row=3, column=3, sticky="ew", padx=5, pady=5)
btn_west.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=1, sticky="ns")
fr_buttons2.grid(row=2, column=2, sticky="ns")
fr_buttons3.grid(row=4, column=1, stick="ns")

txt_conversation.grid(row=1, column=1, sticky="nsew")
txt_description.grid(row=2, column=1, sticky="nsew")
txt_edit.grid(row=3, column=1, sticky="nsew")
map.grid(row=1, column=2, sticky="nsew")




window.mainloop()


