import random
import math
from tqdm import tqdm

def does_cross_line(needle_length: float,
                    line_spacing: float,
                    area_width: float) -> bool:
    center_x = random.uniform(0, area_width)
    angle    = random.uniform(0, math.pi)
    half_dx  = (needle_length / 2) * math.cos(angle)
    x1 = center_x + half_dx
    x2 = center_x - half_dx
    # Different floor indices means it crossed a line
    return math.floor(x1 / line_spacing) != math.floor(x2 / line_spacing)

def count_crossings(number_of_drops: int,
                    needle_length: float,
                    line_spacing: float,
                    area_width: float,
                    area_height: float = None) -> int:
    crossings = 0
    for _ in tqdm(range(number_of_drops)):
        if does_cross_line(needle_length, line_spacing, area_width):
            crossings += 1
    return crossings

def calculate_pi(number_of_drops: int,
                 needle_length: float,
                 line_spacing: float,
                 crossings: int) -> float:
    """
    Estimate π from the total drops and observed crossings.
    Uses π ≈ (2 · L · N) / (t · crossings).
    """
    if crossings == 0:
        return float('nan')
    return 2 * needle_length * number_of_drops / (line_spacing * crossings)

##############################################################################
# Parameters
needle_length = 1
line_spacing  = 1
area_width    = 100
number_of_drops = 10000000

# Perform the simulation
crossings = count_crossings(number_of_drops, needle_length, line_spacing, area_width)
pi_estimate = calculate_pi(number_of_drops, needle_length, line_spacing, crossings)

# Output the result
print(f"Estimated π: {pi_estimate}")
