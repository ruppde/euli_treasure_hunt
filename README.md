# Euli Treasure Hunt

Euli is not a computer game but a tool which helps you set up a real life treasure hunt: Decrypting secret writings, solving Python crackmes and using ultra violett pocket lights to follow hidden arrows to the treasure chest with the sweets. (Can also be used for creating e.g. junior capture the flag hacking competitions, escape rooms at home, mystery geocaches or scavenger puzzle hunts). Kids love treasure hunts and there's a reason why parents organize them usually only once per year for the birthday party: It's just too much work. Unless you use Euli Treasure Hunt. The effort is reduced to printing the generated documents and follow the instructions to hide the puzzles in the home.

To prepare the game, the game operator (usually the parents) have to print out and hide puzzles. Solving these leads the players from one to another until they finally find the treasure (also hidden by the game operator, usually some sweets).

## Gameplay

Here's a simplified example of gameplay, difficulty 3rd grade in school (adjustable):
The players get an envelope with a secret note for them. It contains a hint: If they encounter text in a secret code, it always starts with "Top secret!". So if they figure out the pattern of the encryption of these two words, they can easily decrypt the rest of the message. The initial note reads:

```opT ecrets! heT extn essagem si iddenh ni oury argestl ookingc otp.```

By searching for "Top secret" in the first two words, you can recognize, that just the first letter was moved to the last position (a basic transposition cipher). Using that knowledge, the rest of the sentence can be "decrypted" and the players can search for the next stage in their largest cooking pot.

Here they find a locked treasure chest and another message with a printed QR code:
![QR code](readme_example_qr.png "QR code")

Scanning it gives a hint, that another QR is hidden in the middle. Covering the outer QR code with paper enables them to read the inner QR code, which tells them the location of the next stage.

All further puzzles are chained up to the final location of the key or combination to unlock the treasure, hurray! 

If you want to see it in more detail, look at on one of these example games. They're even ready to print and start playing: [Games in varying difficulties, number of players and languages](examples_list.md)

## Available puzzles

