print(" 1. Phone Book")
print(" 2. Messages")
print(" 3. Chat ")
print(" 4. Call Register")
print(" 5. Tones")
print(" 6. Settings")
print(" 7. Call Divert")
print(" 8. Games")
print(" 9. Calculator")
print(" 10. Reminders")
print(" 11. Clock")
print(" 12. Profiles")
print(" 13. SIM services")

num1 = int(input("\nselect option: "))

if num1 == 1:
    print(" Phone book ")
    print("\t1. Search")
    print("\t2. Service Nos")
    print("\t3. Add Name")
    print("\t4. Erase")
    print("\t5. Edit")
    print("\t6. Assign tone")
    print("\t7. Send b' Card")
    print("\t8. Options")
    print("\t9. Speed Dials")
    print("\t10. Voice Tags")

    pb1 = int(input("\nselect option: "))

    if pb1 == 1:
        print("\nSearch ")
    elif pb1 == 2:
        print("\nService Nos ")
    elif pb1 == 3:
        print("\nAdd name ")
    elif pb1 == 4:
        print("\nErase ")
    elif pb1 == 5:
        print("\nEdit ")
    elif pb1 == 6:
        print("\nAssign tone ")
    elif pb1 == 7:
        print("\nSend b' card ")
    elif pb1 == 8:
        print("1.Type of view ")
        print("2.Memory status ")
    elif pb1 == 9:
        print("\nSpeed Dials ")
    elif pb1 == 10:
        print("\nVoice Tags")

if num1 == 2:
    print(" Messages ")
    print("\t1. Write messages")
    print("\t2. Inbox")
    print("\t3. Outbox")
    print("\t4. Picture messages :)")
    print("\t5. Templates")
    print("\t6. Smileys")
    print("\t7. Message settings")
    print("\t8. Info service")
    print("\t9. Voice mailbox number")
    print("\t10.Service command editor")

    message = int(input("\nselect option: "))
    if message == 1:
        print("\n Write messages ")
    elif message == 2:
        print("\n Inbox ")
    elif message == 3:
        print("\nOutbox")
    elif message == 4:
        print("\nPicture messages ")
    elif message == 5:
        print("\nTemplates ")
    elif message == 6:
        print("\nSmileys :) ")
    elif message == 7:
        print("Message settings")
        print(" \t1. Set 1")
        print("\t\t1. Message centre number ")
        print("\t\t2. Message sent as ")
        print("\t\t3. Message validity ")

        set = int(input("\nselect option: "))
        if set == 1:
            print("\nMessage centre number ")
        elif set == 2:
            print("\nMessage sent as")
        elif set == 3:
            print("\nMessage validity")
            print(" \t2. Common  ")
            print(" \t\t1. Delivery reports")
            print(" \t\t2. Reply via same centre")
            print(" \t\t3. Character support")

if num1 == 3:
    print(" \n Chat ")

if num1 == 4:
    print("4. \nCall register ")
    print("\t1. Missed calls")
    print("\t2. Recievd calls")
    print("\t3. Dialed numbers")
    print("\t4. Erase recent call list")
    print("\t5. Show call duration")
    print("\t6. Show call costs")
    print("\t7. Call cost settings ")
    print("\t8. Prepaid credit")

    register = int(input("\nselect option: "))

    if register == 1:
        print("\n Missed calls ")
    elif register == 2:
        print("\n Recieved calls")
    elif register == 3:
        print("\nDialed numbers")
    elif register == 4:
        print("\nErase recent call lists ")
    elif register == 5:
        print("\n4. Show call duration ")
        print("\t1. Last call duration ")
        print("\t2. All calls' duration ")
        print("\t3. Recieved calls' duration ")
        print("\t4. Dialled calls' duration ")
        print("\t5. Clear timers ")

        duration = int(input("\nselect option: "))
        if duration == 1:
            print("\n Last call duration ")
        elif duration == 2:
            print("\n All calls' duration")
        elif duration == 3:
            print("\nRecieved calls' duration ")
        elif register == 4:
            print("\nDialled calls' duration ")
        elif register == 5:
            print("\nClear timers ")

    elif register == 6:
        print("\n6. Show call costs ")
        print("\t1. Last call cost ")
        print("\t2. All calls' cost ")
        print("\t3. Clear counters ")

        cost = int(input("\nselect option: "))
        if cost == 1:
            print("\nLast call cost ")
        elif cost == 2:
            print("\nAll calls' cost")
        elif cost == 3:
            print("\nClear counters")

    elif register == 7:
        print("\n7. Call cost settings ")
        print("\t1. Call cost limit ")
        print("\t2. Show costs in ")

        reg = int(input("\nselect option: "))
        if reg == 1:
            print("\nCall cost limit ")
        elif reg == 2:
            print("\nShow costs in ")

    elif register == 8:
        print("\n Prepaid credit  ")

