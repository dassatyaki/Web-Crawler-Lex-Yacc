import sys
import ply.lex as lex
import ply.yacc as yacc
import urllib.request,urllib.error,urllib.parse
import re
import os
import a9t

def recurse():

	# Running an infinite loop
	while True:

		print("\nEnter 0 to exit the loop")
		print("Enter 1 to display Movie Name")
		print("Enter 2 to display Directors")
		print("Enter 3 to display Producers")
		print("Enter 4 to display Writers ")
		print("Enter 5 to display Original Language")
		print("Enter 6 to display Cast with the character name")
		print("Enter 7 to display Storyline")
		print("Enter 8 to display Box Office collection")
		print("Enter 9 to display Runtime")
		print("Enter 10 for You Might Also Like")
		print("Enter 11 for Where To Watch")

		# Checking if the input is an integer
		try:
			x = int(input())
		except ValueError:
			continue

		if x == 0:
			break
		elif x == 1:
			print ("Movie name is :")
			print(movie)
		elif x == 2:
			print("Director/directors is/are :")
			for director in directors:
				print(director)
		elif x == 3:
			print("Producer/producers is/are :")
			for producer in producers:
				print(producer)
		elif x == 4:
			print("Writer/Writers is/are :")
			for writer in writers:
				print(writer)
		elif x == 5:
			print("Original language is :")
			print(lang)
		elif x == 6:
			cast_pages = []
			cast_page_links = {}
			flag = True

			str1 = re.compile(r'<a href="/celebrity/[a-zA-Z0-9_-]+" data-qa="cast-crew-item-img-link">')
			pages = str1.findall(txt)

			for page in pages:
				page = page.replace('<a href="','')
				page = page.replace('" data-qa="cast-crew-item-img-link">','')
				page = page.strip()
				page = 'https://www.rottentomatoes.com' + page
				cast_pages.append(page)

			if len(cast_pages) == len(cast_crew):
				for k in range(len(cast_crew)):
					cast_page_links[cast_crew[k]] = cast_pages[k]
			else :
				flag = False

			print("Cast with character names are :")
			if len(cast_crew) == len(characters):
				for i in range(len(cast_crew)):
					print(cast_crew[i],' ',characters[i])
			else:
				for item in cast_crew:
					print(item)
					
			if flag == True:
				inp_cast = input('Enter a cast name from the above cast list\n')
				inp_cast = inp_cast.strip()

				if inp_cast in cast_page_links.keys():
					u = cast_page_links.get(inp_cast)
					r = urllib.request.urlopen(u)
					w = r.read()
					fp = open('cast_page.html',"wb")
					fp.write(w)
					fp.close()
					print('The cast page has been downloaded')	
				else:
					print('The cast name you have entered is not present in the cast list')
			else :
				print('All the casts do not have html pages')

		elif x == 7:
			print("Storyline is :")
			print(story)
		elif x == 8:
			print ("Box office collection is :")
			print(collection)
		elif x == 9:
			print("Movie runtime is :")
			print(runtime[:-1])
		elif x == 10:

			also_links = []
			also_like_links = {}
			string = re.compile(r'<a href="/m/[a-zA-Z0-9_-]+" class="recommendations-panel__poster-link">')
			links = string.findall(txt)

			for link in links:
				link = link.replace('<a href="','')
				link = link.replace('" class="recommendations-panel__poster-link">','')
				link = link.strip()
				link = 'https://www.rottentomatoes.com' + link
				also_links.append(link)
			print("You Might Also Like :")

			for i in range(len(also_like)):
				print(also_like[i])
				also_like_links[also_like[i]] = also_links[i]

			movie_inp = input('Enter a movie name from the above listed movies\n')
			movie_inp = movie_inp.strip()

			if movie_inp in also_like_links.keys():
				u = also_like_links.get(movie_inp)
				r = urllib.request.urlopen(u)
				w = r.read()
				fp = open('download_movie.html',"wb")
				fp.write(w)
				fp.close()

				os.system("python3 a9task1.py")
			else :
				print('The movie you have entered is not in the also-like list')
				
		elif x == 11 :
			print("The online platforms for watching the movie are :")
			for item in where_to_watch:
				print(item)
		else:
			print("Invalid input ")

movie_name = 'download_movie.html'

