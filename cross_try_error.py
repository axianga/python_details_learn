#10.13    try: except 发现错误，排除错误。
try:
    print('Hello,myheart!')
    printerrortest("This is wrong test!")
except Exception as er:
    print("Error state beginning:")
    print(er)
    print("Error state ending !")
