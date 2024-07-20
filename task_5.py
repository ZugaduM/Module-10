from multiprocessing import Manager, Process


class WarehouseManager:

  def __init__(self) -> None:
    self.manager = Manager()
    self._data = self.manager.dict()

  def process_request(self, request: list):
    for item in request:
      if item[1] == "receipt":
        if item[0] in self._data:
          self._data[item[0]] += item[2]
        else:
          self._data.update({item[0]: item[2]})
      elif item[1] == "shipment":
        if item[0] in self._data and self._data[item[0]] > 0:
          self._data[item[0]] -= item[2]
        elif self._data[item[0]] < 0:
          self._data[item[0]] = 0

  def run(self, requests: list):
    if __name__ == "__main__":
      proc = Process(target=self.process_request, args=(requests, ))
      proc.start()
      proc.join()


# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [("product1", "receipt", 100), ("product2", "receipt", 150),
            ("product1", "shipment", 30), ("product3", "receipt", 200),
            ("product2", "shipment", 50)]

# Запускаем обработку запросов
manager.run(requests)

# Выводим обновленные данные о складских запасах
print(dict(manager._data))
