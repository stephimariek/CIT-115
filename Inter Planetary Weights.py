#Constants

MERCURY_SGF = 0.38
VENUS_SGF = 0.91
MOON_SGF = 0.165
MARS_SGF = 0.38
JUPITER_SGF = 2.34
SATURN_SGF = 0.93
URANUS_SGF = 0.92
NEPTUNE_SGF = 1.12
PLUTO_SGF = 0.066
WEIGHT_FORMAT = "10.2f"
MAX_STRING = "20s"

#Input

sName = input("What is your name? ")
sWeight = input("What is your weight? ")

#Convert
nWeight = float(sWeight)

#Calculations

nMercury = nWeight * MERCURY_SGF
nVenus = nWeight * VENUS_SGF
nMoon = nWeight * MOON_SGF
nMars = nWeight * MARS_SGF
nJupiter = nWeight * JUPITER_SGF
nSaturn = nWeight * SATURN_SGF
nUranus = nWeight * URANUS_SGF
nNeptune = nWeight * NEPTUNE_SGF
nPluto = nWeight * PLUTO_SGF

#Output

print(sName,"here are your weights on our Solar System's Planets:")
print(f"{'Weight on Mercury:':{MAX_STRING}} {nMercury:{WEIGHT_FORMAT}}")
print(f"{'Weight on Venus:':{MAX_STRING}} {nVenus:{WEIGHT_FORMAT}}")
print(f"{'Weight on our Moon:':{MAX_STRING}} {nMoon:{WEIGHT_FORMAT}}")
print(f"{'Weight on Mars:':{MAX_STRING}} {nMars:{WEIGHT_FORMAT}}")
print(f"{'Weight on Jupiter:':{MAX_STRING}} {nJupiter:{WEIGHT_FORMAT}}")
print(f"{'Weight on Saturn:':{MAX_STRING}} {nSaturn:{WEIGHT_FORMAT}}")
print(f"{'Weight on Uranus:':{MAX_STRING}} {nUranus:{WEIGHT_FORMAT}}")
print(f"{'Weight on Neptune:':{MAX_STRING}} {nNeptune:{WEIGHT_FORMAT}}")
print(f"{'Weight on Pluto:':{MAX_STRING}} {nPluto:{WEIGHT_FORMAT}}")
