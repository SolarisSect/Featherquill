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

    "In the midst of a cold winter's night, a crow tengu rests beneath the soil, with a certain warmth enveloping her."

    "Not just the warmer surroundings of the underground palace she’s visiting, but the hot flash caused by her own anxiety."

    "She stands in front of the door to the room of the palace’s mistress, wanting nothing more than to knock, but not having the courage to do so."

    "It’s silly, she thinks to herself, the atmosphere here is surprisingly lively, so why is she even freezing up like this?"

    "Because of how long it’s been since she last tried interviewing someone?"

    "Because her interview idea itself is silly?{w} Because she might be considered annoying?"

    "Because there’s always that one voice screaming at her that her words aren’t of worth, that she should just quit while she’s ahead."

    "That she’s both not seeing enough of the world yet wasting everyone’s time when she tries? That-"

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

    h "Whoa... I, erm, sorry. I hope I didn't pick a bad time to come."

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

    "Hatate approaches Satori's desk, giving an anxious glance towards the satori's third eye staring right towards her."

    show hatate anxious at left

    h "Uhm, if it's not too much to ask, do you mind pointing that thing away? It's kind of an evasion of privacy, heh..."

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

    s "Oh, you're taking an interest in my pets? Here I was worried you were going to ask some annoying questions about my private life."

    show hatate annoyed at left

    h "Please, I have better things to do than that. I'm more tasteful than some others."

    show satori thinking at right

    s "Hmm...{w} In that case, I'd actually love to take you up on your offer."

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

    "the crane hiding around the garden":
        $ birds_appreciated += 1
        jump talk_crane

    "the stork and her little chick (*^ ω ^)":
        $ birds_appreciated += 1
        jump talk_stork

    "the cockatoo resting beneath an abandoned birdcage":
        $ birds_appreciated += 1
        jump talk_cockatoo

    "that kiwi bird freaking ZOOMING around the place, holy crap":
        $ birds_appreciated += 1
        jump talk_kiwi

    "hmm. i think that's everything?" if birds_appreciated >= 4:
        jump after_the_birdial

label talk_crane:

      show hatate thinking at left

      show satori smiling at right

      show image "crane.png" at truecenter

      h "So when I was poking around your garden, I found this guy hiding in a bush. I managed to lure him out for this picture, though."

      show hatate thinking at left

      h "I'm extremely curious to know how you even have a proper garden down here, but I think I'll hold that question for a little while."

      show hatate smiling at left

      h "What's this bird really like?"

      s "That would be Atlas. As you can see, he's a bit of a shy fellow."

      show satori sighing at right

      s "What he's absolutely not shy about is his appetite, however."

      s "Atlas will truly eat damn near anything you give him, but when we got the garden going? I don't think it's a coincidence he started building a nest there."

      show satori smiling at right

      s "He's lovely when you get to know him though."
      
      s "And his appetite might simply be a part of the constantly changing diets that cranes usually exhibit."

      s "But as I've mentioned, he's mostly settled into the garden."
      
      s "It's where he feels the most comfortable in, and he's never been very sociable either."

      show satori sighing at right

      s "He's only ever really gotten along with one other pet in the palace, out of the many here. Which would be Utsuho."

      show hatate surprised at left

      h "He quite literally picked the most nuclear option?"

      show satori smiling at right

      s "Well, you know that question you were holding about how the garden is even maintainable in the underground like this in the first place?"

      s "Utsuho would be directly responsible for that, thanks to her ability to create artificial, yet accurate suns for the plants to flourish from."

      h "Wait... that actually like, kind of makes sense? In a stupid way, but I get it, you know?"

      show hatate thinking at left

      h "I take it she doesn't just sit there for hours, right?"

      s "Her artificial suns stick around for a long while.{w} She's good at providing lasting power like that."

      s "I'm very glad we can have proper plant life thanks to her. Especially since the other pets adore it all too."

      show satori laughing at right

      s "Of course, Atlas usually gets to most of the berries first."

      show hatate smiling at left

      h "Can't blame him for having his eye on the prize!"

      show hatate thinking at left

      h "I... also wouldn't mind some of those berries right now, quite frankly.{w} I'm getting kinda hungry right now."

      show hatate smiling at left

      h "Do you mind if I take some later?"

      show satori sighing at right

      s "Go ahead."

      hide image "crane.png"

      jump the_birds

