# numbers = [0,1,2,3,4]

# for num in numbers:
#     print(num)

# for num in range(5):
#     print(num)

# counties = ["a", "b", "c"]

# for i in range(len(counties)):
#     print(counties[i])

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for i in range(len(voting_data)):
#     print(voting_data[i]['county'])


# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for county_dict in voting_data:
#     print(county_dict['county'])


# my_votes = int(input("How many votes did you get?"))

# total_votes = int(input("total votes please?"))

# print(f"I recieved {my_votes/total_votes*100}% of the total votes.")

# for county,voters in counties_dict.items():
#     print(f" {county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)