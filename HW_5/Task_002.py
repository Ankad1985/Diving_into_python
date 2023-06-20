# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

names = ['Андрей', 'Анастасия', 'Надежда']
bets = [100, 200, 150]
bonuses = ['10.25%', '5%', '8.75%']

result = {name: bet * float(bonus.strip('%')) /
          100 for name, bet, bonus in zip(names, bets, bonuses)}

print(result)
