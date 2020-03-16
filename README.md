# Covid 19 estimator

This is something that I made for improving my python skills, this is may not be scientifically correct.
<img src="https://i.ibb.co/n0bWqrX/Captura-de-Pantalla-2020-03-15-a-la-s-19-59-05.png" alt="Captura-de-Pantalla-2020-03-15-a-la-s-19-59-05" border="0" />
<img src="https://i.ibb.co/vYkg2c3/Captura-de-Pantalla-2020-03-15-a-la-s-20-00-12.png" alt="Captura-de-Pantalla-2020-03-15-a-la-s-20-00-12" border="0" />
<img src="https://i.ibb.co/YPrhj67/Captura-de-Pantalla-2020-03-15-a-la-s-20-00-38.png" alt="Captura-de-Pantalla-2020-03-15-a-la-s-20-00-38" border="0" />


## How to run

First install `numpy` and `matplotlib`. Then open `test.py` and adjust the parameters as needed:

* size: size of the population, currently this runs on O(n^3), I would do ~1000.
* factor: a coefficient that determines the how contagious is the virus, ~13.
* cases: the number of initial cases.
* episdoes: the number of days the simuation will run.
* verbose: if true, this will show a scatter plot of the evolution every episode.

## Method

In this simulation I decide how many get infected in day 0, these people will infect `k` nearest neigbours, k is a random variable from an exponential distribution, where its beta arg is the sigmoid of the inverse squared distance to the mean. For example, a point far from the mean (center of the population) will yield a very big number, since the inverse is applied this will be a very small number inserted into the sigmoid function, so the farthest you are from the urban areas, the less probability of infection you have.

