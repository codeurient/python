#


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_composite_sums(target, current_sum=0, current_list=[]):
    if target == current_sum:
        if len(current_list) > 1:
            return [current_list]
        return []

    result = []
    for i in range(4, target - current_sum + 1):
        if not is_prime(i):
            result += find_composite_sums(target, current_sum + i, current_list + [i])
    return result

user_input = int(input("Tam eded daxil edin: "))

result = find_composite_sums(user_input)
if result:
    for res in result:
        print(" + ".join(map(str, res)), "=", user_input)
else:
    print("Tapmaq mumkun olmadi")






# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def find_composite_sums(target, current_sum=0, current_list=[]):
#     if target == current_sum:
#         if len(current_list) > 1:
#             return 1
#         return 0

#     result = 0
#     for i in range(4, target - current_sum + 1):
#         if not is_prime(i):
#             result += find_composite_sums(target, current_sum + i, current_list + [i])
#     return result

# user_input = int(input("Tam eded daxil edin: "))

# result = find_composite_sums(user_input)
# print(f"Istifade edilen kombinasiya sayi: {result}")
