
import pandas as pd
import numpy as np
n = np.zeros([4, 4], dtype=int)
water = np.zeros([4, 4], dtype=bool)
if __name__ == "__main__":

    harvest = 0
    history = []
    for day in range(1,11):
        print(n)
        while np.count_nonzero(water) < 3:
            try :
                ans = str(input("Row or next"))
                if ans == "next":
                    break
                l = int(ans)
                f = int(input())
            except ValueError:
                print("Invalid input")
                continue
            if l < 0 or l>= 2 or f<0 or f>=3:
                print("Not cordinats")
                continue
            if water[l, f] == True:
                print("This plot is already watered")
            else:
                water[l, f] = True
        print(np.count_nonzero(water))
        n[water] += 1
        water.fill(False)
        riqe = n >= 2
        h = np.count_nonzero(riqe)
        print(h)
        harvest += h
        history.append({"day": day,"harvest": h})
        n[riqe] = 0
    pandas_history = pd.DataFrame(history)
    history_mean = pandas_history["harvest"].mean()
    has = pandas_history["harvest"] > 0
    pandas_history.to_csv("harvest.csv",index=False)
    print(pandas_history[has])
    print(history_mean)
    print(harvest)
    print(n)
    print(water)
    print(history)
    if harvest >= 12:
        print("You saved the colony!")
    else:
        print("The colony ran out of food")