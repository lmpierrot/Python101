# Marc Pierrot
# February 28, 2022,
# analyze a network for vulnerabilities
# write a Python program that should test the given host, and it should generate a list of
# all the TCP Open ports within the range of 1 to 1025.

import socket
import datetime

name = input("Please enter your full name: ")
print("Hello!" + name)
print("***************Welcome to our Port Scanner*************")


fl_tpt = open("port's scan file.txt", "w")
fl_tpt.write("Welcome to the scanner-dome.--..--..--..--..-*-.\n\n")

target_name = input("Enter the host that you want to scan please: ")
target_ip = socket.gethostbyname(target_name)

"""just_checking = socket.gethostbyaddr(target_ip)
print(str(target_ip) + " : " + str(just_checking))"""

print(target_ip)


fl_tpt.write("Scanning the target: {}\n\n".format(target_name))

starttime = datetime.datetime.now()
fl_tpt.write(str(starttime) + "\n")
print(starttime)

openports = []
count = 0
i = 1

while i <= 1025:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target_ip, i))
    if status == 0:
        print("{}:{} is open to check!".format(target_ip, i))
        fl_tpt.write(str(target_ip) + " : " + str(i) + " is open")
        fl_tpt.write("{}:{} is open to check!\n".format(target_ip, i))
        openports.append(i)
        count += 1

    elif status == 10060:
        print("{}:{} is closed - Status code: {} This is the reason this port is closed".format(target_ip, i,
                                                                                                status))
        fl_tpt.write("{}:{} is closed - Status code: {} This is the reason this port is closed".format(target_ip, i,
                                                                                                       status))
    elif status == 10061:
        print("{}:{} is closed - Status code: {} This is the other reason this port is closed".format(target_ip, i,
                                                                                                      status))
    elif status == 6660:
        print("{}:{} is closed - Status code: {} This is the other reason this port is closed".format(target_ip, i,
                                                                                                      status))
    elif status == 6669:
        print("{}:{} is closed - Status code: {} This is the other reason this port is closed".format(target_ip, i,
                                                                                                      status))

    else:
        print("{}:{} is closed - Status code: {}".format(target_ip, i, status))

    i += 1


endtime = datetime.datetime.now()
fl_tpt.write("\n" + str(endtime) + "\n")
print(endtime)

total_time = endtime - starttime
fl_tpt.write("This is the total time taken for the scan: " + str(total_time) + " The total number of open ports wa s: "
             + str(count))
print(total_time)

fl_tpt.close()

print("thank you" + name + "for using our port's scan bye!")
