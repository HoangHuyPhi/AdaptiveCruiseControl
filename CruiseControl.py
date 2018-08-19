old_print = ""
while True:
    file = open("test.txt")
    text = file.read()
    file.close()
    text = text.split("\n")
    for n, i in enumerate(text):
        text[n] = i.split(" = ")

    current_velocity = int(text[0][1])
    target_velocity = int(text[1][1])
    object_distance = float(text[2][1])
    threshold_velocity = target_velocity/2
    threshold_minimum = threshold_velocity-10
    threshold_maximum = threshold_velocity+10

    very_slow = 0
    slow = 0
    target = 0
    fast = 0
    if object_distance <= 0:
        print("You are dead")
        break
    if object_distance <= (current_velocity/10):
        to_print = "BRAKE"
    else:
        if current_velocity >= 0 and current_velocity < threshold_minimum:
            very_slow = 100
            slow = 0
            target = 0
            fast = 0
        elif current_velocity >= threshold_minimum and current_velocity < threshold_maximum:
            #fuzzy logic start
            slow = int(5*current_velocity-(5*threshold_minimum))
            very_slow = 100-slow
            target = 0
            fast = 0
            #fuzzy logic end
        elif current_velocity >= threshold_maximum and current_velocity < target_velocity -5:
            very_slow = 0
            slow = 100
            target = 0
            fast = 0
        elif current_velocity >= target_velocity-5 and current_velocity <= target_velocity:
            very_slow = 0
            slow = 0
            target = 100
            fast = 0
        elif current_velocity > target_velocity:
            very_slow = 0
            slow = 0
            target = 0
            fast = 100
        to_print = "Very Slow:"+str(very_slow)+"%\tSlow:"+str(slow)+"%\tTarget:"+str(target)+"%\tFast:"+str(fast)+"%"

    if to_print != old_print:
        old_print = to_print
        print(to_print)



