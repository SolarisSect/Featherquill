# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hatate", color="#ffd3fb",who_outlines = [(3,"#8b1980")])
define s = Character("Satori", color="#eed0ff",who_outlines = [(3,"#9229cf")])
define q = Character("???", color="#eed0ff",who_outlines = [(3,"#9229cf")])
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

    show hatate surprised at left

    h "Whoa... I, erm, sorry. I hope didn't pick a bad time to come."

    show satori smiling at right

    q "It's fine, don't worry. I wasn't really doing much today."

    show hatate thinking at left

    "Hatate takes a deep breath, and does her best to put on her work face."

    show hatate smiling at left

    h "Haha, well, okay. It's nice to meet you, Satori Komeiji!"

    s "Likewise, Hatate Himekaidou."

    h "Right. The pet who introduced me at your doorstep would've told you my name."

    show satori smug at right

    s "Indeed."

    show satori smiling at right

    "Hatate approaches Satori's desk, giving an anxious glance towards the satori's 3rd eye staring right towards her."

    show hatate anxious at left

    h "Uhm, if it's not too much to ask, do you mind pointing that thing away? It's kind of an evasion of privacy, haha..."

    show satori sighing at right

    "Satori lets out a hefty sigh, but listens and follows suit regardless, shifting her eye to the side."

    show satori tired at right

    s "Does that make you feel more comfortable?"

    show hatate smiling at left

    h "Yes. Thank you."

    "Satori gestures towards the free chair on the other side of her table. Hatate takes the invitation, finding the chair surprisingly comfortable. How well made was the furniture down here?"

    "Or, well, maybe the furniture in the Tengu Village just really sucked."

    show satori thinking at right

    s "So, I take it you're here to interview me, right? Is there anything you particularly had in mind?"

    h "Well, it's that I was quite fascinated hearing stories about your vast collection of pets! I figured a piece on the birds here in particular would be just the kind of thing for my paper."

    show hatate excited at left

    h "I can already tell you have some really fun critters around here, so I'd love to learn more about them. And I'm sure the readers of the Kakashi Spirit News would love to as well!"

    show satori smiling at right

    s "Oh, you're taking an interest in my pets? Here was I worried you were going to ask some annoying questions about my private life."

    show hatate annoyed at left

    h "Please, I have better things to do than that. I'm more tasteful than some others."

    show satori thinking at right

    s "Hmm.{w} In that case, I'd actually love to take you up on your offer."

    show hatate surprised at left

    h "Wait, really? You don't think it's too silly of an idea or anything?"

    show satori laughing at right

    s "No, of course not! I could talk about my pets for hours."

    show satori tired at right

    s "And well, I don't typically get any visitors in the first place, although I usually don't appreciate their company either."

    show hatate frowning at left

    h "Yeah... I can unfortunately understand why. Some people down here seem really mean."

    show satori sighing at right

    s "You get used to it, for the better or worse. Hasn't stopped me from doing what I truly love at least."

    "Hatate couldn't help but wonder what kind of hobbies Satori got up to in her spare time. Maybe it was impersonal enough to ask about later?"

    h "That's good at least."

    show hatate smiling at left

    h "Well, in any case, if you're down, then how about we get this interview started! I already have a few particular pets I'd like to ask about."

    show satori smiling at right

    s "Feel free to shoot your questions then."

menu the_birds:

    set menuset
    h "Let's check what I have written down in my notes."

    "the crane hiding around the kitchen":
        $ birds_appreciated += 1
        jump talk_crane

    "the stork and her chick (*^ ω ^)":
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

       h "This stork and her chick are absolutely adoarble! What's it like looking over a family?"
	   
	   s "Well, it's worth noting that I raised two storks since they were chicks, imported from the mountain around the entrance to the underground,"
	   
	   s "So just seeing them go on to make a family together has been really sweet for me."
	   
	   s "To get onto what it's like looking a family, though.{w} Well, I think I've gotten pretty used to it, since they mostly take care of themselves anyway."
	   
	   s "I do my best to help provide for the chicks, though, just to take some of the stress off the parents. And they really are adorable when they're together."
	   
	   s "Before this little stork family came into my life recently, I'd never actually really seen what birds flocking together was like."
	   
	   s "Even in spite of just how many bird species lay within this palace.
	   
	   s "But watching the chicks lovingly follow their parents as they explore the palace, or playing around with the other birds..."
	   
	   s "I think it's really reenforced this sense of community I've always loved in regards to raising all of these different animals."
	   
    
