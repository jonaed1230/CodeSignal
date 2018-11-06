# This solution is belongs to this challenge : https://app.codesignal.com/challenge/QTiyM5zk2mHmC8aox
def fallBack(time):
    #finding colon(:)
    colon = time.find(':')
    #program will enter in this loop if time is about single digit(1 - 9)
    if colon == 1:
        #converting string into list
        new_time = list(time)
        #making 1 as different because its about 12 hours
        if new_time[0] == '1':
            new_time[new_time.index('1')] = '12'
            reversed_time = "".join(new_time)
        
        else:
            #indexing first element of list which means single digit hour(2-9) and replacing it with its previous hour
            new_time[new_time.index(new_time[0])] = str(int(new_time[0]) - 1)
            reversed_time = "".join(new_time)
    #program will enter in this loop if time is about double digit(10 - 12)        
    elif colon == 2:
        new_time = list(time)
        #before 12 AM or PM time changes
        if str(''.join(new_time[0:2])) == '12' and str(''.join(new_time[5:7])) == 'PM':
            #adjusted time
            adjusted_time = str(int(''.join(new_time[0:2])) - 1)
            #adjusted AM or PM
            adjusted_period = 'AM'
            #delete old time(hour)
            del new_time[0:2]
            #inserting new time
            new_time.insert(0, adjusted_time)
            new_time.insert(4, adjusted_period)
            #I don't know why its showing PMAM so I've poped it up
            new_time.pop()
            new_time.pop()
            #finally convert customized list into string
            reversed_time = "".join(new_time)
        
        
        elif str(''.join(new_time[0:2])) == '12' and str(''.join(new_time[5:7])) == 'AM':
            adjusted_time = str(int(''.join(new_time[0:2])) - 1)
            adjusted_period = 'PM'
            del new_time[0:2]
            
            new_time.insert(0, adjusted_time)
            new_time.insert(4,adjusted_period)
            new_time.pop()
            new_time.pop()
            reversed_time = "".join(new_time)
            
            
            
        else:
            #grabing first two elements of list which means two digit hour(10 - 12) and replacing it with its previous hour
            adjusted_time = str(int(''.join(new_time[0:2])) - 1)
            #deleting hour digits so we can replace it easily
            del new_time[0:2]
            new_time.insert(0, adjusted_time)
            reversed_time = "".join(new_time)    
    

    #returning 1 hour back time
    return reversed_time 