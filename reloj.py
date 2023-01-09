import os
import time

while True:
    os.system("cls")
    print("Reloj: ", time.strftime("%Y:%m%H:%M:%S",time.gmtime()))
    time.sleep(5)



# horas, minutos, segundos = 0
# ampm = ""

# while True:

#     if ampm == "am":
#         ampm = "pm"
#     else:
#         ampm = "am"

#     for x in range[11]:
#         horas += 1

#         for 0 in range[59]:
#             minutos += 1

#             for 0 in range[59]:
#                 os.system("cls")
#                 segundos += 1
#                 print("hora",ampm, horas, minutos, segundos)
#                 time.sleep(1)