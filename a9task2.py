import sys
import ply.lex as lex
import ply.yacc as yacc
import a9task1

cast_page = 'cast_page.html'

# Storing the token types in a list
tokens = ['p','a','bday','high','low','span','chigh','chigh1','thigh','thigh1','clow','tlow','label','celeb','box','data','date','Name','Blank','Space','Rarrow','col']

with open(cast_page,'r') as f:
	text =  f.read()
	f.close()

# Tokenizing the downloaded cast html file
def t_p(t):
	r'</p>'
	return t

def t_a(t):
	r'</a>'
	return t

def t_bday(t):
	r'Birthday\:'
	return t

def t_high(t):
	r'Highest\sRated:'
	return t

def t_low(t):
	r'Lowest\sRated:'
	return t

def t_span(t):
	r'<span'
	return t

def t_chigh(t):
	r'class="icon\sicon--tiny\sicon__certified-fresh"'
	return t

def t_chigh1(t):
	r'class="icon\sicon--tiny\sicon__fresh"'
	return t

def t_thigh(t):
	r'title="certified-fresh"></span>'
	return t

def t_thigh1(t):
	r'title="fresh"></span>'
	return t

def t_clow(t):
	r'class="icon\sicon--tiny\sicon__rotten"'
	return t

def t_tlow(t):
	r'title="rotten"></span>'
	return t

def t_label(t):
	r'class="label'
	return t

def t_celeb(t):
	r'<a\sclass="celebrity-bio__link"\shref="/m/'
	return t

def t_box(t):
	r'data-boxoffice="'
	return t

def t_data(t):
	r'data-title="'
	return t

def t_date(t):
	r'data-year="'
	return t

def t_Name(t):
	r'[_%&,:a-zA-Z0-9().\'-]+'
	return t

def t_Blank(t):
	r'\ '
	return t

def t_Space(t):
	r'[\s]+'
	return t

def t_Rarrow(t):
	r'">'
	return t

def t_col(t):
	r'"'
	return t

def t_error(t):
	t.lexer.skip(1)

lexer = lex.lex()

birthday = ""
highest_rated = ""
lowest_rated = ""
other_movies = []
years = []

# Writing the grammar
def p_begin(p):
	'''
	begin : birth
		  | highest 
		  | lowest
		  | other
		  | year
	'''
	pass

def p_words(p):
	'''
	words : Name  
	'''
	p[0] = p[1]

def p_g1(p):
	'''
	words : Name words
	'''	
	p[0] = p[1] + ' ' + p[2]

def p_g2(p):
	'''
	words : Name Blank words
	'''
	p[0] = p[1] + p[2] + p[3]

def p_birth(p):
	'''
	birth : bday Space words Space p
	'''
	global birthday
	birthday = p[3]

def p_highest(p):
	'''
	highest : high Space span Blank label Rarrow Space span Space chigh Space thigh Space words Space celeb words Rarrow Space words Space a
			| high Space span Blank label Rarrow Space span Space chigh1 Space thigh1 Space words Space celeb words Rarrow Space words Space a 
	'''
	global highest_rated
	highest_rated = p[20]

def p_lowest(p):
	'''
	lowest : low Space span Blank label Rarrow Space span Space clow Space tlow Space words Space celeb words Rarrow Space words Space a
	'''
	global lowest_rated
	lowest_rated = p[20]

def p_other(p):
	'''
	other : data words col Space box
	'''
	other_movies.append(p[2])

def p_year(p):
	'''
	year : date words col
	''' 
	years.append(p[2])

def p_error(p):
	pass

parser = yacc.yacc()

# Parsing the cast html file
parser.parse(text)

movie_year = {}

# Storing the release year of the movies in a dictionary
for i in range(len(other_movies)):
	movie_year[other_movies[i]] = years[i]

# Running an infinite loop
while True:

	print("\nEnter 0 to exit the loop")
	print("Enter 1 to display the cast's highest rated movie")
	print("Enter 2 to display the cast's lowest rated movie")
	print("Enter 3 to display the cast's Birthday")
	print("Enter 4 to display the cast's other movies ")

	# Checking if the input is an integer
	try:
		x = int(input())
	except ValueError:
		continue

	if x == 0:
		break
	elif x == 1:
		print('The actor/actress highest rated movie is :')
		print(highest_rated)
	elif x == 2:
		print('The actor/actress lowest rated movie is :')
		print(lowest_rated)
	elif x == 3:
		print('The actor/actress birthday is on :')
		print(birthday)
	elif x == 4:
		inp_year = int(input('Enter the year on or after which movies are to be shown \n'))
		print('The actor/actress other movies on or after',inp_year,'are :')
		for movie in other_movies:
			if movie != highest_rated[:highest_rated.find('(')-1] and movie != lowest_rated[:lowest_rated.find('(')-1] and int(movie_year[movie]) >= inp_year :
				print(movie)
	else :
		print('The input is invalid')