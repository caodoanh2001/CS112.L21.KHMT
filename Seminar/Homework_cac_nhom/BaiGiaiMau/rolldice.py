def diceRolls_optimized(dice, target_sum, tracked_list = []):
  if dice == 0:
    if sum(tracked_list) == target_sum:
      print(tracked_list)
  else:
    for i in range(1,7):
        if (sum(tracked_list) + i + 1*(dice - 1) <= target_sum) \
        and (sum(tracked_list) + i + 6*(dice - 1) >= target_sum):
                tracked_list.append(i)
                diceRolls_optimized(dice - 1, target_sum, tracked_list)
       	del tracked_list[-1]