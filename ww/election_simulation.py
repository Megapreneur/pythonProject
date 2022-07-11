import random


def simulate_election():
    if random.randint(0, 1) == 0:
        return "Candidate A"
    else:
        return "Candidate B"


candidate_a_counter = 0
candidate_b_counter = 0

for vote in range(10000):
    if simulate_election() == 0:
        candidate_a_counter += candidate_a_counter
    else:
        candidate_b_counter += candidate_b_counter
