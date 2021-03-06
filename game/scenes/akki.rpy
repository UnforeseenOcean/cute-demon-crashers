#--CG variations variables init--------
# You can probably manage these better :'D 
define ak_bottom = "on"
define cl_bottom = "on"
define cl_arm = "down"
define cl_top = "on"
define ak_arm = "down"
define ac_heads = "kiss"
define ak_face = None
define cl_face = None
define lay_cface = "1"
define lay_aface = "1"
define cuddle_aface = "3"
define cuddle_cface = "3"
define akki_epilong = False


label akki_hangout1:
    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    $renpy.pause(0.4)
    play music music_akki
    scene bg living_room with dissolve
    $akki.set_state(**Emotion.normal())
    $claire.set_state(**Emotion.normal())

    
    "I spot Akki fervently steering a peripheral wheel. I take a seat on the couch, wondering how to start a conversation."
    show akki at center_alone2 with dissolve
    if current_day == 1:
        voice "a_w16"
        ak "Feel better?"
        $ claire.set_state(with_dissolve ,eyes="happy", eyebrows="default", emotion="sweat", emotion_base="blush", mouth="smile")
        cl "Huh? Oh yes. Sorry about the sobfest."
        $akki.set_state(with_dissolve, eyes="default", eyebrows="tender", mouth="low")
        ak "Don't worry about it... Mirari tends to jump into things head first. Sorry if we scared you." 
    else:
        $claire.set_state(eyes="default", eyebrows="up", mouth="uh")
        cl "I didn't know incubi played video games."
        voice "a_s12"
        ak "Kael sometimes brings back consoles. They're all these old ones though, but I know this series at least."
    $akki.set_state(with_dissolve, emotion="lll", eyes="flat", eyebrows="frown", mouth="ehh", emotion_base="dark")
    voice "a_s08"    
    ak "Ugh, fourth place..."
    $akki.set_state(with_dissolve, emotion="flowers", eyes="happy", eyebrows="default", mouth="smile", emotion_base="default")    
    voice "a_w17"
    ak "Wanna play together?"
    $ claire.set_state(with_dissolve ,eyes="happy", eyebrows="default", emotion="flowers", emotion_base="default", mouth="smile")
    cl "Sure."
    play sound "assets/sfx/race_start.ogg"
    
    "I pick up a second controller and, after selecting a few options, the race begins. Familiar with the game, I already get a speed boost at the starting line and reach first place." 
    $akki.set_state(with_dissolve, emotion="default", eyes="default", eyebrows="up", mouth="oh")    
    voice "a_w18"
    ak "Wow, you're good. Also, do you know why Mirari summoned us here in the first place? She practically teleported us here with nary an explanation besides 'there's someone we can help!'" 
    $ claire.set_state(with_dissolve ,eyes="tender side", eyebrows="inwards", emotion="default", emotion_base="default", mouth="oh")
    $akki.set_state(with_dissolve, emotion="default", eyes="default", eyebrows="up", mouth="low")    
    cl "How thoughtful... I guess I was being mopey over spring break - usually that's a time where people go on vacations or hang out with friends." 
    $ claire.set_state(with_dissolve ,eyes="down", eyebrows="inwards", emotion="lll", mouth="wavy")
    cl "However, most of my friends are busy, and a lot of them are dating or in a relationship."
    $ claire.set_state(with_dissolve ,eyes="closed", eyebrows="inwards", emotion="sweat", mouth="low")
    cl "I thought it'd be nice to have a fling of my own, but I need to know the person first, and I definitely can't do one-night stands. I wouldn't feel comfortable. I never had a boyfriend either."
    $ claire.set_state(with_dissolve ,eyes="tender side", eyebrows="inwards", emotion="default", mouth="wavy", emotion_base="small blush")
    cl "It doesn't help I'm already on the shy side... and a virgin."
    $akki.set_state(with_dissolve, eyes="mortified", eyebrows="inwards", mouth="tiny", emotion_base="no nose") 
    $ claire.set_state(eyes="default", eyebrows="default", emotion="default", mouth="oh" ,emotion_base="default", )
    cl "Was it true when they said you were inexperienced, too?"   
    show akki at bounce_right
    play sound "assets/sfx/screeches.ogg"
    voice "a_s12"
    $akki.set_state(with_dissolve, emotion="sweat", eyes="happy", eyebrows="inwards", mouth="fun grin", emotion_base="default") 
    "Akki's avatar zooms right off a cliff, and he sheepishly laughs."
    $akki.set_state(with_dissolve, emotion="sweat", eyes="closed", eyebrows="default", mouth="oh") 
    voice "a_s13"
    ak "Uh, yeah. Incubi usually don't feel insecure when it comes to sex since it's our food, but there's thousands of years of reputation built up to our name." 
    $akki.set_state(with_dissolve, emotion="default", eyes="tender side", eyebrows="up", mouth="wavy") 
    ak "What have you heard of incubi?" 
    $ claire.set_state(eyes="dots", eyebrows="default", mouth="ehh")
    cl "Hm... That they don't exist?"
    $akki.set_state(with_dissolve, emotion="default", eyes="wink", eyebrows="frown", mouth="happy") 
    voice "a_w20"
    ak "False. One's gaming in your living room right now."
    $ claire.set_state(eyes="happy", eyebrows="frown", mouth="smile")
    cl "And in last place." 
    $akki.set_state(with_dissolve, eyes="flat", eyebrows="frown", mouth="low") 
    voice "a_s19"
    ak "The AI are dirty cheaters. What else?"
    $ claire.set_state(eyes="default", eyebrows="default", mouth="uh")
    cl "That you're practically carnal demons who give mind-blowing sex? Phenomenal sex gods?"
    $akki.set_state(mouth="tiny", emotion="sweat")
    show akki at bounce_down_alone2
    ak "..."
    $ claire.set_state(eyes="happy", eyebrows="default", mouth="wavy", emotion="sweat")
    cl "Sounds like you have pretty big shoes to fill."
    $akki.set_state(with_dissolve, eyes="tender side", eyebrows="default", mouth="tiny") 
    voice "a_s13"
    ak "Even if we're not as well-known in your world anymore, the expectations are still there."
    $ claire.set_state(eyes="default", eyebrows="default", mouth="uh")
    cl "If you need sexual energy to live... then...?"
    $akki.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="ah", emotion_base="default", emotion="default") 
    voice "a_w21"
    ak "It's because I'm still young. We're all born with an energy reserve until we're old enough to nourish ourselves." 
    $akki.set_state(with_dissolve, eyes="tender side", eyebrows="default", mouth="tiny") 
    ak "I'm getting to that age... but I still have time left." 
    $ claire.set_state(eyes="happy", eyebrows="inwards", mouth="smile")
    cl "I guess we both have our share of insecurities." 
    $ claire.set_state(with_dissolve, eyes="tender", emotion="default")
    cl "It's kinda comforting to know, in a way."
    $akki.set_state(with_dissolve, eyes="default", eyebrows="tender", mouth="smile") 
    voice "a_s11"
    ak "I don't mind. We'll be hanging out for a bit, so might as well be honest with each other, even if it's a little embarrassing."
    play sound "assets/sfx/rev_up.ogg"
    "His avatar – which had steadily climbed higher in the rankings - approaches mine, but I break away to the front as we race around a sharp corner." 
    $ claire.set_state(eyes="fun front", eyebrows="default", mouth="kitty")
    cl "Since you've been so open, I'll reveal something very personal."
    $akki.set_state(with_dissolve, eyes="default", eyebrows="one up", mouth="oh") 
    voice "a_s21"
    ak "Oh?"
    $ claire.set_state(eyes="default", mouth="smile")
    cl "If you hold down R at a curve, you'll drift and gain speed."
    $akki.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="ah", emotion="bars") 
    voice "a_w13"
    ak "Really— Hey, that works!"
    $akki.set_state(with_dissolve, eyes="fun front", eyebrows="one up", mouth="grin", emotion="default") 
    voice "a_s06"
    ak "You shouldn't have told me that; now I'll beat you."
    $ claire.set_state(eyebrows="frown", mouth="happy", emotion="flowers")
    stop music fadeout 3
    cl "I like a challenge."
    jump next_day



