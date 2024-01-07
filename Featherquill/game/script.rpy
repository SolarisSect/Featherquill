# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hatate", color="#cf29be")
define s = Character("Satori", color="#9229cf")
define q = Character("???", color="#9229cf")
default birds_appreciated = 0
default menuset = set()

# The game starts here.

label start:

    stop music fadeout 1.0

    "In the midst of a cold winter’s night, a crow tengu rests beneath the soil, with a certain warmth enveloping her."

    "Not just the warmer surroundings of the underground palace she’s visiting, but the hot flash caused by her own anxiety."

    "She stands in front of the door to the room of the palace’s mistress, wanting nothing more than to knock, but not having the courage to do so."

    "It’s silly, she thinks to herself, the atmosphere here is surprisingly lively, so why is she even freezing up like this?"

    "Because of how long it’s been since she last tried interviewing someone?"

    "Because her interview idea itself is silly?{w} Because she might be considered annoying?"

    "Because there’s always that one voice screaming at her that her words aren’t of worth, that she should just quit while she’s ahead, that she’s both not seeing enough of the world yet wasting everyone’s time when she tries? That-"

    "... ..."

    play sound "knockknock.ogg"

    pause(2.2)

    q "Come in. I've been told to expect you."

    "Who knew a moment of anger was all it took to focus."

    scene bg_palace
    with fade

    play music "Heartfelt_Fancy.mp3" fadein 1.0

    "The crow tengu, Hatate Himekaidou, enters the room to immediate awe. This was her casual workplace? It was large enough to be a whole library."

    show hatate_surprised at left

    h "Whoa... I, erm, sorry. I hope didn't pick a bad time to come."

    show satori_smiling at right

    q "It's fine, don't worry. I wasn't really doing much today."

    show hatate_thinking at left

    "Hatate takes a deep breath, and does her best to put on her work face."

    show hatate_smiling at left

    h "Haha, well, okay. It's nice to meet you, Satori Komeiji!"

    s "Likewise, Hatate Himekaidou."

    h "Right. The pet who introduced me at your doorstep would've told you my name."

    show satori_smug at right

    s "Indeed."

    show satori_smiling at right

    "Hatate approaches Satori's desk, giving an anxious glance towards the satori's 3rd eye staring right towards her."

    show hatate_anxious at left

    h "Uhm, if it's not too much to ask, do you mind pointing that thing away? It's kind of an evasion of privacy, haha..."

    show satori_sighing at right

    "Satori lets out a hefty sigh, but listens and follows suit regardless, shifting her eye to the side."

    show satori_tired at right

    s "Does that make you feel more comfortable?"

    show hatate_smiling at left

    h "Yes. Thank you."

    "Satori gestures towards the free chair on the other side of her table. Hatate takes the invitation, finding the chair surprisingly comfortable. How well made was the furniture down here?"

    "Or, well, maybe the furniture in the Tengu Village just really sucked."

    show satori_thinking at right

    s "So, I take it you're here to interview me, right? Is there anything you particularly had in mind?"

    h "Well, it's that I was quite fascinated hearing stories about your vast collection of pets! I figured a piece on the birds here in particular would be just the kind of thing for my paper."

    show hatate_excited at left

    h "I can already tell you have some really fun critters around here, so I'd love to learn more about them. And I'm sure the readers of the Kakashi Spirit News would love to as well!"

    show satori_smiling at right

    s "Oh, you're taking an interest in my pets? Here was I worried you were going to ask some annoying questions about my private life."

    show hatate_annoyed at left

    h "Please, I have better things to do than that. I'm more tasteful than some others."

    show satori_thinking at right

    s "Hmm.{w} In that case, I'd actually love to take you up on your offer."

    show hatate_surprised at left

    h "Wait, really? You don't think it's too silly of an idea or anything?"

    show satori_laughing at right

    s "No, of course not! I could talk about my pets for hours."

    show satori_tired at right

    s "And well, I don't typically get any visitors in the first place, although I usually don't appreciate their company either."

    show hatate_frowning at left

    h "Yeah... I can unfortunately understand why. Some people down here seem really mean."

    show satori_sighing at right

    s "You get used to it, for the better or worse. Hasn't stopped me from doing what I truly love at least."

    "Hatate couldn't help but wonder what kind of hobbies Satori got up to in her spare time. Maybe it was impersonal enough to ask about later?"

    h "That's good at least."

    show hatate_smiling at left

    h "Well, in any case, if you're down, then how about we get this interview started! I already have a few particular pets I'd like to ask about."

    show satori_smiling at right

    s "Feel free to shoot your questions then."

menu the_birds:

    set menuset
    h "Let's check what I have written down in my notes."

    "the crane hiding around the kitchen":
        $ birds_appreciated += 1
        jump talk_crane

    "the stork and her family of chicks (*^ ω ^)":
        $ birds_appreciated += 1
        jump talk_stork

    "the cockatoo resting beneath an abandoned birdcage":
        $ birds_appreciated += 1
        jump talk_cockatoo

    "that kiwi bird freaking ZOOMING around the place, holy crap":
        $ birds_appreciated += 1
        jump talk_kiwi

label talk_crane:

label talk_stork:

label talk_cockatoo:

label talk_kiwi:

       h "So that little kiwi bird of yours, right? She seems uh, really energetic. What's that like to deal with as a pet owner?"

       s "I've had to changed furniture in several rooms for Kuri, haha."

       h "Oh dear."

       s "You see, she's such a little ball of unfiltered energy that she kept constantly tripping around the palace."

       s "Kuri never got that hurt from any of his antics, but I started to realize she needed a bit of help, you know?"

       s "I love her, but she's been one of my most handful pets."

       h "I'm glad you've given her some good care. Seems like a really good friend at the end of the day."

       s "Yes! Very true.{w} Not enough people down in the underground appreciate the idea that animals can be your best friends."

       s "Kuri's very different from what I was used to when I first adopted her, but in sticking it out with the learning process, I learned so many things to appreciate about her."

       s "She's so adorable to play with, for instance! An absolutely fantastic cuddler too."

       h "Aw. That's so cute!"

       s "I'm glad I managed to find her. Kiwi birds are very extant, like many things I've taken under my wing, I really wonder how she even got down here in the first place."

       s "And well, kiwis aren't exactly really good at defending themselves. Running, sure, but I'd hardly expect one to win a fight."

       s "She could've gotten seriously hurt before I ever laid my eyes on hier. I may not have ever met her at all. But she's found somewhere comfortable to be here, and I think that's really nice."

       h "Yeah, I've always wondered what the climate for animals must be like down here."

       s "Awful, most of the time. The underground, especially around Former Hell in particular, is extremely about adaption. If you aren't some magical hell raven, you're basically doomed from the start."

       s "Really, Kuri is a large example of why I'm a pet owner, I think. I like to view the Palace of the Earth Spirits as a safe haven in a sea of terrible pet owners.{w} Maybe calling myself the one who cares is a bit egotistical, but I think it's true."

       h "I don't think I would disagree. This place is way more comfortable to be in than the rest of Former Hell to me."

       s "Really now? Most tengus I've met are quite the partying type."

       h "I'm usually sitting on the sidelines of most parties, haha. Crowds can get kind of too much for me.{w} Maybe I'm not too far from a little bird myself."

       s "You're certainly tall for one, haha."

       s "But yeah, I'm glad you're comfortable here."

       h "And I'm happy your pets can feel the same."

       jump the_birds

label after_the_birdial:

    h "Well, those were some very nice fellas of yours!"

    return
