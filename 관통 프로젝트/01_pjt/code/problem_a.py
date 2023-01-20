import json
from pprint import pprint


def movie_info(movie):
    
    movie_dict = {}

    movie_dict["genre_ids"] = movie["genre_ids"]
    movie_dict["id"] = movie["id"]
    movie_dict["overview"] = movie["overview"]
    movie_dict["poster_path"] = movie["poster_path"]
    movie_dict["title"] = movie["title"]
    movie_dict["vote_average"] = movie["vote_average"]

    return movie_dict

    # new_data = {
    #     'genre_ids': movie.get('genre_ids'),
    #     'id': movie.get('id'),
    #     'overview':movie.get('overview'),
    #     'poster_path':movie.get('poster_path'),
    #     'title': movie.get('title'),
    #     'vote_average':movie.get('vote_average')
    # }
    # return new_data


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))