label akki_hangout2:
    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    $renpy.pause(0.4)
    play music music_akki
    scene bg living_room with dissolve
    $akki.set_state(**Emotion.normal())
    $claire.set_state(**Emotion.normal())

    $akki.set_state(eyes="default", eyebrows="one up", mouth="oh", emotion="default")
    show akki at center_alone2 with dissolve
    show akki at bounce_up_alone2
    voice "a_w12"
    ak "Hey, [claire_name], is it true pizza is better than sex?"
    $ claire.set_state(eyebrows="up", eyes="dots", mouth="oh", emotion="sweat")
    cl "Huh? What brought that up?"
    $akki.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="neutral")
    ak "I was flicking through the channels and saw a scene where someone stated it was better than sex."
    $akki.set_state(with_dissolve, eyes="tender side", eyebrows="default", mouth="low")
    voice "a_s13"
    ak "I've seen some of those pizza commercials too, but I've never tried it..." 
    $ claire.set_state(eyebrows="default", eyes="default", mouth="happy", emotion="flowers")
    cl "If you'd like, I could order one."
    $akki.set_state(eyes="starry", eyebrows="up", mouth="happy", emotion="flowers")
    show akki at bounce_up_alone2
    voice "a_w22"
    ak "You will!?"
    $ claire.set_state(emotion="sweat", eyes="happy")
    cl "Of course, give me a minute."
    "After counting the allowance my parents left me, I call the first search result on my phone. I never tried their pizza before, but they are the closest, so..." 
    $akki.set_state(with_dissolve, eyes="happy", eyebrows="default", mouth="happy", emotion="note")
    "I'll spare Akki the agony of picking from a menu and order a large half cheese, half pepperoni pizza. He's pacing the room in excitement as I explain how the whole delivery thing works."
    $akki.set_state(with_dissolve, eyes="starry", emotion="starry", mouth="uh", eyebrows="up")
    voice "a_w23"
    ak "So, this pizza will magically appear once you hear a knock at the door?"
    $ claire.set_state(eyebrows="inwards", eyes="happy", mouth="wavy", emotion="sweat")
    cl "Um, something like that. However, you have to be out of sight because it only shows itself to humans."
    $akki.set_state(with_dissolve, emotion="default", mouth="drool")
    voice "a_s05"
    ak "I'll still get to eat it, right?"
    $ claire.set_state(eyebrows="default", eyes="default", mouth="smile", emotion="default")
    cl "Don't worry, you'll even get the first slice."
    cl "Now hide."
    hide akki with moveoutright
    "I playfully push him toward the kitchen. Crisis averted!"
    play sound "assets/sfx/knock.ogg"
    "On cue, I hear a knock and praise its speedy delivery. I glance back to see if Akki's gone, then open the door."
    "Delivery Boy" "Hi, here's your large pizza: half cheese, half pepperoni. The total comes to 15.74..."
    show item pizza at chibi_scene with dissolve
    "I place the pizza on the living room table and return with the cash." 
    $ claire.set_state(eyebrows="default", eyes="happy", mouth="grin")
    cl "Right, here's..."
    $akki.set_state(emotion="bars", eyes="default", mouth="uh")
    hide item with dissolve
    show akki at mright4 with moveinright
    voice "a_w24"
    ak "Did the pizza arrive?"
    $ claire.set_state(eyebrows="up", eyes="dots", mouth="low")
    cl "..."
    "Delivery Boy" "..."
    $akki.set_state(eyes="wide", eyebrows="up", mouth="ah", emotion="default")
    $ claire.set_state(eyebrows="up", eyes="shock", mouth="fun ah2", emotion_base="dark")
    cl "KEEPTHECHANGEKTHXBYE."
    "I hurl the bills at the poor guy and slam the door, my hands still on the handle to keep it shut."
    $akki.set_state(eyes="bugteary", eyebrows="inwards", mouth="wah", emotion="panic")
    show akki at center_alone2 with dissolve
    voice "a_w25"
    ak "Did it vanish because I stopped hiding?"
    $ claire.set_state(eyebrows="default", eyes="flat", mouth="wavy", emotion_base="default", emotion="sweat lots")
    cl "No, pizza's here." 
    $akki.set_state(with_dissolve, eyes="happy", eyebrows="default", mouth="happy", emotion="flowers")
    "I point to the table, and we both sit down on the couch. He digs in, completely oblivious to the situation that happened earlier. I grab a cheese slice, trying to shake off the embarrassment." 
    $ claire.set_state(eyebrows="up", eyes="default", mouth="oh", emotion_base="default", emotion="flowers")
    cl "(Hey, this pizza is really good... Like really good.)"
    $ claire.set_state(with_dissolve, eyebrows="inwards", eyes="semi open", mouth="wavy", emotion="sigh")
    cl "(And now I can never order from them again...)"
    $akki.set_state(eyes="default", eyebrows="one up", mouth="oh", emotion="default")
    show akki at sway
    voice "a_s17"
    ak "Um..."
    $ claire.set_state(eyebrows="default", eyes="mortified", mouth="lip bite", emotion="default")
    cl "(I doubt the same delivery guy will return, but I know he'll tell everyone at the pizza place about this.)" 
    $akki.set_state(eyes="closed", eyebrows="default", mouth="wavy", emotion="lll")
    show akki at sway
    voice "a_s03"
    ak "The cheese is dripping off your..."
    $ claire.set_state(eyes="closed", mouth="low", emotion="default")
    cl "(Maybe the next time I can say, 'haha, the pizza was for a costume party'. {i}Some{/i} costume party...)"
    $akki.set_state(eyes="default", eyebrows="one up", mouth="drool", emotion="default")
    show akki at sway
    voice "a_s18"
    ak "Are you going to eat that?"
    $ claire.set_state(eyes="closed", mouth="ehh")
    cl "(It's not too late to change my na—)"
    $akki.set_state(eyes="happy", eyebrows="default", mouth="smile", emotion="heart")
    show akki at mright_alone2 with move
    $claire.set_state(with_dissolve, emotion="shock", eyes="shock", eyebrows="deep frown", mouth="fun ah")
    extend " Hey!"
    "Akki pulls away, a chunk of my pizza slice in his mouth." 
    $ claire.set_state(eyes="default", eyebrows="frown", mouth="uh", emotion="default")
    cl "I thought you demons were all about consent."
    $akki.set_state(eyes="fun front", eyebrows="one up", mouth="grin", emotion="default")
    voice "a_s06"
    ak "When it comes to sex, not food."
    $ claire.set_state(eyebrows="deep frown", mouth="kitty")
    cl "Well, fine."
    $akki.set_state(eyes="shock", eyebrows="up", mouth="fun ah", emotion="shock")
    show akki at center_alone2 with move
    voice "a_w14"
    ak "Hey!"
    "I snatch a pepperoni off his slice, and smugly chew on it." 
    $akki.set_state(with_dissolve, eyes="tender", eyebrows="frown", mouth="low", emotion="default")
    "We glare at each other before we burst out laughing."
    $ claire.set_state(eyebrows="default", eyes="happy", mouth="happy", emotion="flowers")
    voice "a_s22"
    $akki.set_state(with_dissolve, eyes="happy", eyebrows="default", mouth="happy", emotion="flowers")
    cl "So? Taste good? Better than sex?"
    $akki.set_state(with_dissolve, eyes="happy", eyebrows="inwards", mouth="wavy", emotion="sweat")
    voice "a_s14"
    ak "I'll have to get back to you on that last one."
    $akki.set_state(with_dissolve,eyes="default", eyebrows="default", mouth="smile", emotion="default")
    ak "But it tastes great! Thanks for treating me,  [claire_name]."
    $akki.set_state(with_dissolve, mouth="happy")
    ak "We should save the rest for later; I don't want to ruin my appetite before our next meal." 
    $claire.set_state(emotion="default", eyes="default")
    cl "I agree. I love Kael's cooking." 
    if current_day == 2:
        $akki.set_state(with_dissolve,eyes="bugteary", eyebrows="default", mouth="tiny", emotion="default")
        #akki =<
        ak "..."
        $ claire.set_state(eyebrows="default", eyes="default", mouth="smile", emotion="heart")
        cl "And yours, too."
        $akki.set_state(with_dissolve,eyes="default", eyebrows="default", mouth="grin", emotion_base="small blush")
        #akki >///< 
        ak "I try."
    stop music fadeout 1
    jump next_day
        

label akki_hangout3:

    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    $renpy.pause(0.4)
    play music music_akki
    $akki.set_state(**Emotion.normal())
    scene bg living_room with dissolve
    show akki at center_alone2 with dissolve
    $ claire.set_state(eyebrows="default", eyes="default", mouth="ehh", emotion="sweat")
    cl "I don't know about this."
    $akki.set_state(with_dissolve, eyes="default", eyebrows="frown", mouth="grin")
    voice "a_w26"
    ak "We can – seventh time's a charm."
    $ claire.set_state(eyebrows="default", eyes="closed", mouth="uhh", emotion="sigh")
    cl "Two minutes to kill 300 enemies, using only special attacks? Our magic meters replenish too slowly." 
    $akki.set_state(with_dissolve,eyes="clench", eyebrows="default", mouth="ah", emotion="panic")
    voice "a_s07"
    ak "We can do it. I wanna unlock the next stage already."
    $akki.set_state(with_dissolve,eyes="default", eyebrows="frown", mouth="low", emotion="default", emotion_base="default")
    "I shake my head, but shrug, and start slicing through waves and waves of goblin-like monsters. I love hack-and-slash games but these mission requirements are intense." 
    $akki.set_state(with_dissolve,eyes="default", eyebrows="frown", mouth="neutral", emotion="sweat")
    "Akki's really into it. His legs are bouncing and he's biting his lip in concentration. Despite our best attempts, there's only 30 seconds left and my magic meter is—"
    "Ah, a jar!"
    "I smash it open and lament that my meter replenished too late."
    $ claire.set_state(eyebrows="up", eyes="clench", mouth="wah", emotion="panic")
    cl "50 enemies left... but there's barely any around me!"
    $akki.set_state(with_dissolve,eyes="default", eyebrows="frown", mouth="oh", emotion="bars")
    voice "a_w27"
    ak "I have a plan. Run north."
    $ claire.set_state(eyebrows="up", eyes="dots", mouth="ehh", emotion="sweat")
    cl "Okay?"
    $akki.set_state(with_dissolve,emotion="default", eyebrows="default", mouth="smile")
    "My swordswoman runs through the gate, and I see Akki's brawler dart past me... with a swarm of enemies chasing him."
    $akki.set_state(with_dissolve,eyes="happy", eyebrows="up", mouth="ah", emotion="default")
    voice "a_w28"
    ak "Now, now!"
    $akki.set_state(with_dissolve,eyes="default", eyebrows="default", mouth="default", emotion="default")
    "With 10 seconds left, I activate the special attack and my character whirlwinds through the mob, effortlessly slaying them."
    $akki.set_state(with_dissolve,eyes="wide", eyebrows="up", mouth="ah", emotion="bars")
    "'Mission Complete!' appears on the screen, and I bounce on the couch and cheer."
    $ claire.set_state(eyebrows="default", eyes="clench", mouth="happy", emotion="note")
    $akki.set_state(with_dissolve,eyes="happy", eyebrows="up", mouth="grin", emotion="flowers")
    cl "We did it!"
    $akki.set_state(with_dissolve,eyes = "happy", mouth="happy", emotion="default")
    voice "a_w29"
    ak "Yes!"

    hide akki with dissolve
    show chibi_akki01 at chibi_scene with dissolve
    $ gallery.unlock("chibi_akki01")
    

    "In our triumph, we find ourselves hugging each other, my body pressing against his."
    stop music fadeout 2
    "Realizing what's going on, we separate and shuffle away, averting our gaze. My face still feels warm from the contact."
    hide chibi_akki01 with dissolve
    $ claire.set_state(eyes="down", eyebrows="default", mouth="wavy", emotion="default", emotion_base="small blush")
    $akki.set_state(eyes="wide", eyebrows="up", mouth="ah", emotion="panic")
    show akki at center_alone2 with dissolve
    cl "Um..."
    play music music_romance fadein 2
    $akki.set_state(with_dissolve,eyes="tender side", eyebrows="tender", mouth="wavy", emotion="sweat", emotion_base="small blush")
    voice "a_s16"
    ak "S-sorry, I got all excited there..." 
    $ claire.set_state(eyes="down", eyebrows="default", mouth="wavy", emotion="default", emotion_base="large blush")
    cl "I don't mind."
    $akki.set_state(with_dissolve,eyes="closed", eyebrows="tender", mouth="low", emotion="default")
    "We sit in silence while the results tally up."
    $akki.set_state(with_dissolve,eyes="tender side", eyebrows="tender", mouth="oh", emotion_base="large blush")
    voice "a_w30"
    ak "Then... is it okay if we sit a little closer?"
    $ claire.set_state(eyes="default", eyebrows="default", mouth="oh", emotion="default", emotion_base="large blush")
    cl "Sure."
    $akki.set_state(with_dissolve,eyes="tender", eyebrows="tender", mouth="smile", emotion_base="small blush")
    "I shuffle over until our thighs touch, and we both lean in. Hesitantly, Akki reaches around and places a hand on my shoulder."
    voice "a_s14"
    ak "Can I tell you something personal?"
    $ claire.set_state(eyes="happy", eyebrows="default", mouth="grin", emotion="default", emotion_base="small blush")
    cl "Is it a gaming tip?"
    $akki.set_state(with_dissolve,eyes="happy", eyebrows="default", mouth="grin", emotion_base="default", emotion="note")
    voice "a_s12"
    ak "I wish. I doubt I could give you a gaming tip you wouldn't know of, though." 
    $akki.set_state(with_dissolve,eyes="happy", eyebrows="default", mouth="smile", emotion_base="default", emotion="default")
    "He ruffles my hair and I giggle."
    $akki.set_state(with_dissolve,eyes="tender", eyebrows="tender", mouth="oh", emotion_base="small blush", emotion="default")
    voice "a_w31"
    ak "I... like cuddling."
    $akki.set_state(with_dissolve,eyes="tender side", eyebrows="tender", mouth="wavy", emotion_base="large blush", emotion="sweat")
    ak "Um, don't feel like you have to. It's just I've become comfortable with you and..."
    $akki.set_state(with_dissolve,eyes="wide", eyebrows="up", mouth="oh", emotion_base="large blush", emotion="default")
    "He trails off when I snuggle in closer. I can feel his body heat up against mine." 
    $akki.set_state(with_dissolve,eyes="happy", eyebrows="tender", mouth="smile", emotion_base="small blush")
    ak "And, er, by the off chance you pick me..."
    $akki.set_state(with_dissolve,eyes="default", eyebrows="tender", mouth="ah", emotion_base="small blush")
    voice "a_w32"
    ak "I know I'm inexperienced, and I don't know if I'd be any good... but I'd do my best to make you happy."
    $ claire.set_state(eyes="down", eyebrows="default", mouth="wavy", emotion="default", emotion_base="large blush")
    cl "Ah... thank you..."
    $akki.set_state(with_dissolve,eyes="default", eyebrows="one up", mouth="low", emotion_base="default")
    "While I struggle to come up with a better response, Akki taps the controller and frowns."
    $akki.set_state(with_dissolve,eyes="dots", eyebrows="up", mouth="oh")
    voice "a_w33"
    ak "Wait, where's the next stage?"
    $ claire.set_state(eyes="dots", eyebrows="up", mouth="oh", emotion="default", emotion_base="default")
    cl "Huh? We cleared all the requirements, there should be another one."
    $akki.set_state(with_dissolve,eyes="default", eyebrows="one up", mouth="uh")
    voice "a_s19"
    ak "Maybe we had to complete the level faster...?"
    $akki.set_state(with_dissolve,eyes="default", eyebrows="frown", mouth="low")
    "While he navigates through the menu, I decide to check the walkthrough on my phone. I see the description and groan loudly."
    $ claire.set_state(eyes="flat", eyebrows="default", mouth="ehh", emotion="lll", emotion_base="dark")
    cl "There is no next stage..."
    $akki.set_state(with_dissolve,eyes="wide", eyebrows="up", mouth="oh")
    voice "a_s02"
    ak "Huh?"
    $ claire.set_state(eyes="flat", eyebrows="default", mouth="wavy", emotion="default", emotion_base="dark")
    cl "Uh, we can't unlock them. Whether you clear the level or not, you have to buy the downloadable content." 
    $akki.set_state(with_dissolve,eyes="wide", eyebrows="up", mouth="tiny")
    ak "..."
    $ claire.set_state(eyes="flat", eyebrows="default", mouth="low", emotion="default", emotion_base="dark")
    cl "..."
    $akki.set_state(with_dissolve,eyes="shock", eyebrows="up", mouth="fun ah", emotion="shock")
    voice "a_s08"
    ak "That's evil. All this effort!"
    $ claire.set_state(eyes="clench", eyebrows="frown", mouth="wah", emotion="panic", emotion_base="default")
    cl "Hahaha, if we'd known sooner... all those attempts and spending money on better weapons!"
    $akki.set_state(with_dissolve,eyes="clench", eyebrows="default", mouth="ah", emotion="default")
    voice "a_s07"
    ak "Gah, I've had enough of this game."
    $akki.set_state(with_dissolve,eyes="happy", eyebrows="default", mouth="smile", emotion="heart")
    "He drops the controller on the table and pulls me toward him as he lies on his back."
    $akki.set_state(with_dissolve,eyes="default", eyebrows="tender", mouth="smile", emotion="default", emotion_base="small blush")
    voice "a_w34"
    ak "I'd much prefer this."
    "We giggle, and I let myself relax, resting my head on his chest. One hand rubs up and down my back."
    $akki.set_state(with_dissolve,eyes="happy", eyebrows="tender", mouth="smile", emotion="default", emotion_base="small blush")
    voice "a_s10"
    ak "...Really glad we crashed your spring break."
    $ claire.set_state(eyes="happy", eyebrows="tender", mouth="smile", emotion="flowers", emotion_base="small blush")
    cl "Same here."
    stop music fadeout 1
    jump next_day
    

