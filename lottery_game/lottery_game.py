from lottery import Lottery
from lottery_player import LotteryPlayer

Lottery.extract_winning_numbers() #creata set n vincenti

players:list[LotteryPlayer] = [
  LotteryPlayer('Leonardo'),
  LotteryPlayer('Fabio'),
  LotteryPlayer('Federico'),
  LotteryPlayer('Enrico'),
  LotteryPlayer('Sara'),
]

Lottery.start_game(players)