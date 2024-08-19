import threading
import time

# Глобальная переменная для количества врагов
total_enemies = 100
lock = threading.Lock()


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        global total_enemies
        days = 0
        print(f"{self.name}, на нас напали!")

        while total_enemies > 0:
            with lock:
                if total_enemies > 0:
                    total_enemies -= self.power
                    days += 1
                    print(f"{self.name} сражается {days}..., осталось {total_enemies} воинов.")

            time.sleep(1)  # Пауза в 1 секунду

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


# Создание и запуск 2 потоков на основе класса Knight
knight1 = Knight(name="Sir Lancelot", power=10)
knight2 = Knight(name="Sir Sherek", power=30)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Битва окончена!")