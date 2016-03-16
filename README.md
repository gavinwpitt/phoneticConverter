# phoneticConverter
Program used to convert serial numbers into the NATO phonetic alphabet

Small program I developed for my job at a computer repair center.
Will often have to call coworkers in another building, or call users, and give them product keys/serial numbers

We were encouraged to use the NATO phonetic alphabet to avoid confusion, but I was notoriously bad at doing so.

So, I created this small script.

Can be run by typing:
  python3 phoneticConverter.py test123 123test ...
  
to get output:
  TANGO  ECHO  SIERRA  TANGO  ONE  TWO  THREE  
  ONE  TWO  THREE  TANGO  ECHO  SIERRA  TANGO  
  .  .  .  

Or, you can run:
  python3 phoneticConverter.py
  
which will initiate an endless loop to type continous input.
  
