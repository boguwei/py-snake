# Snake
#### Just a Pygame Thing

This is a program to learn Pygame / Python. It's a work in progress... 

---

### How to Play
1. Launch the game by typing `./runGame.bash` from the game dir. 
2. Navigate the Snake using the keyboard. 

  | Key         | Action                |
  | ----------- | --------------------- |
  | w           | move up               |
  | a           | move left             |
  | s           | move down             |
  | d           | move right            |
  | j           | move height down 1    |
  | k           | move height up 1      |
  | g           | grow snake (cheating) |
  | ESC         | quit game             |

The game has 7 height levels mapped to 8 colors. The height of the snake's head 
must match the height of the node to be eaten in order for the snake to eat it. 
In other words, the snake head must match the color of the node to be eaten, in
addition to actually being at the spot on the game screen where the node is. 

Following the same logic, a snake only collides with itself when the color of the
body segments match. 

The height levels are mapped as follows:

| Height Level | Color   |
| ------------ | ------- |
| 1            | RED     |
| 2            | ORANGE  |
| 3            | YELLOW  |
| 4            | GREEN   |
| 5            | BLUE    |
| 6            | INDIGO  |
| 7            | BLACK   |

### Versioning
This game was built using Python v3.5.1 and Pygame 1.9.2a0.
All software was installed using Homebrew 0.9.5 (git revision 11b11)

You can test if Pygame is installed correctly by running `./bouncing_ball/runTest.bash` from the game dir.