label talk_cockatoo:

       show hatate thinking at left

       show satori smiling at right

       h "Something funny I happened to notice was a cockatoo underneath a rather abandoned birdcage. I take it you like letting your birds fly freely?"

       s "Yes. I find my pets in better spirits when they aren't as restricted around the palace. Most of them behave pretty well regardless."

       show satori laughing at right

       s "This cockatoo, Percy, though... happens to be one of worse behaved ones, haha. Ironic that you'd find him near an abandoned cage."

       show satori smiling at right

       s "Percy's quite the rowdy one. He frequently gets into fights into fights with the parrots in the palace. Verbally, mind you."

       show hatate laughing at left

       h "Oh no...{w} Truly only the greatest arguments would ensue."

       show satori sighing at right

       s "It got even worse after Utsuho taught the parrots how to swear... It's like hearing an actual underground brawl sometimes, except it's just loud squawking."

       h 'Almost like a tengu brawl too...{w} The environment follows me wherever I go, damn it!'

       show satori smiling at right

       s "Unfortunate."

       show hatate smiling at left

       s "I'm still fond of Percy, though. He can be a handful, but he's quite handsome. He acts very proud, and I like seeing that in my pets."

       show satori smug at right

       s "I also might've named him after a character from one of my favorite books.{w} You know, just maybe."

       h "I'm not at all surprised you're the reading type, heh."

       show satori smiling at right

       s "Definitely. I spend hours reading books every single day.{w} All of these different stories by all of these different authors across Gensokyo and the Outside World... it gets really interesting, you know?"

       h "Yeah I get really sunk into fiction sometimes too.{w} It's just, like, really comfortable and all, you know? So I think it's really neat you've sort left a mark of how its affected you onto a pet you love."

       h "Like, when I started thinking about dodging life around the Tengu Village, I found books and manga to be a pretty great escape from my troubles."

       h "I could never really find other people to talk to about them, unfortunately, but that didn't stop me from enjoying them on my own time."

       show hatate laughing at left

       h "Like, there's this one I read at the time about some magical alien dude dragging this completely normal dude across space, and it was so entertaining and unlike anything I'd experienced at the time."

       s "That sounds quite fun. I haven't read much science fiction myself. Perhaps I could change that someday, since I am constantly on the lookout for more atypical fiction."

       show hatate smiling at left

       h "I could throw a few suggestions after this interview, if you want!"

       s "Consider me interested."

       s "And yeah, I agree that fiction is a wonderful escape from the harshness of reality."

       s "I've gone through plenty of rough times myself, but there's always been these great stories of the right people prevailing to keep me motivated in life."

       h "Yeah, it's exactly like that for me too."

       h "You know, I'm having a lot of fun talking to you, actually.{w} We're more similar than I expected, you know?"

       s "Likewise, this is fun."

       show hatate thinking at left

       h "Oh yeah, we got completely sidetracked. Do you have any other stories about the cockatoo?"

       show satori sighing at right

       s "Well, there's that time he rode a cat into the absolutely incredible mission of... trying to impress another cockatoo, who unfortunately did not reciprocate."

       show hatate frowning at left

       h "Damn. He even brought the noble steed."

       show hatate laughing at left

       h "Well, at least I'm sure this is absolutely the kind of spicy relationship drama my readers would be looking for, right?"

       show satori laughing at right

       s "Surely."

       jump the_birds

label talk_kiwi:

       show hatate smiling at left

       show satori smiling at right

       show image "kwiii.png" at truecenter

       h "So that little kiwi bird of yours, right? She seems uh, really energetic. What's that like to deal with as a pet owner?"

       show satori sighing at right

       s "I've had to changed furniture in several rooms for Kuri, haha."

       show hatate frowning at left

       h "Oh dear."

       show satori tired at right

       s "You see, she's such a little ball of unfiltered energy that she kept constantly tripping around the palace."

       s "Kuri never got that hurt from any of his antics, but I started to realize she needed a bit of help, you know?"

       s "I love her, but she's been one of my most handful pets."

       show hatate smiling at left

       h "I'm glad you've given her some good care. Seems like a really good friend at the end of the day."

       show satori smiling at right

       s "Yes! Very true.{w} Not enough people down in the underground appreciate the idea that animals can be your best friends."

       s "Kuri's very different from what I was used to when I first adopted her, but in sticking it out with the learning process, I learned so many things to appreciate about her."

       s "She's so adorable to play with, for instance! An absolutely fantastic cuddler too."

       show hatate excited at left

       h "Aw. That's so cute!"

       show hatate smiling at left

       s "I'm glad I managed to find her. Kiwi birds are very extant, like many things I've taken under my wing, I really wonder how she even got down here in the first place."

       show satori concerned at right

       s "And well, kiwis aren't exactly really good at defending themselves. Running, sure, but I'd hardly expect one to win a fight."

       s "She could've gotten seriously hurt before I ever laid my eyes on her. I may not have ever met her at all. But she's found somewhere comfortable to be here, and I think that's really nice."

       show hatate frowning at left

       h "Yeah, I've always wondered what the climate for animals must be like down here."

       show satori sighing at right

       s "Awful, most of the time. The underground, especially around Former Hell in particular, is extremely about adaption. If you aren't some magical hell raven, you're basically doomed from the start."

       show satori smiling at right

       s "Really, Kuri is a large example of why I'm a pet owner, I think. I like to view the Palace of the Earth Spirits as a safe haven in a sea of terrible pet owners.{w} Maybe calling myself the one who cares is a bit egotistical, but I think it's true."

       show hatate smiling at left

       h "I don't think I would disagree. This place is way more comfortable to be in than the rest of Former Hell to me."

       s "Really now? Most tengus I've met are quite the partying type."

       h "I'm usually sitting on the sidelines of most parties, haha. Crowds can get kind of too much for me.{w} Maybe I'm not too far from a little bird myself."

       show satori laughing at right

       s "You're certainly tall for one."

       show satori smiling at right

       s "But yeah, I'm glad you're comfortable here."

       h "And I'm happy your pets can feel the same."

       hide image "kwiii.png"

       jump the_birds

label after_the_birdial:

    show hatate smiling at left

    h "Well, those were some very nice fellas of yours!"



    return
