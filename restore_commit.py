import subprocess

# Find the last good commit
result = subprocess.run(['git', 'log', '--oneline', '-1'], capture_output=True, text=True)
last_commit = result.stdout.split()[0]
print(f"Last commit: {last_commit}")

# Restore everything from that commit
subprocess.run(['git', 'checkout', f'{last_commit}', '--', '.'])
print("Restored all files from last commit")

# Or checkout just specific files
# files_to_restore = ['main.py', 'requirements.txt', 'index.html']
# for file in files_to_restore:
#     subprocess.run(['git', 'checkout', f'{last_commit}', '--', file])