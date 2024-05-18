# Miscellaneous Code Simulations

This repository contains various code simulations that demonstrate different concepts and principles. Below are descriptions of the current simulations included in this repository.

## • Wisdom of the Crowd Simulation

The "Wisdom of the Crowd" simulation in this repository follows the principle of a random forest approach. In this simulation, we set the probability of one person giving the correct answer. Then, we collect predictions from each individual and utilize them to generate a collective prediction from the crowd. By harnessing the collective intelligence of diverse individuals, this simulation explores how aggregating opinions can often lead to more accurate predictions than individual judgments alone.

### Explanation:

Even if an individual's probability of correct prediction is, for example, 0.6, out of 100 individuals, we can expect approximately 60 correct predictions on average. By aggregating these predictions, the crowd's collective wisdom can often lead to more accurate outcomes. Since we only need a simple majority (51 of 100) for the crowd's prediction to be considered.

## • Monty Hall Problem Simulation

The "Monty Hall Problem" simulation in this repository illustrates the well-known probability puzzle based on a game show scenario. Here's a detailed explanation of the problem and why it is statistically better to switch your choice of door.

### The Monty Hall Problem

In the Monty Hall problem, a contestant is presented with three doors. Behind one of these doors is a car (the prize), and behind the other two doors are goats. The contestant initially picks one of the three doors. The host, Monty Hall, who knows what's behind each door, then opens one of the two remaining doors, revealing a goat. The contestant is then given the option to stick with their original choice or switch to the other unopened door. The question is: Should the contestant switch or stay with their initial choice to maximize their chances of winning the car?

### Explanation of Why It's Better to Switch

Imagine the winning door is Door 1. Let's analyze the scenarios:

1. **If the contestant picks Door 1 initially:**
    - Monty opens either Door 2 or Door 3 (both have goats).
    - If the contestant switches, they will lose (since they switch to a goat).

2. **If the contestant picks Door 2 initially:**
    - Monty opens Door 3 (revealing a goat).
    - If the contestant switches, they will win (since they switch to Door 1, the winning door).

3. **If the contestant picks Door 3 initially:**
    - Monty opens Door 2 (revealing a goat).
    - If the contestant switches, they will win (since they switch to Door 1, the winning door).

From this analysis, we see that:
- If the contestant sticks with their initial choice, they only win if they initially picked the winning door (1/3 probability).
- If the contestant switches, they win if they initially picked a losing door (2/3 probability).

Thus, the probability of winning the car by switching is 2/3, while the probability of winning by sticking with the initial choice is only 1/3. Therefore, it is statistically better to switch doors.