label talk_stork:

      show hatate excited at left

      show satori smiling at right

      show image "stork.png" at truecenter

      h "This stork and her chick are absolutely adorable! What's it like looking over a family?"

      s "Ah yes, that's Monokuro and one of her chicks, Banira."

      show hatate smiling at left

      s "It's worth noting that I raised two storks since they were chicks, imported from the mountain around the entrance to the underground."

      s "So just seeing them go on to make a family together has been really sweet for me."

      s "To get onto what it's like looking after a family though, I think I've gotten pretty used to it, since they mostly take care of themselves anyway."

      s "However, I do my best to help provide for the chicks, just to take some of the stress off the parents.{w} And they really are adorable when they're together."

      s "And I remember how fascinating it was watching them build a nest together, constantly providing for each other while waiting for the eggs to hatch."

      s "And when the time came, watching their chicks start to lovingly follow them... It was just so precious for me."

      s "And then those chicks would start to play with the other birds too. That's been absolutely wonderful to observe."

      s "I think it's really reinforced this sense of community I've always loved in regards to raising all of these different animals."

      s "It can get really hard to maintain so many pets... But it's really satisfying at the end of the day, and I wouldn't change a thing."

      show hatate surprised at left

      h "You know, I think that's the perfect note to end this section of the interview on."

      show hatate smiling at left

      h "I think this is just the kind of lovely and inspiring thing my readers would love to see!"

      s "Thank you. I perhaps got a little carried away there, honestly."

      h "Sometimes honesty is like that."

      s "That is definitely true."

      hide image "stork.png"

      jump the_birds

label talk_cockatoo:

       show hatate thinking at left

       show satori smiling at right

       show image "cockatoo.png" at truecenter

       h "Something funny I happened to notice was a cockatoo underneath a rather abandoned birdcage. I take it you like letting your birds fly freely?"

       s "Yes. I find my pets in better spirits when they aren't as restricted around the palace. Most of them behave pretty well regardless."

       show satori laughing at right

       s "This cockatoo, Percy, though... happens to be one of the worse behaved ones, haha. Ironic that you'd find him near an abandoned cage."

       show satori smiling at right

       s "Percy's quite the rowdy one. He frequently gets into fights with the parrots in the palace. Verbally, mind you."

       show hatate laughing at left

       h "Oh no...{w} Truly only the greatest arguments would ensue."

       show satori sighing at right

       s "It got even worse after Utsuho taught the parrots how to swear... It's like hearing an actual underground brawl sometimes, except it's just loud squawking."

       h 'Almost like a tengu brawl too...{w} The environment follows me wherever I go, damn it!'

       show satori smiling at right

       s "Unfortunate."

       show hatate smiling at left

       s "I'm still fond of Percy however. He can be a handful, but he's quite handsome. He acts very proud, and I like seeing that in my pets."

       show satori smug at right

       s "I also might've named him after a protagonist from one of my favorite books.{w} You know, just maybe."

       h "I'm not at all surprised you're the reading type, heh."

       show satori smiling at right

       s "Definitely. I spend hours reading books every single day." 
       
       s "All of these different stories by all of these different authors across Gensokyo and the Outside World... it gets really interesting."

       h "Yeah, I get really sunk into fiction sometimes too." 
       
       h "It's just, like, really comfortable and all, you know?"

       h "So I think it's really neat you've sorta left a mark of how it's affected you onto a pet you love."

       h "Like, when I started thinking about dodging life around the Tengu Village, I found books and manga to be a pretty great escape from my troubles."

       h "I could never really find other people to talk to about them, unfortunately, but that didn't stop me from enjoying them on my own time."

       show hatate laughing at left

       h "Like, there's one manga I read at the time about some kid who literally calls his monster friends into games of sport with a cell phone."

       show hatate smiling at left

       h "And it might sound weird, but it's really entertaining at the end of the day."

       show hatate excited at left

       h "All of the monster designs were so freakin' cool! I loved it!"

       show hatate smiling at left

       s "That sounds quite fun. I've never really found manga to be my thing."
       
       s "But since I am constantly on the lookout for more atypical fiction, maybe it's worth a shot."

       h "I could throw a few suggestions after this interview, if you want!"

       s "Consider me interested."

       s "And yes, I agree that fiction is a wonderful escape from the harshness of reality."

       s "I've gone through plenty of rough times myself, but there's always been these great stories of the right people prevailing to keep me motivated in life."

       h "Yeah, it's exactly like that for me too."

       h "You know, I'm having a lot of fun talking to you, actually." 
       
       h "We're more similar than I expected, you know?"

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

       hide image "cockatoo.png"

       jump the_birds