label akki_sex:
    $ in_sex = True
    $renpy.choice_for_skipping()
    $akki.set_state(**Emotion.normal())
    $claire.set_state(**Emotion.normal())

    if _in_replay:
        $ sex_stop_label = "akki_stop_now"
        show screen replay_controls()
    
    if not _in_replay:
        $ persistent.akki_claire_name = claire_name
        $ persistent.akki_scenes = akki_scenes
        $ persistent.akki_sex_stop = None

    scene black with dissolve
    scene bg bedroom_night with dissolve
    voice "a_s13"
    ak "Now what?"
    show chibi_akki02 at chibi_scene with dissolve
    $ gallery.unlock("chibi_akki02")
    "We sit on the bed, none of us moving a muscle. For someone who burst into my bedroom, carrying me effortlessly, he's sure timid now."
    cla "Well, you're the incubus. Don't they have magical sex powers or something to get it started?"
    voice "a_s12"
    ak "That's called centuries of experience."
    cla "Ah..."
    ak "..."
    cla "..."
    voice "a_sex26"
    ak "Um... I may be new to this, but I'll do my best to be mindful and listen to your feedback."
    ak "I'll probably ask a lot of questions... and it's okay to stop at any time."
    if akki_scenes >= 3:
        voice "a_sex01"
        ak "I really care about you, [claire_name]. The last thing I want to do is make a mistake that hurts your trust."
        cla "T-thank you... You're sweet, Akki. You mean a lot to me, too."
    else:    
        cla "T-thank you... it means a lot to me." 
    hide chibi_akki02 with dissolve
        
    cla "(How should we go about this?)"
    $akki.set_state(emotion_base="small blush", mouth="low", eyebrows="tender")
    show akki at center_alone2 with dissolve
    menu:
        "Kiss him first.":
            $claire.set_state(emotion_base="small blush", eyebrows="inwards", mouth="smile", eyes="tender")
            cl "Here, we can take it slow."
            hide akki with dissolve
            show akki_kiss A with dissolve
            #$akki.set_state(with_dissolve, eyes="closed", mouth="neutral")
            "I lean in, watching him gauge my movements. Gently, I press my lips against his, barely making firm contact."
            #$akki.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="ah", emotion="flowers")
            "After pulling away, I can see his cheeks redden and he looks at me with wide-eyed astonishment."
            hide akki_kiss with dissolve
        
        "Suggest for him to kiss you.":
            $claire.set_state(emotion_base="small blush", eyebrows="inwards", mouth="smile", eyes="tender")
            cl "I suppose it starts with a kiss."
            $akki.set_state(with_dissolve, eyes="tender", mouth="neutral")
            ak "A kiss..."
            hide akki with dissolve
            show akki_kiss B with dissolve
            "His eyes drift to my lips, and he reaches out a hand. After a pause, he sees my affirmation, and he cups my cheek before leaning in." 
            #$akki.set_state(with_dissolve, eyes="closed")
            "He presses his lips against mine, and I'm surprised by how gentle it is." 
            #$akki.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="ah", emotion="flowers")
            "After he pulls away, we're both in awe."
            hide akki_kiss with dissolve

        "Let's not do this.":
            "I hold his hand and give it a comforting squeeze."
            $claire.set_state(emotion_base="small blush", eyebrows="inwards", mouth="smile")
            cl "You know... we don't have to go through with this. I can see you're just as nervous as I am."
            $akki.set_state(eyebrows="inwards", mouth="oh")
            voice "a_sex02"
            ak "You sure, [claire_name]?" 
            $claire.set_state(eyes="closed")
            cl "Honestly, yes. However, I enjoy being with you, and this closeness makes me happy enough."
            if akki_scenes >= 3:
                $claire.set_state(with_dissolve, eyes="tender side", mouth="uh")
                cl "You did mention you like cuddling, so..."
            $claire.set_state(with_dissolve, eyes="happy", mouth="smile", eyebrows="default")
            cl "We can cuddle tonight."
            $akki.set_state(eyebrows="tender", eyes="happy", mouth="default")
            stop music fadeout 2
            voice "a_sex03"
            ak "I'd like that."
            play music music_lullaby fadein 1
            $akki_cuddle_sprite.set_state(base="clothed")
            $ akki_cuddle_sprite.set_state(with_dissolve, akki=3, claire=3)
            scene akkicuddle with dissolve
            "He crawls over to me, and we both curl up on the bed. Once we're comfortable, he hugs me close, one hand stroking my hair."
            "I can feel his chest rise and fall, and his warm breath on my forehead. Soothed, I allow myself to drift into a restful sleep." 
            call credits from _call_credits_5
            jump akki_epilogue

    $ akki_sex_choices.kissing = True    
    $akki.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="ah")
    show akki at center_alone2 with dissolve
    $akki.set_state(with_dissolve, emotion="default", eyebrows="inwards", mouth="neutral", eyes="closed")
    "We exchange a smile then kiss again, this time deeper. I close my eyes, and I can feel his hand slide from my shoulder and trail down my arm, leaving goosebumps in its wake."
    stop music fadeout 2
    voice "a_sex04"
    "I sharply inhale from the sensation, and Akki slightly parts his mouth, brushing his tongue against my lips. When I reciprocate, he slips his tongue inside, taking quick sweeping tastes."
    play music music_love fadein 3
    "At first the texture feels strange, but I warm up to it, and he takes everything slow, exploring my mouth tenderly before returning to a surface kiss."
    $ akki_sex_choices.kissing = False
    python:
        akki_foreplay.set_state(
            akki_bottom="on",
            claire_arm="down",
            claire_bottom="on",
            claire_top="on",
            akki_arm="down",
            heads="kiss",
            claire_face="none",
            akki_face="none"
        )    
    scene akkiforeplay start with dissolve
    scene akkiforeplay
    "Feeling warm, I remove my outer layer, breaking our kiss in the process. I hear an audible gulp and Akki shyly glances down then back to me."
    $ akki_foreplay.set_state(claire_face="smile", akki_face="D:")
    $ akki_foreplay.set_state(with_dissolve, heads="apart")
