def RemoveFirst(value):
	token = "";
	st = 0;
	for arr in 	value:
		#counter
		st += 1;
		if (st == 1):
			#skip first chars
			pass;
		else:
			token += arr;

	return token

def RemoveFirstSpace(value):
	token = "";
	allow = False;

	for chrs in value:
		if (chrs == " " or chrs == "\n" or chrs == "\t"):
			if (allow):
				token += chrs;
			else:
				pass;
		else:
			token += chrs;
			allow = True;

	return token;