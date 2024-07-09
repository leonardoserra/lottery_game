# lottery game, there are 15 winning numbers, each player will extract a number 
# till the first that found 3 numbers win!
# pass a list of LotteryPlayer in the start_game() function

#start the program and see who will win

from lottery import Lottery
from lottery_player import LotteryPlayer

players:list[LotteryPlayer] = [
  LotteryPlayer('Leonardo'),
  LotteryPlayer('Fabio'),
  LotteryPlayer('Federico'),
  LotteryPlayer('Enrico'),
  LotteryPlayer('Sara'),
]

Lottery.start_game(players)
