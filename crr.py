"""import math
import numpy as np

def max(a, b):
    return a if a > b else b


def CRR(n,Spot,K,T,q,r,v,type):
    num_inputs = len(Spot)
    EC_results = np.zeros(num_inputs)
    EP_results = np.zeros(num_inputs)
    AC_results = np.zeros(num_inputs)
    AP_results = np.zeros(num_inputs)

    for input_idx in range(num_inputs):
        S = np.zeros((n + 1, n + 1))
        EC = np.zeros((n + 1, n + 1))
        EP = np.zeros((n + 1, n + 1))
        AC = np.zeros((n + 1, n + 1))
        AP = np.zeros((n + 1, n + 1))

        dt = T / n
        u = math.exp(v * math.sqrt(dt))
        d = math.exp(-v * math.sqrt(dt))
        p = (math.exp((r - q) * dt) - d) / (u - d)

        # Build the Tree
        for j in range(n + 1):
            for i in range(j + 1):
                S[i][j] = Spot[input_idx] * math.pow(u, j - i) * math.pow(d, i)

        # Compute terminal payoffs
        for i in range(n + 1):
            EC[i][n] = max(S[i][n] - K[input_idx], 0.0)
            AC[i][n] = max(S[i][n] - K[input_idx], 0.0)
            EP[i][n] = max(K[input_idx] - S[i][n], 0.0)
            AP[i][n] = max(K[input_idx] - S[i][n], 0.0)

        # Backward recursion through the tree
        for j in range(n - 1, -1, -1):
            for i in range(j + 1):
                EC[i][j] = math.exp(-r * dt) * (p * EC[i][j + 1] + (1 - p) * EC[i + 1][j + 1])
                EP[i][j] = math.exp(-r * dt) * (p * EP[i][j + 1] + (1 - p) * EP[i + 1][j + 1])
                AC[i][j] = max(S[i][j] - K[input_idx], math.exp(-r * dt) * (p * AC[i][j + 1] + (1 - p) * AC[i + 1][j + 1]))
                AP[i][j] = max(K[input_idx] - S[i][j], math.exp(-r * dt) * (p * AP[i][j + 1] + (1 - p) * AP[i + 1][j + 1]))

        # Store results
        EC_results[input_idx] = EC[0][0]
        EP_results[input_idx] = EP[0][0]
        AC_results[input_idx] = AC[0][0]
        AP_results[input_idx] = AP[0][0]
        
        if type == 'Put':
            return AP_results[input_idx]
        else:
            return AC_results[input_idx]"""

    # Output of prices of calls and puts
"""print("The Cox Ross Rubinstein prices using", n, "steps are...")
    for input_idx in range(num_inputs):
        print(f"Input {input_idx+1}:")
        print("European Call", EC_results[input_idx])
        print("European Put", EP_results[input_idx])
        print("American Call", AC_results[input_idx])
        print("American Put", AP_results[input_idx])
        print()"""


import math

def max(a, b):
    return a if a > b else b

# Cox Ross Rubinstein parameters
"""n = 101                  # Number of steps
Spot = 150.35              # Spot Price
K = 145.0                 # Strike Price
T = 0.0082                   # Years to maturity
q = 0.0058
r = 0.0356                    # Risk-Free Rate
v = 0.25                    # Volatility"""

def CRR(n,Spot,K,T,q,r,v,type):
    i, j = 0, 0

    S = [[0] * (n + 1) for _ in range(n + 1)]
    EC = [[0] * (n + 1) for _ in range(n + 1)]
    EP = [[0] * (n + 1) for _ in range(n + 1)]
    AC = [[0] * (n + 1) for _ in range(n + 1)]
    AP = [[0] * (n + 1) for _ in range(n + 1)]

    dt = T / n
    u = math.exp(v * math.sqrt(dt))
    d = math.exp(-v * math.sqrt(dt))
    p = (math.exp((r - q) * dt) - d) / (u - d)

    # Build the Tree
    for j in range(n + 1):
        for i in range(j + 1):
            S[i][j] = Spot * math.pow(u, j - i) * math.pow(d, i)

    # Compute terminal payoffs
    for i in range(n + 1):
        EC[i][n] = max(S[i][n] - K, 0.0)
        AC[i][n] = max(S[i][n] - K, 0.0)
        EP[i][n] = max(K - S[i][n], 0.0)
        AP[i][n] = max(K - S[i][n], 0.0)

    # Backward recursion through the tree
    for j in range(n - 1, -1, -1):
        for i in range(j + 1):
            EC[i][j] = math.exp(-r * dt) * (p * EC[i][j + 1] + (1 - p) * EC[i + 1][j + 1])
            EP[i][j] = math.exp(-r * dt) * (p * EP[i][j + 1] + (1 - p) * EP[i + 1][j + 1])
            AC[i][j] = max(S[i][j] - K, math.exp(-r * dt) * (p * AC[i][j + 1] + (1 - p) * AC[i + 1][j + 1]))
            AP[i][j] = max(K - S[i][j], math.exp(-r * dt) * (p * AP[i][j + 1] + (1 - p) * AP[i + 1][j + 1]))

    # Output of prices of calls and puts
    """print("The Cox Ross Rubinstein prices using", n, "steps are...")
    print("European Call", EC[0][0])
    print("European Put", EP[0][0])
    print("American Call", AC[0][0])
    print("American Put", AP[0][0])
    print()"""
    if type == 'Puts':
        return AP[0][0]
    else:
        return AC[0][0]
