def check_ps(a, q, space, o, reset, t, level):
    COMPI = False
    CASUAL = False
    STRESS = False
    RL = False
    CARE = False
    AGG = False

    exp = 0

    if t <= level * 40 and level>2:
        exp += 10
        rs = reset
        print("Compitative")
        if rs >= 6:
            RL = True

    elif t <= level * 40 + level * 10:
        exp += 8
        rs = reset - 2
        if rs < 10:
            CARE = True
        if a > 15:
            CASUAL = True

    elif t <= level * 40 + level * 20:
        exp += 6
        rs = reset - 4
        CASUAL = True
    elif t <= level * 40 + level * 30:
        exp += 4
        rs = reset - 6
        CASUAL = True
    elif t <= level * 40 + level * 40:
        exp += 3
        rs = reset - 8
    else:
        exp += 2
        rs = 1

    if exp > 7:
        if o > 15 or a > 15:
            STRESS = True
        if space > 30 or q > 10:
            AGG = True

    elif exp > 5:
        if o > 30 or a > 30:
            STRESS = True
        if space > 50 or q > 16:
            AGG = True

    elif exp > 2:
        if o > 60 or a > 60:
            STRESS = True
        if space > 70 or q > 20:
            CARE = True

    else:
        if level>=3 and t< 240:
            COMPI = True
    if reset>24:
        RL = True
    if a+o > 40:
        print("likes to Explore")

    if COMPI:
        print("Compitative")
    if CASUAL:
        print("Casual gaming")
    if STRESS:
        print("Gets stressed eaisly")
    if RL:
        print("Restless")
    if CARE:
        print("Very carefull while doing something")
    if AGG:
        print("Aggressive nature")

    if level==1:
        print("Give up too eaisly")
    elif level==2:
        print("Gave up and frustrated")
    elif level==3:
        print("Its seems Doable")
    elif level==4 :
        print("Dedicated Chalanger")

