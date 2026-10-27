
import os
import shutil

# Specify the paths directly
githubtest_path = r"/home/coder/workspace/github_test"
parent_path = os.path.dirname(githubtest_path)

# Find all folders starting with "q-"
for folder_name in os.listdir(githubtest_path):
    source_path = os.path.join(githubtest_path, folder_name)

    if folder_name.startswith("q-") and os.path.isdir(source_path):
        destination_path = os.path.join(parent_path, folder_name)

        # Prevent overwriting an existing folder
        if os.path.exists(destination_path):
            print(f"Skipped (already exists): {folder_name}")
            continue

        # Move the entire folder and its contents
        shutil.move(source_path, destination_path)
        print(f"Moved: {folder_name}")

print("All eligible folders processed!")


