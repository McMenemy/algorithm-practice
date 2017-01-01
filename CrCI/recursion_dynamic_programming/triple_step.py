def triple_step(steps):
	if steps < 0:
		return 0
	if steps == 0:
		return 1
	if steps == 1:
		return 1
	return triple_step(steps - 1) + triple_step(steps - 2) + triple_step(steps - 3)

print(triple_step(1))
print(triple_step(2))
print(triple_step(3))
print(triple_step(4))
print(triple_step(5))
print(triple_step(7))
print(triple_step(6))
	
def triple_step_memo(steps, memo=[1, 1, 2]):
	if steps < 0:
		return 0
	if steps < len(memo):
		return memo[steps]
	memo.append(triple_step_memo(steps - 1, memo) + triple_step_memo(steps - 2, memo) + triple_step_memo(steps - 3, memo))
	return memo[steps]
	

print(triple_step_memo(1))
print(triple_step_memo(2))
print(triple_step_memo(3))
print(triple_step_memo(4))
print(triple_step_memo(5))
print(triple_step_memo(7))
