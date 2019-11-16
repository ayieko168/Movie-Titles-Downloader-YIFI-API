import json
import urllib.request
import os


movies_dictionary = {} # the main dictionary holding the title and values
pages_to_visit = 230  # change to specify how many pages to visit

# parameters for the API end page
limit = 5
page = 220
quality = "All"
minimum_rating = 0
query_term = "0"
genre = "All"
sort_by = "title"
order_by = "asc"


url = "https://yts.am/api/v2/list_movies.json?order_by={}&page={}&sort_by={}&limit={}&with_rt_ratings=true".format(order_by, page, sort_by, limit)

def visit_site():
    # (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36
    req = urllib.request.Request(url, data=None, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

    f = urllib.request.urlopen(req)

    print("done downloading file..")

    return f

def look_for_movies():

    Main_json = json.loads(visit_site().read().decode()) # main api json file dataType:dictionary
    main_data = Main_json["data"] # type: dictionary
    movies_data = main_data["movies"] # type: list 

    for movie in movies_data:
        '''movie is a dictionary containing individual movie titles and their data'''

        movie_title = movie["title"]
        movie_url = movie["url"]
        movie_cover_image = movie["medium_cover_image"]
        # movie_large_cover_image = movie["large_cover_image"]
        movie_youtube_trailer_link_code = movie["yt_trailer_code"]
        # movie_imdb_code = movie["imdb_code"]
        # movie_year = movie["year"]
        # movie_rating = movie["rating"]
        # movie_length = movie["runtime"]
        # movie_genre = movie["genres"] # a list of genres
        # movie_summary = movie["summary"]
        # movie_description = movie["description_full"]
        # movie_language = movie["language"]
        # movie_torrents = movie["torrents"] # a list of torrent data ie links, pears etc ; list items - 720, 1080, 3D links

     
        movies_dictionary[movie_title] = [movie_url, movie_cover_image, movie_youtube_trailer_link_code]

        # write changes to movie list json file
        with open("Movies_List.json", "w") as json_object:
            json.dump(Main_json, json_object, indent=2)

for for_page in range(page,pages_to_visit+1):
    print("page = ", for_page)
    url = "https://yts.am/api/v2/list_movies.json?order_by={}&page={}&sort_by={}&limit={}&with_rt_ratings=true".format(order_by, page, sort_by, limit)

    try:
        look_for_movies()
        print("Done downloading ang writing file changes")
    except:
        print("pass")
        

    print("page {} done\n".format(for_page))
    
    page+=1

print("\nDone\n\n")





"""
Parameter 	        Type 					                Default 	    Description

limit 		        Integer between 1 - 50 (inclusive) 		20 		    The limit of results per page that has been set

page 		        Integer (Unsigned) 				        1 		    Used to see the next page of movies, eg limit=15 and page=2 will show you movies 15-30

quality 	        String (720p, 1080p, 3D) 		        All 		Used to filter by a given quality

minimum_rating 		Integer between 0 - 9 (inclusive) 	    0 		    Used to filter movie by a given minimum IMDb rating

query_term 			String 					                0 		    Used for movie search, matching on: Movie Title/IMDb Code, Actor Name/IMDb Code, Director Name/IMDb Code

genre 		        String 		                            All 		Used to filter by a given genre (See http://www.imdb.com/genre/ for full list)

sort_by 			String (title, year, rating, peers, 
					seeds, download_count, 
					like_count, date_added) 	            date_added 	Sorts the results by choosen value

order_by 			String (desc, asc) 			            desc 		Orders the results by either Ascending or Descending order

with_rt_ratings 		Boolean 				            false 		Returns the list with the Rotten Tomatoes rating included 


examples:
https://yts.am/api/v2/list_movies.xml?sort=seeds&limit=15

"""