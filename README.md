# Cyberpunk 2077 Hacking Minigame Assistant

![GitHub](https://img.shields.io/github/license/Veinar/cp2k77HackingAssistant?style=flat-square)

FYI:
**Cyberpunk 2077 is registered trademark of CD Project S.A.**  
See: https://twitter.com/CDPROJEKTRED/status/850022540042960896

This project main goal is to help players solving in-game minigames called "hacking" or "protocol breaching".

## Technologies
Project is created with:
* Python 3.9.0 :heart:

## Description

### Minigame description 
Protocol breaching is mini-game in Cyberpunk 2077. Three main elements of this riddle are:

![Screenshot from game](/docs/images/screen_from_game.png)

* **Code Martix** - *it's matrix that holds values from which player must pick and fill buffer in order to complete sequences. Selecting values is restricted by two rules:*

    1. Picking must be done in order. Value must be choosen from column or row and it must be done alternately. Value selection in column marks next row (as active) from which player will choose next element.
    
    2. Once picked value (on fixed matrix position, not every) cannot be selected again.

* **Sequences** - *are basically things that you want to place in buffer. In most cases there will be more than one sequence to complete. The biggest catch is to place values picked from matrix in buffer without* **breaking sequence itself** *But to wipe away those tears, sequences can be part of other avaliable sequences.* :sunglasses:

* **Buffer** - *this is only placeholder for picked values (from Code Matrix), during game it will extend it's size. Main purpose of it is to set how much values player can choose*

### This solution (project) description

Algorithm to solve this riddle has basically three steps:

1. Generate possible combinations (with length of buffer size).   

:speech_balloon: **This is covered by functions:** *generate_combinations(), ~~permute_sequences()~~*

2. Check if there is:
    * **best solution** - *that covers every avaliable given sequence.*
    * **required sequences solution** - *that covers sequences that user mark as wanted.*

:speech_balloon: **This is covered by functions:** *get_best_combination(), get_required_combination()*

3. Generate possible matrix traversal paths (with being obedient to picking rules - mentioned before).
> :warning: There is a catch, for larger buffer size code processes more and more paths - it consumes RAM very aggressively :ram: . 

:speech_balloon: **This is covered by functions:** *traverse_matrix()*

4. Check if solution (from step 2) is covered in any path, and return every or only one solution.

:speech_balloon: **This is covered by functions:** *compare_paths_and_combinations()*

## Installation

Installation is as simple as cloning this repo to your local computer :muscle:   
This piece of software was written without any additional packages :heavy_check_mark:

## Tests

Automatic unit tests will be implemented in future :bell:

## Usage

Coming soon...
For now see: script.py (in root dir)

### **Applies to larger matrix and buffer:**
*In "miscellaneous" directory there are pregenerated traverse paths (paths.7z) for larger matrix and buffer. Use them rather than generate every run - it's easier to read file than generate paths. Use 7zip (or simillar tool) to decompress.* :v:

**Filenames are are basically:**   
> **m**(atrix)**Size** - **b**(uffer)**Size**.

**For example:**

| Filename 	| Matrix size 	| Buffer size 	| File size   (decompressed) 	| Paths 	|
|-	|-	|-	|-	|-	|
| m8b8.txt 	| 8 x 8 	| 8 	| ~354 MB 	| 5 503 680 	|
| m6b8.txt 	| 6 x 6 	| 8 	| ~22 MB 	| 331 200 	|

## Plans

- [x] Minimal readme
- [x] Minimal functionality (with manual fill of matrix and sequences)
- [ ] Code cleanup
- [ ] (Maybe) Optimization
- [ ] Unit testing
- [ ] (Maybe) Reading from screen (also called OCR)
- [ ] Make proper readme

## Contribution

When contributing to this repository, please first discuss the change you wish to make via issue. 
Feel free to add something up, or optimize solution! :purple_heart:

## Additional info (Something from author)

> I know that level of python is barely enough to get running, please let me infrom you that this is my first bigger project in this programming language :hamster:   
I'm very thankful for any hints and code enchantments :pray: