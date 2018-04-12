# cli-game
### A python powered cli game to play and defeat few well-konwn legends.


We always have a fantasy on competing with legends in some field other than in which they have expertize. Like 
we would love to compete "Steve Jobs" in a game of "cricket" or "Alpachino" in a "coding" competition. 

This fantasy game will make your dream true. You build a player according to the qualities you possess from a given
set and then compete with legends. You will surprised to see that you are equally good as them at your field of expertize.
This will surely boost you morale. :p

    How to Play:
    #################################
    1. Open you command line terminal
    2. git clone https://github.com/kharsh77/cli-game
    3. cd cli-game
    4. python game.py (make sure you have python2.7 pre-installed)
    5. Follow instructions and enjoy the game.

    
    GAME RULES
    #################################

    The game is divided into five steps:
      1. Build Your Character (Replicate your strengths)
      2. Choose a Door to go to the Ring (Your opponent waits behind)
      3. Give a Fight in the Ring
      4. Advance to the Next Door  
      5. Game Terminates (When you get exhausted)
    
    Build your character
    ********************
      Rules:
      -------
      1. Your character can have few qualities and a power value for each quality.
      2. A quality can have power value as 0,1,2.
      3. Your player can have total power less than or equal to 5.
      4. While building your player, you can customize the powers values for any given quality.

      Assign power value:
      -------------------
      1. You are shown names of all qualities your character can have.
      2. Enter a value for a prompt for each quality your character can have which will be say, 0,1 or 2.
      3. Sum of all powers should be equal or less than say,5.
      4. If the sun exceeds the total of 5, then you need to re-enter the values.
      5. After building your character you can proceed to play the game.
    
    Choose a Door
    **************
      1. After your character is ready, you need to choose a door to get into the ring.
      2. Behind each door there is a opponent waiting for you to compete.

    In the Ring
    *************
      1. Your player competes with a opponent for a given task.
      2. If you win in a particular task, the excess power you have wrt to your opponent gets added to your energy.
      3. If you loose in a particular task, your energy get reduced accordingly.
    
    Advance to the next door (Game continues...)
    *********************************************
      1. You are directed to choose the next door if you have positive energy left after a fight.
    
    Game over
    **********
      1. If your energy become non-positive after a fight, then the game terminates.
      2. Your achievements are shown thereafter.



