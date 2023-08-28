def to_seconds(hour, minute, second):
    return (hour * 60 * 60) + (minute * 60) + second

def read_hour():
    return int(input('Enter hour: '))

def read_minute():
    return int(input('Enter minute: '))

def read_second():
    return int(input('Enter second: '))

def time_elapsed(start_time, finish_time):
    time = finish_time - start_time
    hour = time // 3600
    minute = time % 3600 // 60
    seconds = time % 3600 % 60
    
    return f'{hour} hours {minute} minutes {seconds} seconds.'

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))