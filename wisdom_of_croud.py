import random
from tqdm import tqdm

#SET PARAMETERS
correst_answer = 1 # 1 for correct, 0 for incorrect
prob_of_correct_ans = 0.51 # probability of correct answer
number_of_people = 10000 # number of people in the crowd
total_iterations = 1000 # total number of simulations

#SIMULATE
correct_pred_by_one_person = 0
correct_pred_by_crowd = 0

for _ in tqdm(range(total_iterations)):

    # Get predictions by each person from the crowd
    correct_pred = 0
    for i in range(number_of_people):
        pred = random.randint(0, 100)
        if pred < prob_of_correct_ans * 100:
            correct_pred += 1
    
    # Prediction by one person with probability of correct_answer
    prediction_by_one_person = 1 if random.randint(0, 100) < prob_of_correct_ans * 100 else 0
    # Prediction by crowd with majority vote
    prediction_by_crowd = 1 if correct_pred > number_of_people / 2 else 0

    # Store predictions for each simulation
    if prediction_by_one_person == correst_answer:
        correct_pred_by_one_person += 1
    if prediction_by_crowd == correst_answer:
        correct_pred_by_crowd += 1

print(f"[INFO] Correct prediction by one person: {(correct_pred_by_one_person / total_iterations)*100} %")
print(f"[INFO] Correct prediction by crowd: {(correct_pred_by_crowd / total_iterations)*100} %")