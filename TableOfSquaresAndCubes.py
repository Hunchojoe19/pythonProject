number = 0

print(f"{'number':<10}{'square':^10}{'cube':>10}")

while number <= 5:
    print(f"{number:<10}{number ** 2:^10}{number ** 3:>10}")
    number += 1

# print("\n")
#
#
# print(f"{'number':>10} {'square':>10} {'cube':>10}")
# while number <= 5:
#     print(f"{number:>10} {number ** 2:>10} {number ** 3:>10}")
#     number += 1
