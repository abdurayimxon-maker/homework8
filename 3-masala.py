import datetime

bugun = datetime.date.today()
yil = bugun.year
mustaqillik = datetime.date(yil, 9, 1)

if bugun > mustaqillik:
    mustaqillik = datetime.date(yil + 1, 9, 1)

farq = mustaqillik - bugun
print(f"Keyingi Mustaqillik bayramiga {farq.days} kun qoldi.")