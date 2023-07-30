# # 1 

# import random
# import string


# def generate_random_number():
#     return random.randint(1, 100)


# def generate_filename(letter):
#     return f"{letter.upper()}.txt"


# def create_text_files():
#     for letter in string.ascii_uppercase:
#         filename = generate_filename(letter)
#         with open(filename, 'a') as file:
#             file.write(str(generate_random_number()) + '\n')


# def create_summary_file():
#     with open('summary.txt', 'w') as summary_file:
#         for letter in string.ascii_uppercase:
#             filename = generate_filename(letter)
#             summary_file.write(f"{filename}: {generate_random_number()}\n")


# if __name__ == "__main__":
#     create_text_files()
#     create_summary_file()

# # 2

# content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# file_path = "sample_file.txt"

# with open(file_path, "w") as file:
#     file.write(content)

# print("File created!")


# with open("sample_file.txt", "r") as file1:
#     content = file1.read()


# upper_case_content = content.upper()


# with open("sample_file_uppercase.txt", "w") as file2:
#     file2.write(upper_case_content)

# print("Content copied in upper case!")

# 3

# import csv
# import random


# players = ["Josh", "Luke", "Kate", "Mark", "Mary"]


# player_scores = {}


# for player in players:
#     scores = [random.randint(0, 1000) for _ in range(100)]
#     player_scores[player] = scores


# with open("game_scores.csv", "w", newline="") as csvfile:
#     fieldnames = ["Player name", "Score"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)      # fieldnames=fieldnames
#     writer.writeheader()
#     for player, scores in player_scores.items():
#         for score in scores:
#             writer.writerow({"Player name": player, "Score": score})


# print("Player name, Score")
# with open("game_scores.csv", "r") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row["Player name"], ",", row["Score"])

# 4
# import csv


# player_scores = {}
# with open("game_scores.csv", "r") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         player_name = row["Player name"]
#         score = int(row["Score"])
#         if player_name in player_scores:
#             player_scores[player_name] = max(player_scores[player_name], score)
#         else:
#             player_scores[player_name] = score


# sorted_scores = sorted(player_scores.items(), key=lambda x: x[1], reverse=True)


# with open("high_scores.csv", "w", newline="") as csvfile:
#     fieldnames = ["Player name", "Highest score"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for player, highest_score in sorted_scores:
#         writer.writerow({"Player name": player, "Highest score": highest_score})


