from PIL import Image
import numpy as np

FILE_PATH = "images/" 

def twoPowers(x):
    return [2**i for i in range(x+1)]

def isEven(x):
    return x % 2 == 0

def horizontalStripeData(x):
    arr = np.zeros(x*x)
    for i in range(len(arr)):
        if isEven(i):
            arr[i] = 255
    return arr

def verticalStripeData(x):
    arr = horizontalStripeData(x)
    square = arr.reshape((x,x))
    vertical = square.transpose()
    return vertical.flatten()
    

def checkeredData(x):
    even_white = np.zeros(x)
    odd_white = np.zeros(x)
    for i in range(x-1):
        if i % 2 == 0:
            even_white[i] = 255
            odd_white[i+1] = 255
    arr = np.array([])
    for i in range(x/2):
        arr = np.append(arr,even_white)
        arr = np.append(arr,odd_white)
    return arr

def xdata(x):
    final_arr = np.array([])
    for i in range(x):
        row = np.zeros(x)
        row[i] = 255
        row[x-i-1] = 255
        final_arr = np.append(final_arr, row)
    return final_arr
        

def main():
    # change this param to change the number of images generated
    for i in twoPowers(5):
        im = Image.new('L',(i,i))
        # a = verticalStripeData(i)
        # a = horizontalStripeData(i)
        # a = checkeredData(i)
        a = xdata(i)
        im.putdata(a)
        filename = FILE_PATH+str(i)+"x"+str(i)+"-test.jpg"
        im.save(filename,"JPEG")
main()


        
        