if num1 == 5:
    print("5. Tones ")
    print("\t1. Ringing tone")
    print("\t2. Ringing volume")
    print("\t3. Incoming call alerts")
    print("\t4. Composer")
    print("\t5. Message alert tone")
    print("\t6. Keypad tones")
    print("\t7. Warning and game tones ")
    print("\t8. Vibrating alert")
    print("\t9. Screen saver")

if num1 == 6:
    print(" Settings ")
    print("\t1. Call settings")
    print("\t2. Phone setting")
    print("\t3. Security settings")
    print("\t4. Restore factory settings")

    callSet = int(input("\nselect option: "))
    if callSet == 1:
        print(" Call settings ")
        print("\t1. Automatic redial")
        print("\t2. Speed dialing")
        print("\t3. Call waiting options ")
        print("\t4. Own number setting")
        print("\t5. Phone line in use")
        print("\t6. Automatic answer")

        callSet1 = int(input("\nselect option: "))
        if callSet1 == 1:
            print("\n Automatic redial ")
        elif callSet1 == 2:
            print("\n Speed dial")
        elif callSet1 == 3:
            print("\n Call waiting options ")
        elif callSet1 == 4:
            print("\n Own number setting ")
        elif callSet1 == 5:
            print("\n Phone line in use ... ")
        elif callSet1 == 6:
            print("\n Automatic answer ")

    elif callSet == 2:
        print(" Phone settings ")
        print("\t1. Language")
        print("\t2. Cell info display")
        print("\t3. Welcome note ")
        print("\t4. Network selection")
        print("\t5. Lights")
        print("\t6. Confirm SIM service actions")

        phoneSet = int(input("\nselect option: "))

        if phoneSet == 1:
            print("\n Phone settings ")
        elif phoneSet == 2:
            print("\n Language")
        elif phoneSet == 3:
            print("\n Welcome note ")
        elif phoneSet == 4:
            print("\n Network selection ")
        elif phoneSet == 5:
            print("\n Lights ")
        elif phoneSet == 6:
            print("\n Confirm SIM service actions ")

    elif callSet == 3:
        print(" Security settings ")
        print("\t1. PIN code request")
        print("\t2. Call barring service")
        print("\t3. Fixed dialing ")
        print("\t4. Closed user group")
        print("\t5. Phone security")
        print("\t6. Change access codes")

        security = int(input("\nselect option: "))

        if security == 1:
            print("\n PIN code ")
        elif security == 2:
            print("\n Call barring service")
        elif security == 3:
            print("\n Fixed dialing")
        elif security == 4:
            print("\n Closed user group ")
        elif security == 5:
            print("\n Phone security ")
        elif security == 6:
            print("\n Change access codes ")

    elif callSet == 4:
        print(" \n Restore factory settings ")

if num1 == 7:
    print(" \nCall Divert ")

if num1 == 8:
    print(" \nGames ")

if num1 == 9:
    print(" \nCalculator ")

if num1 == 10:
    print(" \nReminders ")

if num1 == 11:
    print(" Clock ")
    print("\t1. Alarm clock")
    print("\t2. Clock settings")
    print("\t3. Date settings")
    print("\t4. Stop watch")
    print("\t5. Countdown timer")
    print("\t6. Auto update of date and time")

    clock = int(input("\nselect option: "))
    if clock == 1:
        print("\n Alarm clock ")
    elif clock == 2:
        print("\n Clock settings")
    elif clock == 3:
        print("\n Date setting ")
    elif clock == 4:
        print("\n Stop watch ")
    elif clock == 5:
        print("\n Countdown timer ")
    elif clock == 6:
        print("\n Auto upadate of date and time ")

if num1 == 12:
    print(" \nProfiles ")

if num1 == 13:
    print(" \nSim services ")
