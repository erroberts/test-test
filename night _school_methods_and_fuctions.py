
    ##sports= 'soccer,basketball,football,tennis'
###sports.insert(2,'rugby')
##
###print(sports)
###badSports = sports.pop()
###sports.remove('basketball')
###print('I enjoy {0} but {1} is just not something i care for'.format(sports,badSports))
####sports.split(',')
####print(sports.split(','))
##def nice_message():
##    return 'hello david, how are you doing today?'
##    print(
##
##blah = nice_message()
##print(blah)
def master_yoda(new_sentence):
   # new_sentence= input('please insert saying:')
    st = new_sentence.split()
    rt = st[::-1]
    return ''.join(rt)

#master_yoda = reverse('i am home')
text1 = master_yoda('how is your day')

print(text1)
                       


