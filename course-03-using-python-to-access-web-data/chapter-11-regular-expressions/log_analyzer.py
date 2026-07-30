import re

name = input("Enter the name of the file: ")
if len(name) < 1:
    name = 'server_log.txt'

line_counter = 0
ids = []
user_counts = {}
level_counts = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0,
}

try:
    with open(name) as file_handle:
        for line in file_handle:
            line_counter += 1

            id_matches = re.findall(r'ID:(\d+)', line)
            if id_matches:
                ids.append(int(id_matches[0]))

            user_matches = re.findall(r'User: (\w+)', line)
            if user_matches:
                user = user_matches[0]
                if user in user_counts:
                    user_counts[user] = user_counts[user] + 1
                else:
                    user_counts[user] = 1

            pieces = line.split()
            if len(pieces) >= 3:
                level = pieces[2]
                if level == "INFO":
                    level_counts["INFO"] = level_counts["INFO"] + 1
                elif level == "WARNING":
                    level_counts["WARNING"] = level_counts["WARNING"] + 1
                elif level == "ERROR":
                    level_counts["ERROR"] = level_counts["ERROR"] + 1
except FileNotFoundError:
    print("File not found:", name)
    quit()

ids_sum = sum(ids)
most_common_user = None
most_common_count = 0

for user in user_counts:
    if user_counts[user] > most_common_count:
        most_common_user = user
        most_common_count = user_counts[user]

print("IDs: ")
for id_names in ids:
    print(id_names)
print("Lines:", line_counter)
print("Sum of IDs:", ids_sum)
print(f"INFO:, {level_counts["INFO"]}, WARNING:, {level_counts["WARNING"]}, ERROR:, {level_counts["ERROR"]}")
if most_common_user is not None:
    print("Most frequent user:", most_common_user, "appeared", most_common_count, "times")
else:
    print("No users found in the log.")