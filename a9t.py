import  os
import sys
import re
import urllib.request,urllib.error,urllib.parse

# Storing the urls for the genres in a dictionary

url = {'Action & Adventure':'https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/',
		'Animation':'https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/',
		'Drama':'https://www.rottentomatoes.com/top/bestofrt/top_100_drama_movies/',
		'Comedy':'https://www.rottentomatoes.com/top/bestofrt/top_100_comedy_movies/',
		'Mystery & Suspense':'https://www.rottentomatoes.com/top/bestofrt/top_100_mystery__suspense_movies/',
		'Horror':'https://www.rottentomatoes.com/top/bestofrt/top_100_horror_movies/',
		'Sci-Fi':'https://www.rottentomatoes.com/top/bestofrt/top_100_science_fiction__fantasy_movies/',
		'Documentary':'https://www.rottentomatoes.com/top/bestofrt/top_100_documentary_movies/',
		'Romance':'https://www.rottentomatoes.com/top/bestofrt/top_100_romance_movies/',
		'Classics':'https://www.rottentomatoes.com/top/bestofrt/top_100_classics_movies/'}

url1 = url.get('Action & Adventure')
r1 = urllib.request.urlopen(url1)
w1 = r1.read()

f1 = open("Action & Adventure.html","wb")
f1.write(w1)
f1.close()

url2 = url.get('Animation')
r2 = urllib.request.urlopen(url2)
w2 = r2.read()

f2 = open("Animation.html","wb")
f2.write(w2)
f2.close()

url3 = url.get('Drama')
r3 = urllib.request.urlopen(url3)
w3 = r3.read()

f3 = open("Drama.html","wb")
f3.write(w3)
f3.close()

url4 = url.get('Comedy')
r4 = urllib.request.urlopen(url4)
w4 = r4.read()

f4 = open("Comedy.html","wb")
f4.write(w4)
f4.close()

url5 = url.get('Mystery & Suspense')
r5 = urllib.request.urlopen(url5)
w5 = r5.read()

f5 = open("Mystery & Suspense.html","wb")
f5.write(w5)
f5.close()

url6 = url.get('Horror')
r6 = urllib.request.urlopen(url6)
w6 = r6.read()

f6 = open("Horror.html","wb")
f6.write(w6)
f6.close()

url7 = url.get('Sci-Fi')
r7 = urllib.request.urlopen(url7)
w7 = r7.read()

f7 = open("Sci-Fi.html","wb")
f7.write(w7)
f7.close()

url8 = url.get('Documentary')
r8 = urllib.request.urlopen(url8)
w8 = r8.read()

f8 = open("Documentary.html","wb")
f8.write(w8)
f8.close()

url9 = url.get('Romance')
r9 = urllib.request.urlopen(url9)
w9 = r9.read()

f9 = open("Romance.html","wb")
f9.write(w9)
f9.close()

url10 = url.get('Classics')
r10 = urllib.request.urlopen(url10)
w10 = r10.read()

f10 = open("Classics.html","wb")
f10.write(w10)
f10.close()

# Running an infinite loop
while (1):

	genre = input('Enter the genre or enter exit or EXIT to stop\n')
	# Removing trailing and leading blank spaces
	genre = genre.strip()

	# To exit the loop enter EXIT or exit
	if genre == 'EXIT' or genre == 'exit':
		break
	else :
		gen = genre 

	movie_url = {}

	if genre == 'Action & Adventure' or genre == 'Animation' or genre == 'Drama' or genre == 'Comedy' or genre == 'Mystery & Suspense' or genre == 'Horror' or genre == 'Sci-Fi' or genre == 'Documentary' or genre == 'Romance' or genre == 'Classics':
		site = genre + '.html'
		with open(site,'r') as f:
			w = f.read()
			str1 = re.compile(r'class="unstyled articleLink">[a-zA-Z0-9!\'()-:,\W.\s\-?ôôéûO]+</a>')
			movies = str1.findall(w)
			str2 = re.compile(r'<a href="/m/[a-zA-Z0-9_-]+" class="unstyled articleLink">')
			links = str2.findall(w)

			print('Top 100 movies of genre ',genre)
			i = 0
			for movie in movies:
				link = links[i]
				movie = movie[35:]
				movie = movie.strip()
				# Processing to get only the relevant part
				movie = movie.replace('</a>','')
				link = link.replace('" class="unstyled articleLink">','')
				link = link.replace('<a href="','')
				link = link.strip()
				link = 'https://www.rottentomatoes.com' + link
				if movie != 'll':
					print(movie)
					movie_url[movie] = link
				if i < len(links)-1:
					i += 1

		inp_movie = input('Enter the movie name or enter exit or EXIT to stop\n')
		inp_movie = inp_movie.strip()

		if inp_movie == 'EXIT' or inp_movie == 'exit':
			break

		if inp_movie in movie_url.keys():
			u = movie_url.get(inp_movie)
			r = urllib.request.urlopen(u)
			w = r.read()
			fp = open('download_movie.html',"wb")
			fp.write(w)
			fp.close()
			print('The movie html page has been downloaded')
		else:
			print('Movie not found')

	else:
		print("Invalid genre")
