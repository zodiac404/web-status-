import requests
from termcolor import colored

print(colored("""
       _  _      _  _      _      
|  | |_  |)    /_`  |   /\   |  |  | 
|/\| |_ |_)    ./  |  /~~\  |  \_/ 

#Coded By Zodiac.Hacker
""", "red"))

url1 = input("Enter link : ")

url2 = requests.get(url1)

print('\n')
print("1 - status code : ")
print("2 - source : ")
print("3 - cookies : ")
print("4 - content : ")
print('\n')

x = input('Enter: ')

if x == '1':
    print(url2.status_code)
elif x == '2':
    print(url2.text)
elif x == '3':
    print(url2.cookies)
elif x == '4':
    print(url2.content)
else:
    print("Error")