All kinds of puzzles from the library crypto puzzles (<https://github.com/2d4d/crypto_puzzles>) can be used. Most of them can "cracked" without prior knowledge, tools or boring explanations. Finding the pattern of "Top secret!" is sufficient.

#### a) Transposition ciphers

* Moved whitespace: ```To pSecr et!T heCookie sA reHidd enI nTh eRe dB owl!```
* Randomize middle of words: ```Top setrce! The coekios are hieddn in the red bolw!```

#### b) Substitution ciphers

* Upside down every 2nd word: ```Top ¡ʇǝɹɔǝs The sǝᴉʞooɔ are uǝppᴉɥ in ǝɥʇ red ¡ꞁʍoq```
* Leet speak: ```T0p $3cr3t! Th3 c00k13$ @r3 h1dd3n 1n th3 r3d b0wl!```
* Camelcase: ```tOp sEcReT! tHe cOoKiEs aRe hIdDeN In tHe rEd bOwL!```
* Characters to numbers: ```20,15,16, 19,5,3,18,5,20,!, 20,8,5, 3,15,15,11,9,5,19, 1,18,5, 8,9,4,4,5,14, 9,14, 20,8,5, 18,5,4, 2,15,23,12```
* Characters to roman numbers: ```XX,XV,XVI, XIX,V,III,XVIII,V,XX,!, XX,VIII,V, III,XV,XV,XI,IX,V,XIX, I,XVIII,V, VIII,IX,IV,IV,V,XIV, IX,XIV, XX,VIII,V, XVIII,V,IV, II,XV,XXIII,XII!```
* rot13: ```Gbc frperg! Gur pbbxvrf ner uvqqra va gur erq objy!```

#### c) Steganography (hidding information in other information)

* First letter of words contain the message (Like an Acrostic): ```tunnel orange perfect sabre empire computer ring empire tunnel ! tunnel hobbit empire computer orange orange kangaroo internet empire sabre antelop ring empire hobbit internet dolphin dolphin empire nose internet nose tunnel hobbit empire ring empire dolphin bug orange wardrobe lumber !```
* Numbers inserted: ```T61o61p5s87e14c55r48e37t0!4T0h66e28c64o66o29k87i64e89s18a11r10e73h23i62d37d87e14n58i85n63t50h54e96r74e53d18b92o10w7l10!18```
* This stegosaurus (original by R.Millward) hides the numbers 603:
```
                         .       .
                        / `.   .' \
                .---.  <    > <    >  .---.
                |    \  \ - ~ ~ - /  /    |
                 ~-..-~             ~-..-~
             \~~~\.'                    `./~~~/
              \__/                        \__/
               /                  .-    .  \
        _._ _.-    .-~ ~-.       /       }   \/~~~/
    _.-'6  }~     /       }     {        ;    \__/
   {'__,  /      (       /      {       /      `. ,~~|   .     .
    `''''='~~-.__(      /_      |      /- _      `..-'   \\   //
                / \   =/  ~~--~~{    ./|    ~-.     `-..__\\_//_.-'
               {   \  +\         \  =\ (        ~ - . _ _ _..---~
               |  | {   }         \   \_\
              '---.0___,'       .3___,'       
```


#### d) Crackme programs
 
A crackme is a small (python) program that contains a secret message, but won't show it until the player has understood the code, found the obstacle and removed it.  See crypto puzzles (<https://github.com/2d4d/crypto_puzzles>) for an examples.

## Including your own puzzles or gadgets

The generated documents are in docx format so they can be further adapted with any word processor to your needs. You can also include your own puzzles and gadgets, for example:
* Puzzle boxes
* The contrib directory contains scripts to e.g. insert QR-codes into videos or integrate Lego Mindstorms robots running [ev3dev](<https://www.ev3dev.org/>). It's a great plattform for real life puzzles: Full blown Debian in a small and robust package, battery powered (can be hidden almost anywhere) and lots of hardware options like motors, LEDs, speaker, sensors, ... which can be programmed using Python. But Raspis work nearly as well. Beware: Kids that just opened a puzzle box will start with removing the SD card from the EV3 or Raspi on first sight. Secure with plenty of tape.
* Cryptex
* Put a puzzle in a water proof bag, that into a storage box with water and deep freeze it
* Hide a clue next to a mobile phone, they have to call to find it by following the ring tone

You can also add atmosphere by customize the theme, playing music or make the kids found their own detective agency.

## Examples

The following link contains 22 generic games generated for varying number of players, grades and languages. They can be directly downloaded and played without installing Euli. If there are more than 2 players they can form groups and cooperate. Or you install Euli and create your own game.
[generic example games](examples_list.md)

## Video chat mode

The last two games in the example list are for 15 players and are designed to be played via video chat (e.g. Jitsi or Zoom) from different locations. Very handy for kids birthday parties in Corona times (succesfully tested with 13 kids. Of course this needs the cooperation of all the parents of the guests because they have to hide all the stages.). Players have to cooperate to find hidden codes in all locations, enter them into a webserver to simultationsly learn the location of the treasures (hidden in the same place in all locations.)

General tips for running the game via video chat:
* Start out with at least one hour of general video chat until everybody is familiar with the system. Show them, that you can mute everybody (if it gets too noisy) and how they can unmute themselves.
* Ask them to check out the private chat with each other.
* If some kids have problems with the connection, propose to look for a place with better wifi coverage.
* Tell them to turn down background noise like music.
* If kids ask for help, don't tell the answer but ask where they're stuck and push them in the right direction.

## Final words

There's no minimum age to play but kids should be able to read fluently. Younger kids might form a group with older ones.

Ideas and contributions are always welcome! (Especially a web gui for configuration is missing ...)
