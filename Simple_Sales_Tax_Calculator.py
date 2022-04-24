#Kenneth_Onwubuya_301141637
#Sales_Tax_Calculator

def UserInput():
    data = []
    while True:
        x= float(input('Price of item: '))
        if x == 0:
            break
        else:
            data.append(x)
    return data

def findtax(data):
    return round(sum(data)*.06,2)

def findtotal (data,salestax):
    return sum (data)+salestax

def printdata(data,salestax,total):
    print ('total: ',round(sum(data),2))
    print ('sales tax: ',salestax)
    print ('your total after tax: ', round(total,2))

if __name__ == "__main__":

    while True:
        print('enter items, or 0 to end session')
        data = UserInput()
        salestax = findtax(data)
        total = findtotal(data,salestax)
        printdata(data,salestax,total)
        choice = str(input('more items? (y/n): '))

        if choice == 'n':
            print('Thank you, goodbye!')
            break