# Storing the token types in a list
tokens = ['MovieName','End','div','br','span','LDirector','Celeb','Writer','Producer','Language','Cast','Storyline','Boxoffice','Runtime','also','watch','target','Name','Blank','Space','Rarrow']

with open(movie_name,'r') as f:
	txt = f.read()
	f.close()

# Tokenizing the downloaded movie html file
def t_MovieName(t):
	r'<meta\sproperty="og:title"\scontent="'
	return t

def t_End(t):
	r'</a>'
	return t

def t_div(t):
	r'</div>'
	return t

def t_br(t):
	r'<br/>'
	return t

def t_span(t):
	r'</span>'
	return t

def t_LDirector(t):
	r'data-qa="movie-info-director'
	return t

def t_Celeb(t):
	r'<a\shref="/celebrity/[_-a-zA-z0-9]+'
	return t

def t_Writer(t):
	r'Writer:</div>[\s]+<div\sclass="meta-value"\sdata-qa="movie-info-item-value'
	return t

def t_Producer(t):
	r'Producer:</div>[\s]+<div\sclass="meta-value"\sdata-qa="movie-info-item-value'
	return t

def t_Language(t):
	r'Language:</div>[\s]+<div\sclass="meta-value"\sdata-qa="movie-info-item-value'
	return t

def t_Cast(t):
	r'<span\stitle="'
	return t

def t_Storyline(t):
	r'<meta\sname="description"\scontent="'
	return t

def t_Boxoffice(t):
	r'data-qa="movie-info-item-value">\$'
	return t

def t_Runtime(t):
	r'<time\sdatetime="P'
	return t

def t_also(t):
	r'class="recommendations-panel__poster-title'
	return t

def t_watch(t):
	r'data-affiliate="'
	return t

def t_target(t):
	r'"\ target="blank"'
	return t

def t_Name(t):
	r'[,:a-zA-Z0-9().\'-]+'
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

def t_error(t):
	t.lexer.skip(1)

lexer = lex.lex()

directors = []
writers = []
producers = []
lang = ""
story = ""
movie = ""
collection = ""
runtime = ""
cast_crew = []
characters = []
also_like = []
where_to_watch = []

# Writing the grammar
def p_begin(p):
	'''
	begin : movie
		  | direct 
		  | write
		  | produce
		  | lang 
		  | cast
		  | story
		  | box
		  | Time
		  | chars
		  | like
		  | where 
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

def p_movie(p):
	'''
	movie : MovieName words Rarrow
	'''
	global movie
	movie = p[2]

def p_direct(p):
	'''
	direct : LDirector Rarrow words End
	'''
	directors.append(p[3])

def p_write(p):
	'''
	write : Writer Rarrow Space Celeb Rarrow words End
	'''
	writers.append(p[6])

def p_produce(p):
	'''
	produce : Producer Rarrow Space Celeb Rarrow words End
	'''
	producers.append(p[6])

def p_lang(p):
	'''
	lang : Language Rarrow words Space
	'''
	global lang
	lang = p[3]

def p_cast(p):
	'''
	cast : Cast words Rarrow
	'''
	cast_crew.append(p[2])

def p_story(p):
	'''
	story : Storyline words Rarrow
	'''
	global story
	story = p[2]

def p_box(p):
	'''
	box : Boxoffice Name div Space
	'''
	global collection
	collection = '$' + p[2]

def p_Time(p):
	'''
	Time : Runtime words Rarrow
	'''
	global runtime 
	runtime = p[2] 

def p_chars(p):
	'''
	chars : br Space words Space br Space span
			| br Space words Space span
	'''
	characters.append(p[3])

def p_like(p):
	'''
	like : also Rarrow words span
	'''
	also_like.append(p[3])

def p_where(p):
	'''
	where : watch words target
	'''
	where_to_watch.append(p[2])
	
def p_error(p):
	pass

parser = yacc.yacc()

# Parsing the movie html file
parser.parse(txt)

if len(characters) == len(cast_crew):
	producers = []
	writers = []
	for i in range(len(characters)):
		if characters[i] == 'Writer' or characters[i] == 'Screenwriter':
			writers.append(cast_crew[i])
		elif characters[i] == 'Producer':
			producers.append(cast_crew[i])

recurse()