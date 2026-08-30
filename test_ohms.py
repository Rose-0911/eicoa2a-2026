from ohms_law import calc_resistance

result = calc_resistance(27, 5)

print("Resistance =", result, "ohms")
print(calc_resistance.__doc__)

assert calc_resistance(9, 0.03) == 300

assert calc_resistance(24, 2) == 12
print(calc_resistance.__doc__)

from ohms_law import calc_current, calc_power

power1 = calc_power(12, 6)
print("power 1 =", power1, "W")

power2 = calc_power(24, 12)
print("power 2 =", power2, "W")

print(calc_power.__doc__)