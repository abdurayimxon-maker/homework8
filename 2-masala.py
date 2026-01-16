import datetime

yil = int(input("Yil: "))
oy = int(input("Oy: "))
kun = int(input("Kun: "))

tugilgan_sana = datetime.date(yil, oy, kun)

bugun = datetime.date.today()
farq = bugun - tugilgan_sana

print(f"{farq.days} kun o'tdi")