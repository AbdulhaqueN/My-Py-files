def posorneg(num):
    if num>0:
        return "Positive"
    elif num==0:
        return "Neither Positive nor Negative"
    else:
        return "Negative"
print(posorneg(-5))