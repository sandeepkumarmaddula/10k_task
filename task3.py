#24 type conversions
print(float(10))                 # int -> float
print(int(10.8))                 # float -> int
print(str(100))                  # int -> str
print(int("100"))                # str -> int
print(str(5.5))                  # float -> str
print(float("5.5"))              # str -> float
print(bool(10))                  # int -> bool
print(bool(0))                   # int -> bool
print(int(True))                 # bool -> int
print(int(False))                # bool -> int
print(tuple([1, 2, 3]))          # list -> tuple
print(list((1, 2, 3)))           # tuple -> list
print(set([1, 2, 2, 3]))         # list -> set
print(list({1, 2, 3}))           # set -> list
print(set((1, 2, 2)))            # tuple -> set
print(tuple({1, 2, 3}))          # set -> tuple
print(list("Python"))            # str -> list
print("".join(['P','y','t']))    # list -> str
print(tuple("ABC"))              # str -> tuple
print(set("HELLO"))              # str -> set
print(list({'a':1,'b':2}))       # dict -> list
print(tuple({'a':1,'b':2}))      # dict -> tuple
print(set({'a':1,'b':2}))        # dict -> set
print(dict([('a',1),('b',2)]))   # list -> dict