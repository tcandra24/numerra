from models.history_item import HistoryItem

class History:
  def __init__(self):
    self.histories: list[HistoryItem] = []
      
  def show(self):
    print('================HISTORY==================')
    for history in self.histories:
        print(f"{history.param1} {history.operator} {history.param2} = {history.result}")
    print('=========================================')

  def add_history(self, item: HistoryItem):
    self.histories.append(item)