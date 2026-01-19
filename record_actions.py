import pyautogui
import pygetwindow as gw
import time

# Function to record actions
def record_actions(duration=30):
	actions = []
	start_time = time.time()
	print("Recording...")

	while time.time() - start_time < duration:
		x, y = pyautogui.position()
		actions.append((time.time() - start_time, x, y))
		time.sleep(0.1)

	return actions

# Save recorded actions to a file
def save_actions(filename, actions):
	with open(filename, 'w') as f:
		for action in actions:
			f.write(f"{action[0]},{action[1]},{action[2]}\n")

# Main function
if __name__ == "__main__":
	duration = int(input("Enter recording duration (seconds): "))
	actions = record_actions(duration)
	save_actions("recorded_actions.txt", actions)
	print("Recording saved to recorded_actions.txt")