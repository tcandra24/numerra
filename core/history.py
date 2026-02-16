from models.history_item import HistoryItem
from .storage import push_data, show_data

class History:
  def __init__(self):
    self.histories: list[HistoryItem] = []
      
  def show(self):
    print('=============== HISTORY =================')
    json_histories = show_data()
    if len(json_histories) > 0:
      for history in json_histories:
        print(f"{history['param1']} {history['operator']} {history['param2']} = {history['result']}")
    else:
      print("============ HISTORY KOSONG =============")
    print('=========================================')

  def add_history(self, item: HistoryItem):
    json_histories = show_data()
    self.histories = [HistoryItem(**history) for history in json_histories]

    self.histories.append(item)
    push_data([history.__dict__ for history in self.histories])

  def clear(self):
    self.histories = []
    push_data([])