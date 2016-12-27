def loop_dection(lList):
	walker = runner = lList.head
	while runner:
		if runner == walker:
			return True
		walker = walker.child
		runner = runner.child
	return False
