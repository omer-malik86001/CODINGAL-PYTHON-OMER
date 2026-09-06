# RUN A FOR LOOP FOR NUMBERS 1 TO 25 ONLY PRINT EVEN NUMBERS SKIP ODD NUMBERS

for i in range(1,26):
    # the percent operator is to find the remainder
    if i % 2 == 1:
        continue

    print(i)