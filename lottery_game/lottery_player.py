# player for the start_game function in Lottery class
class LotteryPlayer:

  def __init__(self, name) -> None:
    self.name = name
    self.extracted = set()
    self.count = 0
