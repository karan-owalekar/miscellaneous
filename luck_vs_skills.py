import random
from tqdm import tqdm

class Person:
    def __init__(self, skills, luck, involvement_of_luck=5):
        self.skills = skills
        self.luck = luck
        self.involvement_of_luck = involvement_of_luck

    def probability_of_selection(self):
        return (
            self.skills * (100 - self.involvement_of_luck) + 
            self.luck * self.involvement_of_luck
        )

    def __str__(self):
        return f"Person(skills={self.skills}, luck={self.luck})"
    
    def get_luck(self):
        return self.luck

# Simulation parameters
number_of_people = 10000
involvement_of_luck = 1 # Percentage of luck in the selection probability
iterations = 1000
really_lucky = 75  # Luck threshold

# Tracking variables
total_luck = 0
total_skills = 0
total_min_luck = 0
total_least_lucky = 0

# Run simulation
for _ in tqdm(range(iterations)):
    people = []
    for _ in range(number_of_people):
        skills = random.randint(1, 100)
        luck = random.randint(1, 100)
        people.append(Person(skills, luck, involvement_of_luck))
    
    # Sort and select top 10
    people.sort(key=lambda x: x.probability_of_selection(), reverse=True)
    top_people = people[:10]
    
    # Update statistics
    total_luck += sum(p.get_luck() for p in top_people)
    total_skills += sum(p.skills for p in top_people)
    total_min_luck += min(p.get_luck() for p in top_people)
    total_least_lucky += sum(1 for p in top_people if p.get_luck() < really_lucky)

# Calculate averages
average_luck = total_luck / (iterations * 10)
average_skills = total_skills / (iterations * 10)
average_min_luck = total_min_luck / iterations
avg_less_lucky = total_least_lucky / iterations

print(f"Luck contribution: {involvement_of_luck}% | Skills contribution: {100 - involvement_of_luck}%")
print(f"Average luck of selected people: {average_luck:.2f}")
print(f"Average skills of selected people: {average_skills:.2f}")
print(f"Average of least lucky selected person: {average_min_luck:.2f}")
print(f"Average candidates with luck <{really_lucky}: {avg_less_lucky:.2f}")
