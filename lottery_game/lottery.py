import random
class Lottery:
  winner:bool = False
  winning_numbers:set = set()

  #this create a set of 15 winning numbers 
  @staticmethod
  def extract_winning_numbers()->None:
    while len(Lottery.winning_numbers) < 15:
      r:int = random.randint(1, 90)
      Lottery.winning_numbers.add(r)
    print("Numeri Vincenti:", Lottery.winning_numbers, "\n-------------------------------------")


  @staticmethod
  def start_game(players)->None:

    if not len(players): print("Non Ci sono Players"); exit(); 
    
    while not Lottery.winner:
      
      for player in players:
        
        r:int = random.randint(1, 90)
        player.count += 1

        if Lottery.winning_numbers.__contains__(r):
          player.extracted.add(r)
          print(F"{player.name} -> Trovato numero!:", r)
          print(F"Mancano {3 - len(player.extracted)} numeri per vincere!")
          print(F"{player.count} estrazioni effettuate.")
          print("---------------------------------------")

        if len(player.extracted) == 3: Lottery.winner = True 
        if Lottery.winner: print(F"{player.name} ha vinto! Estrazioni effettuate: {player.count}"); exit()
        random.seed(None)

