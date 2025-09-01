t=('Bob','Alice','Max','Mihir')
t2=tuple(item for l in t for item in l)
print("combined string tuple:",t2)