# ECM1400 - Programming - Coursework 2
**Author: Emre Acarsoy**

---

NOTES

should generate attack take in the board?? (is it against what is outlined in the doc?)

# Features

### 1. Singleplayer

This battleships game supports singleplayer gameplay (with no opponent).  

### 2. Against AI opponent

I am currently implementing multiplayer functionality.  

---

# Build

### 1. Singleplayer 

To **specify which ships you would like** to have in the singleplayer game, please configure the **`config/battleships.txt`** file.  
Example file: 
```
s1:1
s2:3
s3:4
s4:2
```
This configuration will place 4 ships on the board, of sizes 1, 3, 4, and 2 respectively.

### 2. Against AI opponent

In order to **specify your ship placement** when playing against the AI opponent, please configure the **`config/placements.json`** file.  
Example file:
```
{
  "Aircraft_Carrier":["0","0","h"],
  "Battleship":["2","2","v"],
  "Cruiser":["4","4","h"],
  "Submarine":["6","6","v"],
  "Destroyer":["8","8","h"]
}
```

---
