## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define Saber = Character('Saber')
define Gilgamesh = Character('Gilgamesh')
define Archer = Character('Archer')
## The game starts here.

init:
    image bg ROOT = "images/BG/bg_ROOT.png"
    image SaberNorm = "images/Saber/SaberCasual01aMAIN.png"
    image SaberSmiles = "images/Saber/SaberCasual01b2MAIN.png"
    image SaberAnnoyed = "images/Saber/SaberCasual01aAnnoyedMAIN.png"
    image SaberAngry = "images/Saber/SaberCasual10dBlushingMAIN.png"
    image SaberPISSED = "images/Saber/SaberCasual10dCLOSE.png"
    image nuke = "images/BG/Nuke.jpg"
    image GilgameshSmirk = "images/Gilgamesh/GilgameshArmored02a(CLOSE).png"
    image GilgameshAngry = "images/Gilgamesh/GilgameshArmored04a(CLOSE).png"
    image Hawaii = "images/BG/HAWAII.jpg"
label start:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene bg ROOT

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    show SaberNorm

    ## These display lines of dialogue.

    Saber "Hello, good citizens of Hawaii."

    hide SaberNorm

    show SaberSmiles

    Saber "I am Arturia Pendragon, the former King of Britain!"

    hide SaberSmiles

    show SaberNorm

    "Silence..."

    hide SaberNorm

    show SaberAnnoyed

    Saber "What? Just because I'm a girl doesn't mean that I can't be a king!"

    "More silence..."

    hide SaberAnnoyed

    show SaberAngry

    Saber "You people are rude!" 

    hide SaberAngry

    show SaberPISSED

    Saber "{b}YOU CAN ALL GO F*** YOUR SELVES IN HELL!!!{/b}"  
    
    scene nuke
    
    "*BOOOOOOOOOOOMMMMM*"

    "Some time later..."

    scene Hawaii
    with dissolve

    show SaberSmiles at left

    Saber "Ahem, I apologize for my breakdown. I have been so stressed out this past week that my nerves were frayed to high hell"

    Saber "Now where was I... oh yes, I am the rightful king of the English Isles"

    Saber "I was summoned in both the fourth and the fifth Heaven's Feel rituals as a Saber-class servant, which I may add is one of the most powerful servant class in the wars. How else did I manage to reach the Holy Grail twice."

    Saber "My master in the fourth Holy Grail war was an assassin named Kiritsugu Emiya"

    show SaberAnnoyed at left

    Saber "He was a cold and ruthless man who had no qualms in involving innocent people in his assassinations if it meant a near-certain chance of success"

    Saber "He was also very unfaithful and was willing to tell lies and deceptions to get his goals"

    Saber "I never liked him much. I think he would have been better off with an assassin-class servant instead of me"

    "Saber clears her throat"

    Saber "Now as for my master in the fifth war-"

    "*CRASH*"

    "Someone just barged through the studio wall!"

    Saber "Wha-"

    Gilgamesh "Muwahahahahaha! Did you really think that you could hide from me, the one true king, my dear Saber?"

    "A brash and arrogant voice cut through the air as the dust settled to reveal-"

    show GilgameshSmirk at right

    Gilgamesh "From I, Gilgamesh, the King of all Heroes?"

    "-Gilgamesh, the King of A-Holes, who is an arrogant piece of crap"

    hide GilgameshSmirk

    show GilgameshAngry

    Gilgamesh "...why you INSOLENT-"

    "Shut up, Gil, and kindly see yourself out the door"

    Gilgamesh "...fine..."

    hide GilgameshAngry

    "And he walks out the door"

    ## This ends the game.

    return
