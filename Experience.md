<h1 align = 'center'> 🎀 The Advent of Code Experience! 🎀 </h1>

***HEY WHAT'S UP***
Welcome to my experience document, where I'm going to write down my experience of participating in Advent of Code (AoC)!
This is my first year doing it, so why not make it memorable?
(*Although, I feel like the magnitude of the code bugs themselves will be memorable enough...*)
**CHRISTMAS CODING!**

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

**Happy Holidays!** ❄️