#    $ ac_heads = "apart"
#    $ cl_face = "smile"
#    $ ak_face = "D:"
    voice "a_s13"
    ak "Is it okay if I touch you there?"
    menu:
        "Sure.":
            $ akki_sex_choices.breasts = True
            show screen sex_stop("akki_stop_now")
            $ akki_foreplay.set_state(with_dissolve, heads="kiss", claire_face="none", akki_face="none", akki_arm="breast")
#            $ breasts = "True"
#            $ ac_heads = "kiss"
#            $ cl_face = None
#            $ ak_face = None
#            $ ak_arm = "breast"
            "I nod, and Akki resumes kissing me while his hands lightly travel down my front."
            "He takes his time, leaving an agonizing relish, and the faintest moan escapes me when he finally cups my breast."
            "His hand stays there, unmoving, as if unsure how to proceed, and awkwardly applies pressure like its a button."
            "A slight pain shoots through my chest when his fingers squeeze under my bra, and I cover his hand with mine."
            $ akki_foreplay.set_state(claire_face="smile", akki_face="nervous")
            $ akki_foreplay.set_state(with_dissolve, heads="apart")
#            $ ac_heads = "apart"
#            $ cl_face = "smile"
#            $ ak_face = "nervous"
            cla "Not so hard."
            voice "a_sex12"
            ak "Sorry... More like this?"
            $ akki_foreplay.set_state(with_dissolve, akki_face="D:")
#            $ ak_face = "D:"
            "He makes circular motions, and I hum in agreement. His thumbs start to swirl gingerly over my bra where my nipples are. It tingles ever so slightly from his touch."
            $ akki_foreplay.set_state(with_dissolve, claire_face="pleasure")
#            $ cl_face = "pleasure"
            cla "Much better." 

        "Only if I can do the same.":
            show screen sex_stop("akki_stop_now")
            $ akki_sex_choices.breasts = True
            $ akki_sex_choices.kissing = False
#            $ breasts = "True"
#            $ kissing = "False"

            $ akki_foreplay.set_state(with_dissolve, claire_face="smile")
#            $ cl_face = "smile"
            cla "Only if I can touch your chest, too."
            $ akki_foreplay.set_state(with_dissolve, akki_face="nervous")
#            $ ak_face = "nervous"
            voice "a_sex14"
            ak "... I wouldn't... mind..."
            $ akki_sex_choices.pectouch = True
            $ akki_foreplay.set_state(with_dissolve, akki_arm="down", claire_arm="chest")
#            $ak_arm = "down"
#            $cl_arm = "chest"
            "Comforted I'm not the only one nervous by this, I glide my hand up and down his muscular chest."
            $ akki_foreplay.set_state(with_dissolve, heads="kiss", claire_face="none", akki_face="none", akki_arm="breast")
#            $ ac_heads = "kiss"
#            $ cl_face = None
#            $ ak_face = None
#            $ ak_arm = "breast"
            "Between our kisses, my fingers find his nipples and I let my nails graze over them lightly. Akki's movements start to awkwardly mirror mine, as if taking cues that's how I want it too." 
            "I find the hollow of his chest, and slide a finger down his sternum. He quivers under my movements, then breaks off the kiss."
            $ akki_foreplay.set_state(claire_face="smile", akki_face="happy")
            $ akki_foreplay.set_state(with_dissolve, heads="apart")
#            $ ac_heads = "apart"
#            $ cl_face = "smile"
#            $ ak_face = "happy"
            voice "a_sex24"
            ak "That's surprisingly sensual... Is it the same for you?"
            "He mimics the same gestures. It's pleasant but it doesn't do anything for me."
            $ akki_foreplay.set_state(with_dissolve, claire_face="pleasure")
#            $ cl_face = "pleasure"
            cla "It feels nicer when you trail your fingers over my nipples."
            "He adjusts his approach, making circular motions over my breasts."
            
        "I'd like to stop now.":
            jump akki_early_stop

    scene akkiforeplay
    $ akki_foreplay.set_state(with_dissolve, claire_face="happy", akki_face="D:")
#    $ cl_face = "happy"
#    $ ak_face = "D:"
    voice "a_s13"
    ak "I apologize... this is your first time and I'm already fumbling..."
    cla "Aw, I don't mind. I can't expect you to know what I like, especially since I'm new to this, too." 
    "I lean in to kiss him on the lips, but his face aims higher, and we clumsily brush against each other before pulling away. We exchange a look then laugh."
    voice "a_s10"
    ak "Here..."
    $ akki_foreplay.set_state(with_dissolve, akki_face="happy")
#    $ ak_face = "happy"
    "He gives me a peck on the lips, his fingers lingering over the fabric of my top."
    voice "a_s13"
    ak "Would you like it more if I took off your shirt, too?"        
    menu:
        "Keep shirt on.":
            $ akki_sex_choices.top_off = False
            $ akki_foreplay.set_state(with_dissolve, claire_face="embarrassed")
#            $ cl_face = "embarrassed"
            cla "I'd like to leave it on. I'm still shy when it comes to my body..."
            ak "That's alright. I'll do my best to pleasure you like this."
            "He playfully kneads them then places a kiss between my breasts."

        "Take it off.":
            $ akki_sex_choices.top_off = True
            $ akki_foreplay.set_state(with_dissolve, claire_face="happy")
#            $cl_face = "happy"
            cla "Sure... It'd feel more equal like this."
            voice "a_s10"
            "We exchange a laugh. I lift up my arms and he nimbly pulls my shirt off."
            $ akki_foreplay.set_state(with_dissolve, claire_top="bra", akki_face="nervous", claire_arm="down", akki_arm="down")
#            $ cl_top = "bra"
#            $ ak_face = "nervous"
#            $ cl_arm = "down"
#            $ ak_arm = "down"
            "He stares at the bra contraption, then reaches around my back."
            $ akki_foreplay.set_state(with_dissolve, claire_face="happy")
#            $ cl_face = "happy"
            $ claire.set_state(base="bra")
            cla "It actually unclasps at the front."
            $ akki_foreplay.set_state(with_dissolve, akki_face="happy")
#            $ ak_face = "happy"
            voice "a_sex15"
            ak "Oh, that's convenient. Now I won't fumble because I can't see." 
            cla "Haha, unhooking different bras will be a useful skill to pick up."
            if akki_scenes >= 3:
                ak "Depends on how many styles you own."
                cla "Huh?"
                $ akki_foreplay.set_state(with_dissolve, akki_face="D:")
#                $ ak_face = "D:"
                voice "a_s13"
                ak "Um... is it okay if you're my first for longer...?"
                $ akki_foreplay.set_state(with_dissolve, claire_face="smile")
#                $cl_face = "smile"
                cla "Aw, Akki..."
            $ akki_foreplay.set_state(with_dissolve, claire_top="off", akki_face="nervous")
#            $ cl_top = "off"
            $ claire.set_state(base="naked")
#            $ ak_face = "nervous"
            "He removes the bra, releasing the constrains. For a second he gazes at me intently, then looks away, blushing."
            $ akki_foreplay.set_state(with_dissolve, claire_face="embarrassed")
#            $ cl_face = "embarrassed"
            cla "Um, do I look weird?"
            $ akki_foreplay.set_state(with_dissolve, akki_face="happy")
#            $ ak_face = "happy"
            voice "a_sex19"
            ak "No... You're beautiful, [claire_name]."
            $ akki_foreplay.set_state(with_dissolve, claire_face="smile")
#            $ cl_face = "smile"
            ak "I'm happy you're comfortable with me."
            $ akki_foreplay.set_state(with_dissolve, akki_arm="breast")
#            $ ak_arm = "breast"
            "He cups my breasts again, caressing each one equally. His thumbs resume their brushes over my nipples, which peak under his touch."
            if akki_sex_choices.pectouch:
                $ akki_foreplay.set_state(with_dissolve, claire_arm="chest")
#                $cl_arm = "chest"
                "I do the same in return, admiring his firm muscle under my hand."
                
        "I'd like to stop now.":    
            jump akki_early_stop

    $ akki_foreplay.set_state(with_dissolve, claire_face="pleasure")
#    $cl_face = "pleasure" 
    "My body stirs from the featherlight motions, and I feel heat radiate between my thighs. My heart races, and I subconsciously spread my knees out a little wider."
    $ akki_sex_choices.breasts = False
    $ akki_sex_choices.below_waits = True
    voice "a_sex16"
    ak "Such smooth skin..."
    $ akki_foreplay.set_state(claire_face="none", akki_face="none")
    $ akki_foreplay.set_state(with_dissolve, heads="kiss")
#    $ ac_heads = "kiss"
#    $ cl_face = None
#    $ ak_face = None
    "Akki notices, and he kisses me heavily as his hand meanders down my stomach and hips."
    "The multiple sensations are nearly overwhelming and I barely notice his fondling below until he explores my inner thighs."
    $ akki_sex_choices.below_waist = False
    $ akki_sex_choices.thighs = True
#    $ thighs = "True"
    "My stomach plunges and I feel something coil in my belly, desire swelling up in me."
    $ akki_foreplay.set_state(claire_face="smile", akki_face="happy")
    $ akki_foreplay.set_state(with_dissolve, heads="apart")
#    $ ac_heads = "apart"
#    $ cl_face = "smile"
#    $ ak_face = "happy"
    cla "A-Akki..."
    voice "a_sex17"
    ak "Does it feel good?"
    cla "It feels amazing."
    $ akki_foreplay.set_state(with_dissolve, akki_face="D:")
#    $ ak_face = "D:"
    voice "a_sex18"
    ak "Then...?"
    "His thumbs stroke the seams of my shorts, and I inhale deeply."  
    cla "You can continue."
    $ akki_foreplay.set_state(with_dissolve, akki_arm="finger", akki_face="happy")
#    $ak_arm = "finger"
#    $ ak_face = "happy"
    "At first he simply rubs over the shorts while his other hand cradles my back. Then he starts applying the pressure with two fingers, and the seams of my shorts push against my folds."
    $ akki_sex_choices.thighs = False
    $ akki_sex_choices.between_thighs = True
    $ akki_foreplay.set_state(with_dissolve, claire_face="pleasure")
#    $ cl_face = "pleasure"
    "Warmth spreads throughout my body, and I can feel my panties cling due to the increasing dampness."
    if akki_sex_choices.top_off:
        voice "a_s13"
        ak "Would you like it if we removed the rest of your clothes?"
    else:
        voice "a_s13"
        ak "Would you feel comfortable with your shorts off?"

    menu:
        "Yes.":
            $ akki_foreplay.set_state(with_dissolve, claire_face="embarrassed")
#            $ cl_face = "embarrassed"
            cla "I'd like to feel you directly."
            $ akki_foreplay.set_state(with_dissolve, akki_face="nervous")
#            $ ak_face = "nervous"
            ak "... I'll do my best."
            $ akki_sex_choices.naked_below = True
            $ akki_foreplay.set_state(with_dissolve, claire_arm="down", akki_arm="down")
