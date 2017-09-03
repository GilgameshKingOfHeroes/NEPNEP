## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define Unknown = Character('Unknown')
define Minato = Character('Minato')
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
    image MinatoUniform = im.Scale("images/Minato/MinatoProfile.png", 470, 470)
label start:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene bg ROOT

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    ## These display lines of dialogue.

    show MinatoUniform

    Minato "Hmm? Am I dead?"

    Minato "It looks like it, but it doesn't feel like it"

    Minato "..."

    Minato "...weird"

    Minato "So, if I am dead..."

    Minato "...where am I?"

    "Hmm? I never expected to see someone here as well"

    Minato "Huh? who's there?"

    "A beautiful woman clad in armor appeared before my eyes"

    hide MinatoUniform

    show MinatoUniform at right

    show SaberNorm at left

    Unknown "Welcome, young man, to the root of the world"

    Minato "Huh. I was sort of expecting you to say 'Welcome to the Velvet Room'"

    Unknown "Hmm? What's this 'Velvet Room' you speak of?"

    Minato "Nevermind. Anyways, I don't you and you don't know me so why don't we introduce ourselves?"

    Unknown "Very well, but why don't you introduce yourself first since you were the one who suggested it first?"

menu:

    "Fair enough. My name is Minato Arisato":
        jump intro

    "Nah, I'm good. Ladies first, after all":
        jump ERROR

label ERROR:
    
    "..."

    "..."

    "...the woman slowly starts to shake, from what I don't know."

    Minato "Umm... miss...?"

    "She then lifted her head, her bangs shadowing her face and her VERY much annoyed expression."

    Saber "Excuse me, but... did you just assume that I was a lady..."

    Minato "Umm... that's what you-"

    hide SaberNorm

    show SaberPISSED at left

    Saber "I AM NOT A LADY!!! I AM A DRRRRRRAAAAAAAAAAGGGGGGGGGGGOOOOOOOOOOOOOOOOONNNNNNNNNNNNNNN!!!!!!!!!!!!!!!!"

    scene nuke

    play sound "bomb.wav"

    "*BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMMMMMMMMMMMMMMMMMMMM*"

    return

label intro:

    Unknown "Minato Arisato... an interesting name"

    Saber "I am the 'Servant of the Sword', but you may call me Saber for short. It is a pleasure to make your acquaintance, Mister Arisato"

    Minato "'A pleasure to make your acquaintance'? You sound like one of the people I used to know..."

    "Saber looked confused at my statement but quickly regained her stoic expression"

    Saber "Ah, did I accidentally bring up painful memories? My apologies, Mister Arisato"

    Minato "No no no, you did nothing wrong. I was just stating one of my observations. So, mind telling me where exactly am I?"

    Saber "That... is a complicated issue."

    "Complicated?"

    Minato "Could you please elaborate?"

    Saber "This place exists outside the realms of time and space, where dimensions and universes intersects and moves away at the same time. It is hard to explain. Think of this as a sort of... train stations for all of the dimensions and universes."

    "..."

    "......"

    "......what?"

    "After the whole 'Velvet Room' and facing off against Nyx this shouldn't really suprise me, but..."

    Minato "Are you saying that my soul somehow transcended past the bonds of my universe into this place?"

    hide SaberNorm

    show SaberSmiles at left

    Saber "In a word..."

    Saber "Yes."

    "Well now."

    Minato "So, what is my fate now? Am I cursed to wander aimlessly through this place, never to be reincarnated?"

    Saber "No. Since this is the root of the world, you've essentially achieved what thousands of others have sacrificed years of the time to achieve. You've probably attained a True Magic at this point."

    "True Magic?"

    Minato "What is this 'True Magic' you are talking about? And what do you mean that others have sacrificed years of their time to try to achieve what I've done?"

    "Saber looked confused"

    hide SaberSmiles

    show SaberNorm at left

    Saber "Was that not your intention? You are a magus, are you not?"

    Minato "No, reaching the 'root' as you call it was not my intention at all, and last I checked, I was not a magus or whatever they are"

    Saber "I see. So you must've done something of signifigance that opened up a path to the root by itself. Pray tell what deed have you done that might've warranted such an event?"

    Minato "Would sealing the Greek Primordial Goddess of the Night away into my body count as one?"

    "Saber's eyes widened and her jaw had dropped"

    hide SaberNorm

    show SaberPISSED at left

    Saber "SEALING  AWAY A GODDESS IN YOUR BODY!? ARE YOU MAD, BOY!?"

    "I did not know how to react to her sudden explosion except to just stare at her blankly and keep my stoic face up."

    Saber "What kind of idiocy justified sealing away a Primordial into your own body!? What could possibly warrant such a event as large as this!?" 

    Minato "The world was about to end, my friends were about to die, and I still didn't get to eat all the sweetrolls I ever wanted, so I decided to sacrifice myself for 'The Greater Good' or something like that."

    hide SaberPISSED

    show SaberNorm at left

    Saber "I see. So it was a dire situation that forced your hand."

    Saber "By the way, why do you seem to have the same facial expression and body posture all this time? Are you stuck that way or what?"

    Minato "Blame it on the lazy artists who drew me and the lazy-ass dev who decided to put me into this game."

    Saber "What?"

    Minato "Nevermind."

    Saber "In any case, because you reached akasha, you've gained a true magic that you can use at your disposal, which happens to be the Denial of Nothing-"

    Minato "Wait, before you go on to tell me what the name of my power is, could you explain to me what a true magic is?"

    Saber "A true magic is a power that allows for the impossible to happen. Normal magic only allows for the recreation of known miracles like setting something on fire. However someone could accomplish the same thing with a match or lighter."

    Saber "True magic allows for miracles that cannot be recreated with science like creating something from nothing. That is the nature of your power."

    "I looked at my seemingly glowing hands and wondered about what my gaining this power mean for me. Does that mean that I will embark on another adventure? To once more know friendship and sacrifice."

    Saber "If you are wondering if this means that your journey is not over, then yes, it is not over."

    "I turned to Saber, my expression like that of a guy who just got told that his hundred-million yen lottery ticket was actually a prank."

    Minato "...why? I just sacrificed myself for the entirety of humanity. My fate is that of a seal to forever keep erebus at bay. What can I offer that justifies me leaving the seal?"

    Saber "If you are worried about the state of your seal, then fear not."

    return

    ## This ends the game.

    return
