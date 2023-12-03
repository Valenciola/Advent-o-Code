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

**Happy Holidays!** ❄️