#            $ cl_arm = "down"
#            $ ak_arm = "down"
            "I unzip my shorts and pull them down. Once they're off, I tug at the ends of my pantyhose, trying not to get the delicate fabric caught."
            "I can almost feel the seconds tick loudly."
            $ akki_foreplay.set_state(with_dissolve, akki_face="D:")
#            $ ak_face = "D:"
            voice "a_sex27"
            ak "That's... a lot of layers."
            cla "I-I wasn't prepared... or thought ahead..."
            $ akki_foreplay.set_state(with_dissolve, akki_face="happy", claire_face="happy")
#            $ ak_face = "happy"
#            $ cl_face = "happy"
            ak "It's alright, I can wait."
            cla "You didn't wait when you bridal carried me." 
            "I stretch and slingshot the leggings at him. He catches them, laughing, then tosses them aside."
            $ akki_foreplay.set_state(with_dissolve, claire_bottom="off")
#            $ cl_bottom = "off"
            "My hands slow down considerably while I carefully strip off my panties, and I suddenly feel a little colder. I hesitantly look back at Akki, unsure about his reaction."
            voice "a_sex28"
            ak "You're gorgeous."
            $ akki_foreplay.set_state(with_dissolve, claire_face="embarrassed")
#            $ cl_face = "embarrassed"
            "I blush when I realize I didn't, um, trim exactly down there. Akki was so excited earlier we skipped any chance to prepare ourselves..."
            cla "You mean it?"
            voice "a_sex06"
            ak "Of course. It's you."
            $ akki_foreplay.set_state(claire_face="none", akki_face="none")
            $ akki_foreplay.set_state(with_dissolve, heads="kiss", akki_arm="finger")
#            $ ac_heads = "kiss"
#            $ cl_face = None
#            $ ak_face = None
#            $ ak_arm = "finger"
            "His fingers tease the rim of my pubic hair, and he kisses me passionately again, familiar with how I love my kisses." 
            voice "a_sex29"
            ak "You're adorable..."
            "His fingers wander down, brushing my lower lips and my body responds to his touch."
            voice "a_sex30"
            ak "Um, wow, you're so wet..."
            "He presses against the cleft between my legs and continues stroking me with increased vigor."
            menu:
                "Touch him in return.":
                    $ akki_sex_choices.mutual_touching = True
                    $ akki_foreplay.set_state(claire_face="smile", akki_face="happy")
                    $ akki_foreplay.set_state(with_dissolve, heads="apart")
#                    $ ac_heads = "apart"
#                    $ cl_face = "smile"
#                    $ ak_face = "happy"
                    cla "I want to make you feel what I feel... Akki."
                    "My eyes drift to his hardness pressing against the fabric of his pants. He blushes, then covers it."
                    $ akki_foreplay.set_state(with_dissolve, akki_face="nervous")
#                    $ ak_face = "nervous"
                    voice "a_sex23"
                    ak "If it's okay with you... I thought the experience would be more about you?"
                    cla "It wouldn't feel right if it wasn't mutual."
                    $ akki_foreplay.set_state(with_dissolve, claire_arm="down", akki_arm="down")
#                    $ cl_arm = "down"
#                    $ ak_arm = "down"
                    voice "a_sex33" 
                    ak "That makes sense..."
                    "Oddly, he doesn't undo his belts, and instead inserts his thumbs under the leather."
                    cla "That's... rather convenient."
                    voice "a_sex34"
                    ak "Well, incubi... um... are supposed to be ready for anything..."
                    "I politely glance upward and realize he's blushing as much as I am."
                    $ akki_foreplay.set_state(with_dissolve, claire_arm="chest", akki_bottom="off", claire_face="surprised")
#                    $ cl_arm = "chest"
#                    $ ak_bottom = "off"
#                    $cl_face = "surprised"
                    "He tugs down the front of his pants, exposing his erection. The giddiness leaves my body and I'm unsure of how to react."
                    cla "..."
                    cla "...Impressive..."
                    ak "W-we're incubi ... we're supposed to be..."
                    "I reach out and stroke under his navel before descending, trailing my fingers through his hair. He deeply inhales in anticipation and I can sense the heat before I directly touch him."
                    "He twitches and I recoil."
                    cla "I-it moved."
                    voice "a_sex35"
                    ak "It's a natural reflex! I can't help it."
                    cla "H-huh... I don't remember this in any romance books..."
                    $ akki_foreplay.set_state(with_dissolve, claire_arm="handjob")
#                    $ cl_arm = "handjob"
                    "My face burns as I grip his shaft, wondering if I should observe to help perform better, or look away and focus on the sensation." 
                    "After I clumsily slide my hand up and down, Akki gently demonstrates."
                    $ akki_foreplay.set_state(with_dissolve, akki_face="happy")
#                    $ak_face = "happy"
                    ak "Here, I like it when there's a twisty motion..."
                    $ akki_foreplay.set_state(with_dissolve, akki_face="pleasure")
#                    $ ak_face = "pleasure"
                    "Using his hand, he mimics the action over his leg, and I dutifully replicate the request."
                    cla "Better?"
                    voice "a_sex36"
                    ak "Much."
                    $ akki_foreplay.set_state(with_dissolve, claire_face="embarrassed")
#                    $cl_face = "embarrassed"
                    cla "Now I'm the one who's fumbling..."
                    $ akki_foreplay.set_state(with_dissolve, akki_face="happy")
#                    $ak_face = "happy"
                    ak "No worries, take your time. You're doing great."
                    $ akki_foreplay.set_state(with_dissolve, akki_arm="finger", claire_face="pleasure", akki_face="pleasure")
#                    $ ak_arm = "finger"
#                    $ cl_face = "pleasure"
#                    $ ak_face = "pleasure"
                    "He resumes touching me again, his fingers stroking me deeply. I try to maintain the pace, but it's getting harder to concentrate from the increasing pleasure building inside of me."
                    "Occasionally Akki pauses and takes a breath before continuing and I realize we both feel the same way."
                    $ akki_foreplay.set_state(with_dissolve, akki_face="happy", claire_face="smile")
#                    $ak_face = "happy"
#                    $cl_face = "smile"
                    "Our eyes happen to meet, and it's obvious he's enjoying himself. We both accelerate our movements, wanting to share the same rhythm."
                    $ akki_foreplay.set_state(with_dissolve, claire_face="pleasure")
#                    $cl_face = "pleasure"
                "Enjoy the moment.":    
                    "The tickle I felt earlier spreads and I lean heavily against him, finding it hard to concentrate on anything beyond the sensation."
                    
                "I'd like to stop.":
                    jump akki_middle_stop

            cla "Ah... it feels so good.."
            if akki_sex_choices.mutual_touching == True:
                $ akki_foreplay.set_state(with_dissolve, claire_arm="down")
#                $cl_arm = "down"
                "My hands drop, unable to focus anymore."
            $ akki_foreplay.set_state(akki_face="happy", claire_face="pleasure")
            $ akki_foreplay.set_state(with_dissolve, heads="apart")
#            $ac_heads = "apart"
#            $ak_face = "happy"
#            $cl_face = "pleasure"
            hide screen sex_stop
            "He continues the motions, and my body arches against him."
            $ akki_foreplay.set_state(with_dissolve, claire_face="O")
#            $cl_face = "O"
            "My words are incomprehensible; I can only utter a soft groan. The core of my being vibrates and pressure that built up suddenly shoots down my legs and arms."
            "My breathing escalates until I sharply heave from one final wave of pleasure."
            $ akki_foreplay.set_state(with_dissolve, claire_face="pleasure", akki_arm="down")
#            $cl_face = "pleasure"
#            $ ak_arm = "down"
            "Akki holds me closely as my entire body shudders, followed by a floating sensation."
            "I feel I could melt in his arms and disappear..."
            "Akki shifts under me, then reaches for my hand, while the other brushes away my sweaty bangs."
            voice "a_sex31"
            ak "I felt it... Are you okay?"
            $ akki_foreplay.set_state(with_dissolve, claire_face="smile")
#            $cl_face = "smile"
            cla "I... wow, Akki. That was amazing, I never had anything like that by myself."
            voice "a_sex32"
            ak "I did a good job?"
            $ akki_foreplay.set_state(with_dissolve, claire_face="happy")
#            $cl_face = "happy"
            cla "Of course you did! I, hahaha..."
            show screen sex_stop("akki_stop_now")
            $ akki_foreplay.set_state(claire_face="none", akki_face="none")
            $ akki_foreplay.set_state(with_dissolve, heads="kiss")
            "Feeling giddy, I press my lips against him. My thighs feel sore and I'm fighting off exhaustion and yet I want to show him how amazing he is."
            
#            $ ac_heads = "kiss"
#            $ cl_face = None
#            $ ak_face = None

        "This is fine.":
            cla "I'm happy like this..."
            $ akki_foreplay.set_state(with_dissolve, heads="apart", akki_face="happy", claire_face="smile")
#            $ac_heads = "apart"
#            $ak_face = "happy"
#            $cl_face = "smile"
            $ akki_sex_choices.naked_below = False
            $ akki_foreplay.set_state(with_dissolve, akki_face="D:")
#            $ak_face = "D:"
            voice "a_sex20"
            ak "I can tell... Er, even through the fabric..."
            $ akki_foreplay.set_state(with_dissolve, claire_face="pleasure")
#            $cl_face = "pleasure"
            "He rubs deeply against the fabric, paying attention to my reactions. Whenever I wriggle sightly he repeats the motion with more vigor, and I can feel his fingers becoming moist against my shorts." 
            menu:
                "Touch him in return.":
                    $ akki_foreplay.set_state(with_dissolve, claire_face="smile")
#                    $cl_face = "smile"
                    cla "I want to make you feel what I feel... Akki."
                    "My eyes drift to his hardness pressing against the fabric of his pants. He blushes, then covers it."
                    $ akki_foreplay.set_state(with_dissolve, akki_face="nervous")
#                    $ak_face = "nervous"
                    ak "If it's okay with you... I thought the experience would be more about you?"
                    $ akki_foreplay.set_state(with_dissolve, claire_face="embarrassed")
#                    $cl_face = "embarrassed"
                    cla "It wouldn't feel right if it wasn't mutual. Um, this is my first time so..."
                    $ akki_foreplay.set_state(with_dissolve, akki_arm="down")
#                    $ ak_arm = "down"
                    "He widens his legs and I take it as a cue to reach in."
                    $ akki_foreplay.set_state(with_dissolve, claire_face="smile", akki_arm="down", claire_arm="crotch")
#                    $cl_face = "smile"
#                    $ak_arm = "down"
#                    $cl_arm = "crotch"
                    "Teasing, I stroke under his navel first before my fingers wriggle below his belts. He inhales deeply in anticipation, and my hand glides down to the stretched fabric."
                    $ akki_foreplay.set_state(with_dissolve, akki_face="pleasure")
