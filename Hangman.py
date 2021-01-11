def replace_char(a_string,index,a_char):
	output = ''

	for i in range(index):
		output = output+a_string[i]
	
	output = output+a_char

	for i in range(index+1,len(a_string),1):
		output = output+a_string[i]

	return output
	
def play():
	player_count = 2
	secret_word = raw_input("The word is: ")
	player_input = '_'*len(secret_word)
	number_incorrect = 0
	guessed_list = []
	game_is_done = False 
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	
	a="\n\n"
	b=" o\n\n"
	c=" o\n |\n"
	d=" o\n |-\n"
	e=" o\n-|-\n"
	f=" o\n-|-\n/"
	g=" o\n-|-\n/ \\"



	my_list = [a,b,c,d,e,f,g]


	while number_incorrect < 7 and secret_word != player_input:
		print player_input
		print guessed_list
		print my_list[number_incorrect]
		guessed_letter = raw_input("Guess a letter: ")
		 
		while guessed_letter not in alphabet and guessed_letter not in guessed_list:
			print "invalid choice, choose again"
			guessed_letter = raw_input('Guess a letter: ')
		guessed_list.append(guessed_letter)
		
		if guessed_letter not in secret_word: 
			print 'Letters is not found.'
			number_incorrect = number_incorrect + 1
		
		
			
			


		for i in range(len(secret_word)):
			if guessed_letter == secret_word[i]: 
				player_input = replace_char(player_input,i,guessed_letter)
			
	

	
			
	
	if number_incorrect == 7:
		print 'Game over for you. Srub'
		print 'The word was %s: ' % secret_word 
	
	if secret_word == player_input:
		print 'The word is %s' % secret_word
		
		print 'Game over. You have correctly guessed the word.'
			
			
play()


			