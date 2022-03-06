from itertools import product


def graduation_cermony(working_days):
    # Let consider Present to the calss as P and Absent as A
    total_attend_ways = product(["P","A"], repeat=working_days)
    total_attend_ways_list = list(total_attend_ways)
    consecutive_four_abs_count = 0
    graduation_day_miss_count = 0
    total_attend_ways_count = len(total_attend_ways_list)

    for comb in total_attend_ways_list:
        comb_str = "".join(comb)
        if "AAAA" in comb_str:
            consecutive_four_abs_count += 1
        elif comb_str.endswith("A"):
            graduation_day_miss_count += 1

    cermony_allowed_attend_ways = total_attend_ways_count - consecutive_four_abs_count
    return("{}/{}".format(graduation_day_miss_count, cermony_allowed_attend_ways))


print(graduation_cermony(5))
print(graduation_cermony(10))