#                    $ak_face = "pleasure"
                    "I can feel my face heat up as I grab his shaft. Maybe it's a good thing he's still covered..."
                    "After a few clumsy fondles, Akki places a hand inches above mine."
                    ak "I'll feel more here..."
                    "I nod, shift my fingers higher, and make twirling motions around his tip."
                    cla "Like this?"
                    voice "a_sex25"
                    ak "Uh-huh..."
                    $ akki_foreplay.set_state(with_dissolve, claire_face="pleasure", akki_arm="finger")
#                    $cl_face = "pleasure"
#                    $ak_arm = "finger"
                    "He closes his eyes briefly, then reaches out to resume touching me."
                
                "Enjoy the moment.":
                    "We resume kissing while he strokes me. I can feel pressure build inside me gradually, although there's only so much Akki can do with layers between us."
                
                "I'd like to stop now.":
                    jump akki_middle_stop
                
            
        "I'd like to stop now.":
            jump akki_middle_stop

    $ akki_foreplay.set_state(with_dissolve, heads="apart", claire_face="smile", akki_face="happy")
#    $ac_heads = "apart"
#    $cl_face = "smile"
#    $ak_face = "happy"   
    ak "Would you like it if we took it further...?"
    menu:
        "Yes.":
            hide screen sex_stop
            cla "Just take it slow..."
            ak "Of course."
            scene bg bedroom_night with dissolve
            $akki.set_state(eyes="tender", mouth="default", eyebrows="tender", emotion_base="small blush")
            show akki at center_alone2 with dissolve
            stop music fadeout 3
            "Wait, now that it's getting to that point..."
            
            menu:
                "Suggest a condom.":
                    $claire.set_state(eyes="default", eyebrows="up", mouth="uh", emotion_base="large blush")
                    cl "Before I forget... Is it okay if you put on a condom? There should be one in the drawer next to us..."
                    "He nods and reaches over to the nightstand. I'm glad I accepted those free packages they handed out at the university..."
                "It'll be fine.":
                    "I'm on the pill, so..."

            if akki_sex_choices.naked_below and not akki_sex_choices.top_off:
                "I raise my arms and Akki pulls my shirt off, tossing it aside."
                $akki.set_state(with_dissolve, base="naked")
            elif not akki_sex_choices.naked_below and akki_sex_choices.top_off:
                "I unzip my shorts and pull them down. Once they're off, I tug at the ends of my pantyhose, regretting all these layers that I decided to wear. Akki does the same, although fumbles with the belts in his rush."
                "My hands slow down considerably while I carefully strip off my panties, and I suddenly feel a little colder. I hesitantly look back at Akki, unsure about his reaction."              
                $akki.set_state(with_dissolve, base="naked", mouth="happy")
                ak "You look beautiful..."
            elif not akki_sex_choices.naked_below and akki_sex_choices.top_off:
                "I raise my arms and Akki pulls my shirt off, tossing it aside."
                "I unzip my shorts and pull them down. Once they're off, I tug at the ends of my pantyhose, regretting all these layers that I decided to wear. Akki does the same, although fumbles with the belts in his rush."
                "My hands slow down considerably while I carefully strip off my panties, and I suddenly feel a little colder. I hesitantly look back at Akki, unsure about his reaction."
                $akki.set_state(with_dissolve, base="naked", mouth="happy")
                ak "You look beautiful..."  

            play music music_romance fadein 2
            $akki.set_state(with_dissolve, base="naked")
            pause(0.3)
            $ akki_missionary_sprite.set_state(claire=1, akki=1)
            scene akki_missionary with dissolve  
            show screen sex_stop("akki_stop_now")
            "Gingerly, he lays me down on the bed, his body straddling mine with his elbows propped up beside me. He gently lowers himself until I can feel his heartbeat against my chest, his warm breath tickling my ear."
            $ akki_sex_choices.missionary = True
            $ claire.set_state(base="naked")
            voice "a_sex39"
            ak "I'm not too heavy?"
            cla "No, this is perfect."
            $ akki_missionary_sprite.set_state(with_dissolve, akki=2, claire=2)
#            $lay_aface = "2"
#            $lay_cface = "2"
            "I embrace him and he kisses me lightly, adjusting his position until his hardness presses against my thigh."
            "Moaning, I break from the kiss and hug him tighter, pushing my hips against him to close the distance. My fingers dig into him as he slides against me with long sensual strokes, causing me to shiver each time."
            "He adjusts his angle, nudging into me, causing me to gasp in surprise. Akki pauses as I get used to him and, slowly, I allow myself to relax."
            $ akki_missionary_sprite.set_state(with_dissolve, akki=1, claire=1)
#            $lay_aface = "1"
#            $lay_cface = "1"
            voice "a_s13"
            ak "Should I keep going?"
            cla "Yes, I'm fine now."
            $ akki_missionary_sprite.set_state(with_dissolve, akki=2, claire=2)
#            $lay_aface = "2"
#            $lay_cface = "2"
            "I feel like I'm sinking into the pillows as he enters me. When our hips touch, I inhale sharply from the warmth and filling sensation. He notices I'm clenching the sheets and leans in."
            $ akki_missionary_sprite.set_state(with_dissolve, akki=1, claire=1)
#            $lay_aface = "1"
#            $lay_cface = "1"
            voice "a_sex41"
            ak "Are you okay?"
            cla "Yeah. Um, it's a little tight so... don't move around too much."
            voice "a_sex42"
            ak "I understand. I'll..."
            $ akki_missionary_sprite.set_state(with_dissolve, akki=2)
#            $lay_aface = "2"
            "He moves his hip back, slides forward again, keeping an unhurried tempo."
            $ akki_missionary_sprite.set_state(with_dissolve, claire=2)
#            $lay_cface = "2"
            voice "a_sex43"
            ak "Ah..."

            #remove stop button, it's all done.
            hide screen sex_stop
            $ akki_missionary_sprite.set_state(with_dissolve, akki=3)
#            $lay_aface = "3"
            stop music
            play sound "assets/sfx/scratch.ogg"
            $renpy.pause()
            $ akki_missionary_sprite.set_state(with_dissolve, akki=4)
#            $lay_aface = "4"
            "Suddenly, he halts in his movements and he hastily averts his gaze from me."
            $ akki_missionary_sprite.set_state(with_dissolve, claire=1)
#            $lay_cface = "1"
            cla "You okay?"
            ak "..."
            voice "a_sex44"
            extend "Er, I finished early..."
            cla "..."
            $ akki_missionary_sprite.set_state(with_dissolve, akki=5)
#            $lay_aface = "5"
            voice "a_sex45" 
            ak "I can keep going."
            cla "You sure? We can stop, you know."
            voice "a_sex46"
            ak "Seriously, I can keep going. Just... uh, give me a minute..."
            $ akki_missionary_sprite.set_state(with_dissolve, claire=3)
#            $lay_cface = "3"
            "His abashed expression causes me to burst out laughing against my best intentions."
            play music music_love fadein 1
            cla "I-it's okay! Don't force yourself. I'm really happy with where we are."
            $ akki_missionary_sprite.set_state(with_dissolve, akki=6)
#            $lay_aface = "6"
            voice "a_sex47" 
            ak "Really?"
            cla "Yes, honest. This has been a great experience, Akki."
            $ akki_missionary_sprite.set_state(with_dissolve, claire=1)
#            $lay_cface = "1"
            "I hug him close to show that I mean it, and I feel him chuckle lightly and relax."
            voice "a_sex48"
            ak "...Same here."
            stop music fadeout 2
            voice "a_sex49"
            "We giggle and he kisses my forehead."
            play music music_lullaby fadein 2
            cla "Thank you, Akki."
            #transition
            scene white with dissolve
            pause (0.8)
            python:
                akki_cuddle_sprite.set_state(
                    base="naked" if akki_sex_choices.missionary else "clothed",
                    claire=1, akki=3
                )            
#            $cuddle_cface = "1"
#            $cuddle_aface = "3"
            scene akkicuddle with dissolve

            "I'm curled up against Akki's chest, feeling fulfilled and happy. He places a protective hand on my head, and strokes my hair. I can tell he's still feeling a little sheepish over the whole incident."
            $ akki_cuddle_sprite.set_state(with_dissolve, claire=2)
#            $cuddle_cface = "2"
            cla "No matter the conclusion, nothing beats a good cuddle afterwards, right, Akki?"
            $ akki_cuddle_sprite.set_state(with_dissolve, akki=2)
#            $cuddle_aface = "2"
            ak "You can say that again."
            $ akki_cuddle_sprite.set_state(with_dissolve, akki=1)
#            $cuddle_aface = "1"
            voice "a_sex52"
            ak "How are you feeling?"
            cla "Content... Maybe a little sore. I'm really happy my first time was with you."
            ak "Same."
            if akki_scenes >= 3:
                $ persistent.akki_complete = True
                ak "And I hope the next time will be even better for you."
                cla "If it's with you again, I know it will."
            $ akki_cuddle_sprite.set_state(with_dissolve, claire=3, akki=3)
#            $cuddle_cface = "3"
#            $cuddle_aface = "3"
            "Exhaustion creeps in and I know Akki obtained nourishment from our experience. Satisfied, I allow myself to fall into a deep sleep."
            call credits from _call_credits_6
            $akki_epilong = True
            jump akki_epilogue
                
        "I'd like to stop now.":   
            jump akki_middle_stop



label akki_early_stop:
    hide screen sex_stop
    if ac_heads == "kiss":
        $ akki_foreplay.set_state(with_dissolve, heads="apart", akki_face="happy", claire_face="embarrassed")
#            $ac_heads = "apart"
#            $ak_face = "happy"
    else:
        $ akki_foreplay.set_state(with_dissolve, claire_face="embarrassed")
#    $cl_face = "embarrassed"
    cla "Um... I change my mind. I'd like to stop here if that's alright."
    $ akki_foreplay.set_state(with_dissolve, claire_arm="down", akki_arm="down", akki_face="D:")