label talk_kiwi:

       show hatate smiling at left

       show satori smiling at right

       show image "kiwi.png" at truecenter

       h "So that little kiwi bird of yours, right? She seems uh, really energetic. What's that like to deal with as a pet owner?"

       show satori sighing at right

       s "I've had to change furniture in several rooms for Kuri, haha."

       show hatate frowning at left

       h "Oh dear."

       show satori tired at right

       s "You see, she's such a little ball of unfiltered energy that she kept constantly tripping around the palace."

       s "Kuri never got that hurt from any of her antics, but I started to realize she needed a bit of help, you know?"

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

       s "Awful, most of the time.{w} The underground requires adaption, and a lot of creatures who aren't born from the more magical parts of nature simply aren't built for it."

       s "Nor do a lot of people down here, especially around Former Hell, know how to take care of the more fragile critters."

       show satori smiling at right

       s "Which is why Kuri is a large example of why I'm a pet owner, I think." 
       
       s "I like to view the Palace of the Earth Spirits as a safe haven in a sea of terrible pet owners."

       s "Maybe calling myself the one who cares is a bit egotistical, but I think it's true."

       show hatate smiling at left

       h "I don't think I would disagree. This place is way more comfortable to be in than the rest of Former Hell to me."

       s "Really now? Most tengu I've met are quite the partying type."

       h "I'm usually sitting on the sidelines of most parties, heh. Crowds can get kind of too much for me.{w} Maybe I'm not too far from a little bird myself."

       show satori laughing at right

       s "You're certainly tall for one."

       show satori smiling at right

       s "But yes, I'm glad you're comfortable here."

       h "And I'm happy your pets can feel the same."

       hide image "kiwi.png"

       jump the_birds

