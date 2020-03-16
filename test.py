import numpy as np
import matplotlib.pyplot as plt
import math
import copy


mean = [0,0]
cov = [[1,0], [0,1]]
size = 1200
factor = 13
cases = 3
episodes = 35
verbose = True
x, y = np.random.multivariate_normal(mean, cov, size).T

def split_infected(data):
    infected = []
    not_infected = []
    for i in data:
        if i[2] == 1 or i[2] == 2:
            infected.append(tuple(i))
        else:
            not_infected.append(tuple(i))
    return infected, not_infected

def plot_infection(data, accum_infected):
    infected, not_infected = split_infected(data)
    x_infected = [i[0] for i in infected]
    y_infected = [i[1] for i in infected]
    x_not_infected = [i[0] for i in not_infected]
    y_not_infected = [i[1] for i in not_infected]
    plt.scatter(x_not_infected, y_not_infected, color='b', alpha=0.1)
    plt.scatter(x_infected, y_infected, color='r', alpha=0.3)
    plt.title(f"COVID-19 Estimator J. Chávez")
    plt.ylabel("Total infected")
    plt.xlabel("Days")
    plt.show()

def distance(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def iterate(data, factor):
    total_infected = 0
    for i in data:
        if i[2] == 1:
            i[2] = 2
            # Search k nearest neighbours
            for j in data:
                j[3] = distance(j[0:2], i[0:2])

            # Order by distance
            data = data[data[:,3].argsort()]
        
            aislamiento = i[0]**2 + i[1]**2
            aislamiento = aislamiento if aislamiento != 0 else 0.01

            beta_exp = factor*(1/(1+math.e**(-.1/aislamiento)))**2
            k = round(np.random.exponential(beta_exp))
            
            sum = 0
            for j in range(1,k+2):
                if data[j][2] == 0: #If not infected
                    data[j][2] = 1
                    sum += 1

            total_infected += sum

    return total_infected, data


               


# Data -> [x,y,infected,dummy]
data = zip(x, y)
data = [list(p) for p in data]
for i in data:
    i.append(0)
    i.append(0)

data = np.array(data)

### Infection
for i in range(cases):
    case = np.random.randint(0, size)
    data[case][2] = 1

accum_infected = [cases]
if verbose:
    plot_infection(data, cases)
for i in range(episodes):
    infected, data = iterate(data, factor)
    accum_infected.append(infected+accum_infected[-1])
    if i > 0:
        print(f"dia {i} - acc {accum_infected[-1]} - %crec {accum_infected[-1]/accum_infected[-2]}")
    if verbose:
        plot_infection(data, accum_infected[-1])

plt.plot(accum_infected)
plt.title("COVID-19 Estimator J. Chávez")
plt.ylabel("Total infected")
plt.xlabel("Days")
plt.show()