#    $cl_arm = "down"
#    $ak_arm = "down"
#    $ak_face = "D:"
    voice "a_sex05"
    ak "O-of course it's alright. I hope I didn't make you feel uncomfortable."
    cla "It's not that... I just feel this is enough for me."
    scene bg bedroom_night with dissolve
    $claire.set_state(**Emotion.normal())
    $claire.set_state(emotion_base="small blush", eyebrows="inwards", eyes="tender side", emotion="default", mouth="low")
    $akki.set_state(emotion_base="small blush", mouth="default", eyes="default", eyebrows="tender", emotion="default")
    show akki at center_alone2 with dissolve
    cl "Sorry, maybe I wasn't as ready as I thought."
    voice "a_sex07"
    ak "That's fine. Sometimes you don't really know until you reach that point. Kael told me." 
    $akki.set_state(eyebrows="inwards", mouth="low")
    ak "You don't like me less now, right?"
    if akki_scenes >= 1:
        $claire.set_state(eyes="clench", mouth="uh")
        cl "Of course not! Akki, you're very sweet. Sometimes you don't even blue shell me when I'm in first place."
        $akki.set_state(with_dissolve, eyes="fun front", mouth="uh", eyebrows="up")
        voice "a_s15"
        ak "Now {i}that{/i} takes real self-control."
        $akki.set_state(with_dissolve, eyes="happy", mouth="smile", eyebrows="default")
        "I giggle and he plants a platonic kiss on my forehead."
    else: 
        $claire.set_state(eyes="tender", mouth="smile", eyebrows="default")
        cl "Of course not! Akki, you're very sweet. Thank you."
        $akki.set_state(with_dissolve, eyes="happy", mouth="smile", eyebrows="default")
        "He plants a platonic kiss on my forehead." 
    $claire.set_state(eyes="happy", mouth="happy", eyebrows="up")
    cl "I'll be up for a cuddle though." 
    stop music fadeout 2
    if akki_scenes >= 3:
        $akki.set_state(with_dissolve, eyes="happy", eyebrows="default", mouth="grin")
        voice "a_sex11"
        ak "You know me so well."
    else:
        $akki.set_state(with_dissolve, eyes="happy", eyebrows="default", mouth="smile")
        ak "I'd like that."
    play music music_lullaby fadein 2
    python:
        akki_cuddle_sprite.set_state(
            base="naked" if akki_sex_choices.missionary else "clothed",
            claire=3, akki=3
            )    
    scene akkicuddle with dissolve
    "We both curl up on the bed. Once we're comfortable, he hugs me close, one hand stroking my hair."
    "I can feel his chest rise and fall, and his warm breath on my forehead. Soothed, I allow myself to drift into a restful sleep."     

    call credits from _call_credits_7
    jump akki_epilogue


label akki_middle_stop:
    hide screen sex_stop
    $ akki_foreplay.set_state(with_dissolve, claire_arm="down", heads="apart", akki_face="happy", claire_face="embarrassed")
#    $ cl_arm = "down"
#    $ac_heads = "apart"
#    $ak_face = "happy"
#    $ cl_face = "embarrassed"       
    cla "I'd... like to stop if that's alright with you."
    voice "a_sex08"
    ak "I understand."
    $ akki_foreplay.set_state(with_dissolve, akki_arm="down")
#    $ak_arm = "down"
    "He removes his hands from my thighs."
    scene bg bedroom_night with dissolve
    $claire.set_state(**Emotion.normal())
    $claire.set_state(emotion_base="small blush", eyebrows="inwards", eyes="tender side", emotion="default", mouth="low")
    $akki.set_state(emotion_base="small blush", mouth="default", eyes="default", eyebrows="tender", emotion="default")
    show akki at center_alone2 with dissolve
    cl "I'm sorry, I feel like I pulled away when it was getting good..."
    $akki.set_state(with_dissolve, eyes="tender")
    voice "a_sex09"
    ak "Don't be! Kael told me it's important to respect our lovers, and they're allowed to change their mind at any time."
    $akki.set_state(with_dissolve, eyebrows="inwards", mouth="oh",)
    ak "I-I hope I'm doing this right."
    if akki_scenes >= 3:
        $akki.set_state(with_dissolve, eyes="tender side", mouth="neutral")
        ak "It's hard to explain but... you're important to me. I don't want to do anything that'd make you unhappy." 
    else:
        $akki.set_state(with_dissolve, mouth="smile")
        ak "I'm happy you're honest with me. I don't want to do something you'd silently dislike."
    $claire.set_state(with_dissolve, eyes="default", eyebrows="inwards", mouth="smile")
    cl "Thank you, Akki."
    $claire.set_state(with_dissolve, eyes="happy")
    cl "I just feel I'm not ready to go the whole way yet. Thank you for being attentive to my needs."
    $akki.set_state(with_dissolve, eyes="happy", eyebrows="tender", mouth="smile")
    voice "a_sex10"
    ak "No problem. We can still cuddle, right?"
    $claire.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="happy")
    stop music fadeout 2
    if akki_scenes >= 3:
        cl "Of course, I know you love those."
    else: 
        cl "Of course. Cuddling sounds amazing right now."
    python:
        akki_cuddle_sprite.set_state(
            base="naked" if akki_sex_choices.missionary else "clothed",
            claire=1, akki=3
            )
#    $cuddle_cface = "1"
#    $cuddle_aface = "3"
    play music music_lullaby fadein 2
    scene akkicuddle with dissolve
    "We both curl up on the bed. Once we're comfortable, he hugs me close, one hand stroking my hair."
    $ akki_cuddle_sprite.set_state(with_dissolve, akki=1)
#    $cuddle_aface = "1"
    ak "I... still got a little energy from your arousal. Thank you..."
    voice "a_sex22"
    ak "I'm glad I got to experience it with you..."
    cla "Aw, same here... Thanks for making me feel things I never felt before."
    $ akki_cuddle_sprite.set_state(with_dissolve, akki=3, claire=3)
#    $cuddle_aface = "3"
#    $cuddle_cface = "3"
    "I can feel his chest rise and fall, and his warm breath on my forehead. Soothed, I allow myself to drift into a restful sleep."      
    call credits from _call_credits_8
    jump akki_epilogue

label akki_late_stop:
    hide screen sex_stop
    $ akki_foreplay.set_state(with_dissolve, claire_arm="down", heads="apart", akki_face="happy", claire_face="embarrassed")
#    $ cl_arm = "down"
#    $ ac_heads = "apart"
#    $ ak_face = "happy"
#    $ cl_face = "embarrassed"     
    cla "Maybe it's for the best we stop now."
    $ akki_foreplay.set_state(with_dissolve, akki_arm="down")
    cla "Um, I'm still sorting out these... feelings..."
    voice "a_sex08"
    ak "I understand. It felt... nice."
    $ akki_foreplay.set_state(with_dissolve, claire_face="happy")
#    $ cl_face = "happy"
    cla "Hehehe..."
    scene bg bedroom_night with dissolve
    "I hug him tightly and I can feel his chest shudder from a faint chuckle."
    $claire.set_state(**Emotion.normal())
    $claire.set_state(emotion_base="small blush", eyebrows="default", eyes="tender", emotion="default", mouth="smile")
    $akki.set_state(emotion_base="small blush", mouth="default", eyes="default", eyebrows="tender", emotion="default")
    show akki at center_alone with dissolve
    ak "I'm so glad I was able to make you happy..."
    $akki.set_state(with_dissolve, eyes="happy")
    ak "Shall we take it easy now? We can cuddle."
    cl "I'd like that..."
    $claire.set_state(with_dissolve, eyes="tender side", eyebrows="inwards", mouth="low")
    cl "I'm sorry, I feel like we could've done more..."
    $akki.set_state(with_dissolve, eyes="default", mouth="happy")
    ak "No, I think this was a good first step for the both of us."
    stop music fadeout 2
    $akki.set_state(with_dissolve, eyes="wink", mouth="smile")
    ak "Who said we had to go all the way?"
    python:
        akki_cuddle_sprite.set_state(
            base="naked" if akki_sex_choices.missionary else "clothed",
            claire=1, akki=3
            )    
#    $cuddle_cface = "1"
#    $cuddle_aface = "3"
    play music music_lullaby fadein 2
    scene akkicuddle with dissolve
    
    "I giggle, mostly from the lightheadedness and exhaustion. We curl up on the bed, and Akki holds me close."
    $ akki_cuddle_sprite.set_state(with_dissolve, akki=2)
#    $cuddle_aface = "2"
    ak "I'm so glad you were my first..."
    cla "Me, too, Akki..."
    $ akki_cuddle_sprite.set_state(with_dissolve, claire=3, akki=3)
#    $cuddle_cface = "3"
#    $cuddle_aface = "3"
    "His chest rises and falls, and his warm breath tickles my bangs. Soothed, I allow myself to fall asleep..."
    call credits from _call_credits_9
    jump akki_epilogue


label akki_super_late_stop:
    hide screen sex_stop        
    $akki.set_state(with_dissolve, eyebrows="tender", eyes="default", mouth="smile")
    "I hug him to show my appreciation, and he embraces me in return."
    voice "a_sex06"
    ak "Of course. Shall we take it easy now? We can cuddle."
    stop music fadeout 2
    cl "I'd like that..."
    python:
        akki_cuddle_sprite.set_state(
            base="naked" if akki_sex_choices.missionary else "clothed",
            claire=1, akki=3
            )    
#    $cuddle_cface = "1"
#    $cuddle_aface = "3"
    play music music_lullaby fadein 2
    scene akkicuddle with dissolve
    "We curl up on the bed, and I rest my head on Akki's chest. He gingerly combs through my hair and plants a chaste kiss on my head."
    $ akki_cuddle_sprite.set_state(with_dissolve, akki=1)
#    $cuddle_aface = "1"
    ak "Even if we didn't go all the way, I... still got nourished by you."
    $ akki_cuddle_sprite.set_state(with_dissolve, claire=2)
#    $cuddle_cface = "2"
    cla "So it's a win-win scenario?"
    $ akki_cuddle_sprite.set_state(with_dissolve, akki=2)
#    $cuddle_aface = "2"
    voice "a_sex51"
    ak "Heh, I think so. Thank you for being my first. I consider it a first, anyway."
    cla "Same here, Akki..."
    "His chest rises and falls, and his warm breath tickles my bangs. Soothed, I allow myself to fall asleep..."
    call credits from _call_credits_10
    jump akki_epilogue


label akki_stop_now:
    if not _in_replay:
        $ persistent.akki_sex_stop = last_statement
    hide screen sex_stop 
    if akki_sex_choices.missionary:
        $ akki_missionary_sprite.set_state(with_dissolve, claire=2)
#        $lay_cface = "2"
        hide screen sex_stop
        cla "I'd like to stop now..."
        $ akki_missionary_sprite.set_state(with_dissolve, akki=2)
