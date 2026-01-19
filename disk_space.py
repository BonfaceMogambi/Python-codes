import shutil

total, used, free = shutil.disk_usage("C:/")

print(f"Total: {total // (2**30)} GB")
print(f"Used: {used // (2**30)} GB")
print(f"Free: {free // (2**30)} GB")

if free // (2**30) < 10:
    print("⚠ WARNING: Low disk space!")
