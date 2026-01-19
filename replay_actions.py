import pyautogui
import time

# Function to load recorded actions from a file
def load_actions(filename):
	actions = []
	with open(filename, 'r') as f:
		for line in f:
			t, x, y = line.strip().split(',')
			actions.append((float(t), int(x), int(y)))
	return actions

# Function to replay actions
def replay_actions(actions):
	start_time = time.time()
	for action in actions:
		while time.time() - start_time < action[0]:
			time.sleep(0.01)
			pyautogui.moveTo(action[1], action[2])

# Main function
if __name__ == "__main__":
	actions = load_actions("recorded_actions.txt")
	print("Replaying actions...")
	replay_actions(actions)
	print("Actions replayed successfully")