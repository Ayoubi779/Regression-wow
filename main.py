###regression wow
import matplotlib.pyplot as plt
import math 
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
##functions and methods required for regression
def ListPow2(A):
    B =[]
    for i in A:
        B.append(i**2)
    return B
def mean(A):
    return sum(A)/len(A)
def meanTwoVar(A,B):
    total = 0
    for i in range(0,len(A)):
        total = total + A[i]*B[i]
    return total/len(A)
def COV(X,Y):
    MeanX = mean(X)
    MeanY = mean(Y)
    covWn = 0
    for i in range(0,len(X)):
        covWn = covWn + (X[i]-MeanX)*(Y[i]-MeanY)
    return covWn/len(X)
def COV2(X,Y):
    return meanTwoVar(X,Y) - mean(X) * mean(Y)
def stddev(A):
    return math.sqrt(mean(ListPow2(A)) - mean(A)**2)
def coeffCorr(X,Y):
    return COV(X,Y)/(stddev(X)*stddev(Y))
def coeffCorr2(X,Y):
    return COV2(X,Y)/(stddev(X)*stddev(Y))
def clean(A):
    B = []
    for x in A:
        try:
            B.append(float(x))
        except (ValueError,TypeError):
            if x == 'ND':
                B.append(x)
            else:
                print(f"Warning: Invalid input '{x}'")
                B.append("ND")
            continue
    return B

#simple linear regression
def reg(data):
    sY = stddev(data["Y"])
    sX = stddev(data["X"])
    if (sX == 0):
        print("Invalid Data")
        return None
    if (sY == 0):
        return {"b":0,"a": mean(data["Y"])}
    row = coeffCorr(data["X"], data["Y"])
    b =  row * (sY/sX)
    a = mean(data["Y"]) - b*mean(data["X"])  
    return {"b": b, "a": a}
def reg2(data): #not safe, do not use
    b = coeffCorr2(data["X"], data["Y"]) * (stddev(data["Y"])/stddev(data["X"]))
    a = mean(data["Y"]) - b*mean(data["X"])  
    return {"b": b, "a": a}

def Prd(data,info):
        YPrd,XPrd = {},{}
        for x in data["X"]:
            YPrd[x] = info["a"] + info["b"] * x
        for y in data["Y"]:
            XPrd[y] = (y - info["a"]) / info["b"]
        return {"Y":YPrd,"X": XPrd}
    
def line(data,info):
    y ={}
    for x in data:
        y[x]  = info["a"] + info["b"] * x
    return y
##collect data
X = []
Y = []

i = None

print("Type '...' to stop or 'ND' for no data")

while i != "...":
    i = input(f"Enter X{len(X)}: ")
    X.append(i)
    
i = None
print("Type '...' to stop or 'ND' for no data")

while i != "...":
    i = input(f"Enter Y{len(Y)}: ")
    Y.append(i)
##clean data

#convert to float
X = clean(X)
Y = clean(Y)
Ypopped = []
Xpopped = []
for i in range(len(X)-1,0,-1):
    if X[i] == 'ND':
        X.pop(i)
        try:
            Ypopped.append(Y.pop(i))
        except:
            continue
for i in range(len(Y)-1,0,-1):
    if Y[i] == 'ND':
        Y.pop(i)
        try:
            Xpopped.append(X.pop(i))
        except:
            continue
#match sizes
diff = len(X) - len(Y)
if diff > 0:
    for i in range(len(X)-1,len(X)-diff-1,-1):
        Xpopped.append(X.pop(i))
elif diff < 0:
    for i in range(len(Y)-1,len(Y)+diff-1,-1):
        Ypopped.append(Y.pop(i))
##merge
data = {"X":X,"Y":Y}
del X,Y
##perform regression
info = reg(data)
if info is None:
    raise SystemExit("Regression could not be performed.")
    
YPrd = line(Xpopped, info)
del Xpopped,Ypopped
#print info on console
clear()
print(f"ŷ = {info['b']:.3f}x + {info['a']:.3f}")
cov = COV(data["X"],data["Y"])
stddevX = stddev(data["X"])
stddevY = stddev(data["Y"])
if stddevX == 0 or stddevY == 0:
    r = None
    R2 = None
else:
    r = coeffCorr(data["X"], data["Y"])
    R2 = r**2
print(f"Covariance: {cov}")
print(f"Standared Deviation X: {stddevX}")
print(f"Standared Deviation Y: {stddevY}")
print(f"Determiantion: {R2}")


# Regression visualization
plt.figure(figsize=(9, 6))

# Scatter plot
plt.scatter(data["X"], data["Y"],color="blue", label="Observed values")

plt.scatter(YPrd.keys(), YPrd.values(),color="orange", marker="X", label="Predicted missing Y")

# Regression line
plt.axline(
    (mean(data["X"]), mean(data["Y"])),
    slope=info["b"],
    linewidth=2,
    color="red",
    label=f"ŷ = {info['b']:.3f}x + {info['a']:.3f}"
)
# Labels and information
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Linear Regression")

plt.legend()
plt.grid(True, alpha=0.3)

plt.show()



    