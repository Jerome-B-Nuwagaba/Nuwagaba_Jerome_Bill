import numpy as np
import random

# Define environment parameters
road_length = 7 
actions = 3 

Q = np.zeros((road_length, actions))
# Define parameters
episodes = 1000  
learning_rate = 0.7  
gamma = 0.9  
epsilon = 0.3  

# Training loop
for episode in range(episodes):
    # Start at position 0
    state = 0
    
    while state < road_length - 1:  
        
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, actions - 1)  
        else:
            action = np.argmax(Q[state])  
        # Take action and observe next state
        if action == 0:  
            next_state = max(0, state - 1)
        elif action == 1:  
            next_state = state
        else:  
            next_state = min(road_length - 1, state + 1)
            
        # Reward structure
        if next_state == road_length - 1:  
            reward = 10
        elif action == 2:  
            reward = 1
        elif action == 1: 
            reward = -1
        else:  
            reward = -2
            
        # Q-learning update
        Q[state, action] += learning_rate * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
        
        # Transition to next state
        state = next_state
        
        # End episode if goal reached
        if state == road_length - 1:
            break

# Test the trained agent
print("\nTrained Agent's Path to Cross the Road:")
state = 0  
steps = 0
path = []

while state < road_length - 1 and steps < 20:  # Prevent infinite loops
    action = np.argmax(Q[state])
    if action == 0:
        next_state = max(0, state - 1)
        action_str = "Left"
    elif action == 1:
        next_state = state
        action_str = "Stay"
    else:
        next_state = min(road_length - 1, state + 1)
        action_str = "Right"
        
    path.append(f"Pos {state} -> {action_str} -> Pos {next_state}")
    state = next_state
    steps += 1

# Print the path
for i, step in enumerate(path):
    print(f"Step {i+1}: {step}")

if state == road_length - 1:
    print(f"\nSuccessfully crossed the road in {steps} steps!")
else:
    print("\nFailed to cross the road within the step limit.")

# Final Q-table
print("\nFinal Q-table:")
print("Rows: Positions (0 to 6), Columns: [Left, Stay, Right]")
print(Q)