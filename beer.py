word = "bottles"
for beer_num in range(99,0,-1):
    print(beer_num,word,"of beer on this wall.")
    print(beer_num,word,"of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beer_num == 1:
        print("No more bettles of beer on this wall.")
    else:
        new_num = beer_num - 1
        if new_num==1:
            word = "bittle"
        print(new_num,word,"of beer on this wall.")
    print()