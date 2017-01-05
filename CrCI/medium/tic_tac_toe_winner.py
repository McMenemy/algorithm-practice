def tic_tac_toe_winner(board):
	for i in range(0, 3):
		row = ''
		col = ''
		for j in range(0, 3):
			row += board[i][j]
			col += board[j][i]
		if row == 'xxx' or col == 'xxx':
			return 'x won'
		elif row == 'ooo' or col == 'ooo':
			return 'o won'
	diag1 = board[0][0] + board[1][1] + board[2][2]
	diag2 = board[2][0] + board[1][1] + board[0][2]
	if diag1 == 'xxx' or diag2 == 'xxx':
		return 'x won'
	elif diag1 == 'ooo' or diag2 == 'ooo':
		return 'o won'
	return None

board1 = [['x', 'x', 'x'],
		  ['o', 'o', 'x'],
		  ['o', 'x', 'o']]

board2 = [['o', 'x', 'x'],
		  ['o', 'o', 'x'],
		  ['o', 'x', 'o']]

board3 = [['x', 'x', 'o'],
		  ['o', 'o', 'x'],
		  ['x', 'x', 'o']]

print(tic_tac_toe_winner(board1))
print(tic_tac_toe_winner(board2))
print(tic_tac_toe_winner(board3))
	
