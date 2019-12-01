f = int(input('farenheit:'))
c = int(input('celcius: '))

def convertc(c):
   return c / 5 * 9 + 32
def convertf(f):
    return (f-32) / 9 * 5
print('celcius para farenheit: ',convertc(c))
print('farenheit para celcius; ', convertf(f))