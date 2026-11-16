import time, datetime

start = time.time()
input("Press Enter as fast as you can!")
print(f"{time.time() - start:.3f} seconds")

today = datetime.date.today()
birthday = datetime.date(2027, 3, 14)
print((birthday - today).days, "days to go")
print(today.strftime("%A %d %B %Y"))