label after_the_birdial:

    show hatate smiling at left

    show satori smiling at right

    h "Well, those were some very nice fellas of yours!"

    h "I think the readers of the Kakashi Spirit News are absolutely going to love this upcoming article."

    "Or at least, that's what she really, really hoped anyway."

    h "Thank you so much for your time, Satori. This was a wonderful interview."

    s "I appreciate you coming down here. It's rare I have visitors I actually enjoy talking to."

    show hatate laughing at left

    h "I'm glad I could be one of the few."

    show hatate smiling at left

    h "In any case, as much as I'd love to stay, I should really get going and have this article out soon."

    h "I'll be on my way, and I'll uh, grab a snack on the way out."

    show satori thinking at right

    s "Actually, Hatate, before you go..."

    show satori concerned at right

    s "Do you mind if we talk for a bit. There's something I noticed when you came here that bothered me."

    show hatate anxious at left

    stop music fadeout 1.0

    h "Huh?"

    s "It's just, you seemed extremely anxious when you got here. I could catch that you were really worried about being able to get some good material from this."

    h "...!"

    s "Do you need someone to talk to? If you're getting really worked up about your writing, at all."

    s "I feel like I might be able to help if you're willing to confide in me."

    h "I-I don't know... It's just..."

    "But Hatate couldn't help but think to herself; Who else had ever even cared to ask her this?"

    h "I suppose I could like, try talking about it, a bit. Maybe you're right. Maybe it would help."

    s "Talk about as much as you think you need to."

    "Hatate took a long deep breath. Then settled on where to start."

    play music "Bell_of_Avici.mp3"

    show hatate frowning at left

    h "So... uh, I guess it's important to start with the context that I'm pretty young by the standards of a tengu."

    h "I haven't had the hundreds or thousands of years to grab experience on things in comparison to everyone else."

    h "A few years ago, I was finally thrust into the newspaper workforce." 
    
    h "At the time, I was actually pretty excited for it."

    h "Because to me, I could finally follow in the footsteps of my idol at the time..."

    h "Tell me, Satori. Have you ever been unfortunate enough to meet Aya Shameimaru?"

    show satori sighing at right

    s "A few times, sadly."

    show hatate annoyed at left

    h "Yeah. That sounds about right."

    show hatate frowning at left

    show satori frowning at right

    h "Back then, I always found her newspaper really exciting." 
    
    h "But occasionally I'd notice something wrong slip through the cracks based on my own research."

    h "When I felt like I had a decent grasp of this whole writing thing, I tried going up to her and giving her my honest feedback."

    h "I was polite, I wasn't trying to be antagonistic, and I just wanted to help someone I really respected at the time."

    h "She ignored every piece of advice I gave her.{w} Every single one.{w} And put me down for it."

    h "She said my work was awful, when I tried to give her the benefit of the doubt in regards to the problems I had with hers."

    h "And that just, really deflated me at the time."

    show hatate annoyed at left

    h "I've always been trying to push my newspaper to some level of actual notoriety, but it never gets anywhere with the way that I do things."

    h "But I don't want to just mindlessly put bait in every title.{w} I don't want to just focus on what's trendy."

    h "I just... Want to talk about the little things in the world I've grown to love." 
    
    h "... And apparently that's not good enough."

    show hatate frowning at left

    h "And I just feel so burnt out and anxious recently."

    h "I have a lot worse social anxiety than a majority of people around me, I can't just make connections easily in the same way that everyone else can."

    h "And it makes me question what I'm even supposed to do, besides slam my head against the wall every day until something magically works."

    h "Until I finally write something I'm proud of that gets people's attention."

    s "I see. That's a lot to take in."

    s "Well... Let's start with this question, before I get into anything further."

    s "Do you truly enjoy writing at the end of the day?"

    h "Yes."

    s "Do you view it as an escape, in the same way reading does?"

    show hatate anxious at left

    h "... Sometimes."

    show satori sighing at right

    s "Then it seems like to me that your problem is that you forgot how to enjoy writing."

    show satori frowning at right

    s "You're gonna need to take a step back for yourself here."

    s "Are you writing for yourself, or are you writing to raise an arbitrary number?"

    s "You might not have a large following at the end of the day, but what matters is that the people who do read what you have to say care about it."

    s "Didn't you just say a bit ago about how you thought your readers were going to love what you had to show?"

    s "Was that just you pulling a face for your own sake?"

    h "..."

    show satori sighing at right

    s "Okay, I perhaps maybe went a touch too far there."

    h "You didn't.{w} It's the honest truth and you were right to say it."

    show satori frowning at right

    s "Alright.{w} Regardless, you see my point here, right?"

    s "You do have confidence about what you're doing somewhere, perhaps you should be paying more attention to it."

    s "Stop trying to please bad actors." 
    
    s "Stop trying to make a number grow as if it's the only sign of your skill."

    s "Focus on making what you want to create at the end of the day."

    s "And if you feel that you must appease someone, focus on the people who aren't just trying to drag you down."

    s "There's an extreme difference between valuable criticism and unnecessary hatred." 
    
    s "You need to start figuring out where that line is defined."

    s "If you can learn to keep yourself happy with what you do, you can find that spark again."

    s "It won't come instantly, and it may not even come for awhile."

    s "But you can get there, you just have to calm down and try."

    show hatate surprised at left

    h "..."

    h "I-I suppose you're right, huh."

    s "Take it all from someone who once learned how to write as a coping mechanism for their troubles."

    s "I can tell you love what you do deep down, and I understand that desire to prove yourself as well."

    s "So don't let the latter consume you to the point you lose the spark for the former."

    s "I can't help too much more than that without having your writing directly in my hands, but..." 
    
    s "I hope any of this was useful to you."

    show hatate smiling at left

    h "I think it really was. Thank you."

    h "It's kind of really rare that people actually try to help me with something."

    h "I'll try and step back for a few days." 
    
    h "See if I can find the wind for my wings again."

    h "And when I'm ready, well, I'll try and make something I'm proud of."

    h "I cannot stress how much I've loved seeing what I have today."

    show satori smiling at right

    s "If what I do can inspire anybody, I'm truly honored."

    h "Again, thank you so much for everything." 
    
    h "The pictures, the interview, the advice, all of it."

    h "I really should be heading on my way...{w} But I'll try and make the best of what's to come."

    show satori laughing at right

    s "That's the spirit!"

    show satori smiling at right

    s "Thank you for coming down here, Hatate. I hope we can meet again soon."

    h "I wish the same! See you around, Satori. Have a good night."

    s "Same to you."

    hide satori
    hide hatate

    stop music fadeout 1.0

    "Hatate was going to have to spend awhile figuring out exactly what to do from here.{w} Maybe it wasn't even worth planning out the exact details."

    "But wherever her life and career may go from here."

    "She was ready to soar."


    return