#        $lay_aface = "2"
        "Akki freezes, then carefully withdraws as I sit up as well."
        scene bg bedroom_night with dissolve
        $akki.set_state(eyebrows="inwards", mouth="oh",emotion_base="small blush", emotion="default", eyes="default")
        show akki at center_alone2 with dissolve
        ak "Were things going too fast for you...?"
        $claire.set_state(eyes="down", eyebrows="inwards", mouth="lip bite", emotion="default", emotion_base="small blush")
        cl "..."
        $akki.set_state(with_dissolve, eyes="wide", mouth="ah")
        voice "a_sex50"
        ak "Ah, don't worry. Don't feel like you need to explain yourself. I just hope I didn't make you uncomfortable."
        $claire.set_state(eyes="tender", eyebrows="inwards", mouth="smile")
        cl "No, you did nothing wrong, Akki. Thank you for listening. I'm satisfied with how far we got."
        jump akki_super_late_stop

    elif akki_sex_choices.between_thighs:
        $ akki_foreplay.set_state(with_dissolve, claire_arm="down", heads="apart", akki_face="D:", claire_face="embarrassed")
        hide screen sex_stop
        cla "I'd like to stop..."
        voice "a_s13"
        $ akki_foreplay.set_state(with_dissolve, akki_arm="down")
        ak "Was it feeling a little overwhelming for you..?"
        cla "Yeah, so..."
        jump akki_late_stop     

    elif akki_sex_choices.thighs:
        jump akki_middle_stop

    elif akki_sex_choices.kissing:
        hide screen sex_stop
        "I break off the kiss."
        jump akki_early_stop

    elif akki_sex_choices.breasts:
        hide screen sex_stop
        "I gently cover his hands to stop his movements."
        jump akki_early_stop

    elif akki_sex_choices.below_waist:
        hide screen sex_stop
        "I shy away and close my legs."
        jump akki_early_stop

    else:
        jump akki_early_stop
    
label akki_epilogue:
    # smaller epilogues you get if:
    #1) didn't see all three scenes from the same sex demon
    #2)didn't make it ALL the way with sex. 
    if akki_scenes==3 and akki_epilong == True:
        jump akki_epilogue_long
    else:
        pass
    scene bg bedroom_day with dissolve 
    play sound "assets/sfx/bird_chirp.ogg"
    pause(0.5)
    $ claire.set_state(eyes="closed", eyebrows="frown", mouth="default", emotion="default", emotion_base="default")
    if claire_base.current_state == "default":
        $claire.set_state(base="default")
    else:
        $claire.set_state(base="lazy")
    cl "Mm..."
    "I groggily open my eyes. When I roll over, I realize the bed is empty and I place an arm out to confirm I'm indeed alone."
    $ claire.set_state(eyes="semi open", eyebrows="default", mouth="oh")
    cl "...Was it a dream?"
    "I sit up and reach for my phone as part of my routine. But there's something different about it. Next to my phone is a note. Curious, I pick it up."
    scene white with dissolve
    voice "a_note01"
    show text "{color=#000}'Thanks for everything, [claire_name].\n It was my first time in the human world, and I had a lot of fun.\n If you ever want to see me again, draw the symbol and repeat\n the words on the back of the note to summon me.\n I promise I'll make tastier aebleskiver next time.\n - Akki.'{/color}" with dissolve
    $renpy.pause()
    voice "a_note02"
    show text "{color=#000}'P.S. Uh, technically you'd be summoning Kael.\n I'm too weak to actually be summoned yet but I wanted to sound cool for a moment.'{/color}" with dissolve
    $renpy.pause()
    show bg bedroom_day with dissolve
    $ claire.set_state(eyes="semi open", eyebrows="default", mouth="grin")
    cl "Aw, I thought the aebleskiver were delicious."
    cl "Thanks, Akki."
    $ persistent.akki_replay = True
    scene white with dissolve
    hide screen replay_controls
    $ renpy.end_replay()
    return

label akki_epilogue_long:
    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    $renpy.pause(0.4)
    play music music_akki
    $akki.set_state(base="human", **Emotion.normal())
    scene bg street with dissolve
    $ claire.set_state(base="default", **Emotion.normal())
    $claire.set_state(eyes="closed", emotion="sigh", eyebrows="inwards", mouth="uhh", emotion_base="default")
    cl "..."
    "I sigh as I walk home from university." 
    "It's been a week after my spring break, and I still miss Akki. It almost feels like a dream..."
    voice "a_w13"
    "???" "[claire_name]!"
    $claire.set_state(eyes="default", emotion="default", eyebrows="default", mouth="uh", emotion_base="default")
    cl "Huh?"
    $claire.set_state(eyes="wide", emotion="shock", eyebrows="up", mouth="oh", emotion_base="default")
    cl "Wha— Akki!?"
    $akki.set_state(emotion="flowers", eyes="happy", mouth="grin", emotion_base="small blush")
    show akki at center_alone2 with dissolve
    voice "a_s10"
    ak "There you are!"
    $akki.set_state(emotion="default", eyes="happy", mouth="happy", emotion_base="small blush", eyebrows="default")
    show akki at bounce_up_alone2
    "We run toward each other, arms outstretched. At the last second, he picks me up and twirls around, laughing before embracing me close."
    $akki.set_state(emotion="default", eyes="default", mouth="smile")
    "He kisses me deeply, and we step back from our hug."
    $claire.set_state(eyes="happy", emotion="flowers", eyebrows="default", mouth="happy", emotion_base="default")
    cl "It's you! And look at you, all cleverly disguised."
    $akki.set_state(emotion="note", eyes="happy", mouth="grin", emotion_base="small blush")
    voice "a_s05"
    ak "What do you think? It took me a while to master the spell."
    $akki.set_state(emotion="default", eyes="happy", mouth="smile", emotion_base="small blush")
    show akki at sway
    "He turns around once, then tugs on his shirt."
    $akki.set_state(emotion="default", eyes="fun front", mouth="low", emotion_base="default", eyebrows ="default")
    voice "a_s08"
    ak "Human clothing is so restrictive though." 
    $claire.set_state(eyes="happy", emotion="default", eyebrows="default", mouth="happy", emotion_base="default")
    $akki.set_state(emotion="default", eyes="default", mouth="tiny", emotion_base="small blush", eyebrows ="default")
    cl "Even so, you look great."
    $claire.set_state(eyes="down", emotion="default", eyebrows="default", mouth="smile", emotion_base="small blush")
    cl "I've missed you so much."
    $akki.set_state(emotion="default", eyes="tender side", mouth="oh", emotion_base="large blush", eyebrows ="inwards")
    voice "a_s13"
    ak "I've missed you too, [claire_name]."
    $claire.set_state(eyes="semi open", emotion="default", eyebrows="inwards", mouth="low", emotion_base="default")
    $akki.set_state(emotion="default", eyes="tender side", mouth="low", emotion_base="small blush", eyebrows ="inwards")
    cl "I thought, once you left, there was some kind of demon law where you could never see me again..."
    $akki.set_state(emotion="default", eyes="happy", mouth="smile", emotion_base="default", eyebrows ="tender")
    voice "a_epi02"
    ak "What? Of course not. As long as you want to see me, I can."
    $claire.set_state(eyes="default", emotion="default", eyebrows="default", mouth="uh", emotion_base="small blush")
    $akki.set_state(emotion="default", eyes="default", mouth="smile", emotion_base="default", eyebrows ="tender")
    cl "Then... you can visit me anytime?"
    $akki.set_state(emotion="note", eyes="happy", mouth="grin", emotion_base="default", eyebrows ="tender")
    voice "a_epi03"
    ak "Yes. Now I've learned how to disguise myself, we can do more things together."
    $claire.set_state(eyes="happy", emotion="flowers", eyebrows="default", mouth="grin", emotion_base="default")
    cl "That's great! I know you're new to the human world, and I'd love to show you around."
    $akki.set_state(emotion="default", eyes="default", mouth="oh", emotion_base="default", eyebrows ="default")
    voice "a_epi04"
    ak "As a fling?"
    $claire.set_state(eyes="default", emotion="default", eyebrows="up", mouth="oh", emotion_base="default")
    cl "Huh?"
    $akki.set_state(emotion="default", eyes="tender side", mouth="wavy", emotion_base="small blush", eyebrows ="tender")
    voice "a_s13"
    ak "Um... I remember you mentioning that you wouldn't mind a fling... I'm not sure what it means, but if I can spend time with you..." 
    $claire.set_state(eyes="tender", emotion="default", eyebrows="default", mouth="smile", emotion_base="small blush")
    cl "Depends, how long you would like to see me? For a little while or a longer while?"
    $akki.set_state(emotion="default", eyes="tender side", mouth="oh", emotion_base="large blush", eyebrows ="tender")
    ak "A longer while if possible..."
    $akki.set_state(emotion="default", eyes="default", mouth="neutral", emotion_base="small blush", eyebrows ="tender")
    $claire.set_state(eyes="tender", emotion="default", eyebrows="default", mouth="grin", emotion_base="small blush")
    cl "Then lovers would be a better term." 
    $akki.set_state(emotion="default", eyes="default", mouth="smile", emotion_base="small blush", eyebrows ="tender")
    "Our fingers intertwine, and I tug him gently forward."
    $claire.set_state(eyes="happy", emotion="note", eyebrows="default", mouth="grin", emotion_base="default")
    cl "I think this calls for a celebration. What would you like to do?"
    $akki.set_state(emotion="heart", eyes="starry", mouth="drool", emotion_base="default", eyebrows ="tender")
    voice "a_s05"
    ak "I'd like to have that pizza again from—"
    $claire.set_state(eyes="shock", emotion="shock", eyebrows="frown", mouth="fun ah2", emotion_base="no nose")
    $akki.set_state(emotion="bars", eyes="dots", mouth="low", emotion_base="default", eyebrows ="up")
    cl "NO!"
    $akki.set_state(emotion="default", eyes="cry", mouth="ehh", emotion_base="default", eyebrows ="inwards")
    voice "a_s02"
    ak "No?"
    $claire.set_state(eyes="happy", emotion="panic", eyebrows="inwards", mouth="ehh", emotion_base="small blush")
    cl "Ah, there's a pizza place by my campus. Let's celebrate there instead." 
    $akki.set_state(emotion="flowers", eyes="happy", mouth="happy", emotion_base="default", eyebrows ="tender")
    show akki at bounce_up_alone2
    voice "a_epi06"
    ak "Okay!"
    $claire.set_state(eyes="default", emotion="default", eyebrows="default", mouth="oh", emotion_base="default")
    cl "You seem a little different today."
    $akki.set_state(emotion="default", eyes="tender side", mouth="oh", emotion_base="small blush", eyebrows ="tender")
    voice "a_s13"
    ak "You've noticed? Um... after that night..."
    $akki.set_state(emotion="default", eyes="tender", mouth="smile", emotion_base="small blush", eyebrows ="tender")
    voice "a_epi07"
    ak "I can't explain it, but I feel revitalized. I've never felt better. It's thanks to you, [claire_name]."
    $akki.set_state(emotion="default", eyes="happy", mouth="smile", emotion_base="default", eyebrows ="tender")
    "He wraps his arms around my waist and leans in, his breath tickling my ear."
    $akki.set_state(emotion="heart", eyes="happy", mouth="grin", emotion_base="default", eyebrows ="tender")
    voice "a_epi09"
    ak "You're better than pizza."
    $claire.set_state(eyes="tender", emotion="default", eyebrows="default", mouth="grin", emotion_base="small blush")
    cl "That's the most unsexy compliment I've ever heard. I'll take it."
    $ persistent.akki_replay = True    
    stop music fadeout 1
    scene white with dissolve
    hide screen replay_controls
    $ renpy.end_replay()
    return

