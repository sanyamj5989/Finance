

from scipy.stats import norm
import math

def blackscholescall(S, K, r, SD, t):
    d1 = (math.log(S/K) + t*(r + ((SD**2)/2)))/SD*math.sqrt(t)
    d2 = d1 - SD*math.sqrt(t)
    return ((S * norm.cdf(d1,0,1)) - ((K * math.exp(-r*t)) * norm.cdf(d2,0,1)))

def blackscholesput(S, K, r, SD, t):
    d1 = (math.log(S/K) + t*(r + ((SD**2)/2)))/SD*math.sqrt(t)
    d2 = d1 - SD*math.sqrt(t)
    return (((K * math.exp(-r*t)) * norm.cdf(-d2,0,1)) - S * norm.cdf(-d1))

def Delta(Us,Ds,Cu,Cd):
    return (Cu-Cd)/(Us-Ds)

def deltahedgingcall (S, K, r, Us, Ds, t):
    Cu = Us - K
    Cd = 0
    d = Delta(Us,Ds,Cu,Cd)
    NetInflow = Ds*d
    x = NetInflow*math.exp(-r*t)
    f = -x + (d*S)
    return f


def deltahedgingput (S, K, r, Us, Ds, t):
    Cu = 0
    Cd = K - Ds
    d = Delta(Us, Ds, Cu, Cd)
    NetInflow = Us*d
    x = NetInflow * math.exp(-r*t)
    f = -x + (d * S)
    return f

    
print("Select Model:")
print("1. Black Scholes Model Call Pricing")
print("2. Black Scholes Model Put Pricing")
print("3. Delta Hedging Call Pricing (C-, S+)")
print("4. Delta Hedging Put Pricing (P-, S-)")

while True:
    choice = input("Enter choice (1-4): ")
    
    if choice == '1':
        S = float(input("Enter the spot price: "))
        K = float(input("Enter the strike price: "))
        r = float(input("Enter the risk free rate: "))
        SD = float(input("Enter the volatility: "))
        t = float(input("Enter the time to maturity (in yeras): "))
        result = blackscholescall(S, K, r, SD, t)
        print("Call Price:", result)
        
    if choice == '2':
        S = float(input("Enter the spot price: "))
        K = float(input("Enter the strike price: "))
        r = float(input("Enter the risk free rate: "))
        SD = float(input("Enter the volatility: "))
        t = float(input("Enter the time to maturity (in yeras): "))
        result = blackscholesput(S, K, r, SD, t)
        print("Put Price:", result)

    if choice == '3':
        S = float(input("Enter the spot price: "))
        K = float(input("Enter the strike price: "))
        r = float(input("Enter the risk free rate: "))
        Us = float(input("Enter the upper price: "))
        Ds = float(input("Enter the lower price: "))
        t = float(input("Enter the time to maturity (in years): "))
        result = deltahedgingcall(S, K, r, Us, Ds, t)
        print("Call Price:", result)


    if choice == '4':
        S = float(input("Enter the spot price: "))
        K = float(input("Enter the strike price: "))
        r = float(input("Enter the risk free rate: "))
        Us = float(input("Enter the upper price: "))
        Ds = float(input("Enter the lower price: "))
        t = float(input("Enter the time to maturity (in years): "))
        result = deltahedgingput(S, K, r, Us, Ds, t)
        print("Put Price:", result)
