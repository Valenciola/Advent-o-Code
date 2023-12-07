<h1 align = 'center'> 🎀 The Advent of Code Experience! 🎀 </h1>

***HEY WHAT'S UP***
Welcome to my experience document, where I'm going to write down my experience of participating in Advent of Code (AoC)!
This is my first year doing it, so why not make it memorable?
(*Although, I feel like the magnitude of the code bugs themselves will be memorable enough...*)
**CHRISTMAS CODING!**

[**TODAY'S EXPERIENCE**](https://github.com/Valenciola/Advent-o-Code/blob/main/Experience.md#day-2---12223)

---

### Day 1 - 12/1/23

Today's challenge was to translate a bunch of random lines with numbers in them into **calibration numbers**.
For each line, I needed to extract the numbers from each string, convert each string to the first and last numbers in each string (which is the **calibration number**), and then add up all of those numbers.

***PART 1:***
Coded in Python. I went with Python because it would be much easier for me to manipulate strings.
*C++ won't let me do real string stuff. I haven't revisited JS in a while. And C... well...*
So I made four different functions to go through each string step-by-step and decode it. I accidentally made it convert some of the text numbers into integers, which I didn't need to do for part 1, but once I skipped the initial decoding, everything was great! And I was proud of it. Until...

***PART 2:***
I think most people looked at it and was like *"WHAT THE ACTUAL WHAT IS THIS LIKE WHY AND HOW AND WHAT"*
But like I was already translating numbers so I wasn't scared. Some of the numbers shared letters with other numbers. With some critical thinking, the answer was pretty simple: translate each number to the integer and the letter that's shared at the end. Worked amazingly! But there was still a bug. I completely forgot to consider that the letters are also shared at the start of the word. I was also decoding in numerical order, meaning that some numbers were translated before others, which messed up the code.
BUT! Just when I was about to be super mad at AoC for doing weird stuff, I remembered... TOP LETTER! So I made the words translate first and last, meaning I made "two" become "t2o". If you think about, it's a pretty good solution!

Some friends of mine had a lot to say about part 2, but we got it in the end! The thing about being a programmer is that problem solving really makes you have to *think*. And we all thought and we all solved! Go us!

Now I wonder what's in store for tomorrow's puzzle...

---

### Day 2 - 12/2/23

**The story thus far:** I have been launched from a trebuchet (sort of against my will, but what an experience), and I landed on a chilly sky island that was also nearly snowless! The place was called *Snow Island* (which is ironic at the moment). An Elf met me where I landed to debrief me on what's going on, but it's a bit of a walk to where I need to be, so he asked if I'd like to play a game in the meantime.

Today's challenge was about this game, which involved of bag of red, green, and blue cubes. The Elf would grab a handful of cubes and show them to me, which I would then record. After a few rounds (if you think of 100 as a few), the Elf asked me a few questions about my data. So here came the string parsing and the stats! I used Python today.

***PART 1:***
The goal was to see which of the games in my sample input would be possible if there were only 12 red cubes, 13 green cubes, and 14 blue cubes. Then, I was to add up all of the game IDs that were possible, and input the sum as the answer. For this solution, I decided to simplify each line by changing the big words (removing the "Game" and turning green into "g" and the like), and then I parsed through the simplified string using a loop that would read each character and make decisions based on that. If any value for the g's, b's, or r's went over the limit, the loop would break and would return 0 instead of the game's ID. It took a bit of time for me to figure it out (mainly because I didn't break this one into as many steps), but I got it!

***PART 2:***
Part two was only slightly more difficult. This time, the Elf wanted to know what the fewest number of cubes needed to be for each color, for each game. So, I needed to find the highest number of cubes in each game, out of all of the drawings. That one was a little bit more challenging because my string parsing kept erasing the character markers I was using to separate the cube colors. I think future me will read the code and understand... though maybe near-future me should spend some time commenting the code. Anyway, I was *very* happy to complete today's challenge!

My friends didn't break a sweat over this challenge, but they *also* waited until midnight so they could start working on the puzzle. So when we first looked at it, most of us had a heart attack. And I went to sleep. And the rest of them puzzled it out. So now, I'm tied for 6th place in the private leaderboard.

Tomorrow's Sunday, meaning I'm definitely not getting any speed points. But another day means another puzzle--and who knows what's in store!

---

### Day 3 - 12/4/23

**The story thus far:** I've gotten up to a gondola lift, which the Elf tells me will take me up to the water source. This is as far as the elf can take me, so I'm on my own again... or so I thought. I get into a gondola, but it's not moving. It turns out that it's broken. I notice the engineer Elf there, and he tells me that the gondolas aren't working because there's a gear missing. I offer to help, and he explains that if I can add up the part numbers of the engine schematic, we can find which one is missing. Today's code is in Python once again.

***PART 1:***
The first step was to read through the schematic to find the part numbers. In the input, each number that touches a symbol (even diagonally) is a part number. I started pretty late on this day's challenge, and it took me *quite* a while to piece it together. It was about 11 at night when I solved the first part. I decided to store the entire file's content into a single string variable, because I figured that would help me with positioning (because there were 140 characters in each line). This one took multiple steps: I searched by symbol and had it see if there were any numbers around the symbol. Then, any number was investigated to read the entire number in between the .'s. Then I had to record each of these numbers and add it together. I don't exactly remember everything that went into it, but the code is pretty readable-ish, so I could probably go back and figure it out.

***PART 2:***
The next day, I addressed part 2. This one's goal was to find each **gear ratio** (a.k.a, any symbol that is connected to more than one number, and the product of those numbers). This one didn't take much because my original code was already separating numbers by symbols. The trick was to include a separater in the array for the part numbers (a '|'), and then have it read. The first time I did it, I got a bug because I didn't realize that single numbers weren't gears. In that case, I ended up just setting the total product to zero so it didn't add anything. I was getting an answer that was too high at first, but once I figured it out (it took some testing in Bye.py with the example code), I got the gold star! **YAY!**

My friends had some mixed feelings about this challenge, but they all found ways to solve it (and they're all *vastly* different solutions). A lot of us are starting to think that AoC is starting to get overly complicated, but it's only day three, so maybe we might find some relief in future challenges. I'm trying to remain optimistic.

Now I gotta try Day 4's challenge and hope I can still get some good points, even though I did D3P2 in the same day! (and no I'm not looking to see what's in store this time. I might not like it)

---

### Day 4 - 12/4/23

**The story thus far:** I've ridden the gondola up to another island! This island is much warmer compared to the others. When I get there, I notice an Elf surrounded by a pile of cards. The Elf comes up to greet me and I ask about the water sources. The Elf doesn't know about that, though, and explains that the **gardener** would know more. Apparently I'm on **Island Island**, a floating island, and I need to get to the island where the gardener is, which is surrounded by water. Luckily, the Elf has a boat and will let me borrow it... *if* I help the Elf figure out what the cards, which are scratch cards, are worth. Each card contains a list of both winning numbers and given numbers, which are separated by a **vertical bar** ('|').

***PART 1:***
The Elf has figured out that each card might have some given numbers that match the winning numbers, and for each number that matches, the first number makes the card worth 1 point, and each following number doubles the value. So, given my card input, the goal was to find the value of all of the cards and add that up. So, the main thing was to interpret each line with the card input and separate it into the winning numbers and the given numbers. Then I stored them in separate arrays (both of which would be cleared in each repition). This involved reading and adding the characters to the winnings up until the vertical bar, and then add the rest to the givens. Then I had to clean up each array and turn the characters into full numbers (and then clean it up again to get rid of the extra empty strings). After I had my numbers, I had to compare the winning numbers to the given numbers and see where there were matches (since each line didn't repeat numbers). Then I could correctly parse each amount of matches (so the first is 1, and the others double the amount), and store the values in another array. Then I added up everything in the array and we were all good!

***PART 2:***
In part 2, it turns out that directions were on the back of each card. It turns out that for each winning number, you get copies of more scratch cards. Basically, if I had four winning numbers on the first scratch card, then I get one copy each of the next four cards (2, 3, 4, 5). With this in mind, I could reuse my code to find the matches, which would be the winning numbers. Now, instead of parsing for values, I needed to add these copies. This was simple, since I could use a for loop and add one to each number in the array (which represents the number of copies for each card). However, it turns out that I had to factor in the copies too. So, the solution was for me to repeat the same array extension multiple times to account for each copy, and then I would total that up!

My friends didn't think this challenge was too hard, and most of them got it. In my opinion, this one was pretty straightforward and simple to think about!

So now, we're about to be a fifth of the way through Advent of Code. Hopefully the challenges don't become too difficult, or I might have to start sacrificing stars... which I'm very determined not to do! Let's also try to complete daily challenges within the same day...

---

### Day 5 - 12/5/23

**The story thus far:** I took the boat over to the island within **Island Island** to meet with the gardener there. I ask him what he knows about the fact that **Snow Island** isn't receiving any water. It turns out that the water had been turned off because there was no sand to filter it with, but as the Elf thinks through this, he realizes that he's had the water off for *way* too long. This is because he was busy trying to make sure everyone has food, so he forgot to check why the island had stopped receiving sand. So he asks *me* to go check it out by taking a ferry to the place where I can go investigate the lack of sand. Just ask quickly, he gives me another task: read the latest **Island Island almanac**, which lists the seeds that need to be planted and contain information for how to convert the seed numbers to their attributes (like temperature and location).

***PART 1:***
Given my puzzle input, my job was to find the lowest location number out of all of the seeds I was given. Now, let me just say this: the numbers were *ridiculous*. So big and crazy... But luckily, after some time, I managed to make one function that would convert a number to a different number based on which list was inputted as a parameter. It took a lot of true/false and if-statements and everything... But at some point, I finally got it. I don't exactly know how I got up to that point, but I did...

***PART 2:***
...Is technically not done. I apparently made a program that brute-forces all of the seeds. See, it turns out that the seed input was a starting seed number and then a range, meaning that I have about a billion seeds to process. And I haven't yet gotten an answer because the compilers I've tried so far keep running out of memory. So now I gotta find some way to use less memory... Maybe I'll try to simplify things into one variable, rather than storing things. I've got some ideas for how to do it... But, for now, we're on a silver star.

**Happy Holidays!** ❄️
