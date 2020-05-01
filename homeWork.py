# num = int(input("Enter a number "))

# print((num%5==0 and num%3==0 and "Clarusway") or (num%5==0 and "Way") or (num%3==0 and "Clarus") or (num%3!=0 and num%5!=0 and num))


# ----------------------------------------

# Write a program that converts milliseconds into hours, minutes, and seconds.

# If the hours calculated is 0, it should not be shown in the output.
# If the minutes calculated is 0, it should not be shown in the output.
# If the seconds calculated is 0, it should not be shown in the output.
# If the milliseconds is greater than 1000, remainder milliseconds should not be shown in the output.
# If milliseconds given is less than 1000, only milliseconds should be shown in the output.
# Do not use if statements in your code.
# Output should always be string in the format shown in the following examples.
# Examples
# milliseconds = 2001 --> 2 second/s
# milliseconds = 60011 --> 1 minute/s
# milliseconds = 122011 --> 2 minute/s 2 second/s
# milliseconds = 3661011 --> 1 hour/s 1 minute/s 1 second/s
# milliseconds = 7322011 --> 2 hour/s 2 minute/s 2 second/s
# milliseconds = 7200011 --> 2 hour/s
# milliseconds = 555 --> just 555 millisecond/s


#  millis=int(input("Enter time in milliseconds "))
millis=999
seconds=(millis/1000)%60
seconds = int(seconds)
minutes=(millis/(1000*60))%60
minutes = int(minutes)
hours=(millis/(1000*60*60))
hours = int (hours)

# print ("%d hour %s minutes/s %s second/s %d millisecond/s" % (hours, minutes,seconds, millis))
# print ("%d hour %s minutes/s %s second/s" % (hours, minutes,seconds, millis))

print(("%d hour/s" % (hours)) * (hours > 0) + " %d minutes/s" % (minutes) * (minutes > 0) + " %d seconds/s" % (seconds)*(seconds>0) or "just %d millisecond/s" % millis )

print(f'{hours} hour/s'*(hours != 0) + f' {minutes} minute/s'*(minutes != 0) + f' {seconds} second/s'*(seconds != 0) or f'just {milliseconds} millisecond/s')

# print(f'{hours} hour/s' * (hours != 0))
