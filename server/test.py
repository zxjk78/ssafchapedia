'''
주석처리한 것이
django project, app 외부에서 파일을 사용하기 위한 코드
'''
# import os
# from config.settings import LANGUAGE_CODE
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# import django
# django.setup()
from movies.models import Movie
from people.models import Actor, Tmp, Cast
import requests
from pprint import pprint
import json
import re



TMDB_BASE_URL = 'https://api.themoviedb.org/3'
TMDB_API_KEY = 'b083ba699306944d1930bb483794ede6'
LANGUAGE_CODE = 'ko-KR'

'''
1. 내 DB의 영화에서 id로만 요청을 보내서 cast 정보를 json으로 얻어온 후
맨 앞 6명의 id만을 저장
'''

# for i in range(0, 99):
#     movies = Movie.objects.all()[i*10:i*10 + 10]
#     # movies = None
#     actor_id_set = set()
#     director_id_set = set()

#     for movie in movies:
#         movie_id = movie.id
#         print(f'영화 번호 {movie_id}')
#         get_credits_url = TMDB_BASE_URL + f'/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language={LANGUAGE_CODE}'

#         raw_data = requests.get(get_credits_url).json()
#         # cast한 배우, 감독 id를 저장
#         cnt = 0
#         for cast in raw_data.get('cast'):
#             cast_id = cast.get('id')
#             if not Tmp.objects.filter(actor_id=cast_id).exists():
#                 Tmp.objects.create(actor_id=cast_id)

#             print(f'배우{id} set에 집어넣는중')
#             cnt += 1
#             if cnt == 6:
#                 cnt = 0
#                 break
                
    # for crew in raw_data.get('crew'):
    #     if crew.get('job') == 'director':
    #         director_id_set.add(crew.get('id'))
    #         break
    
    # print('감독id set에 집어넣는중')

'''
배우 id로 다시 TMDB 로 요청을 보내서, 한글 이름이 존재하는 배우면 배우 테이블에 추가
'''


# actor_ids = Tmp.objects.all()


# for person in actor_ids:
#     person_id = person.actor_id
#     get_people_url = TMDB_BASE_URL + f'/person/{person_id}?api_key={TMDB_API_KEY}&language={LANGUAGE_CODE}'

#     raw_data = requests.get(get_people_url).json()

#     known_as = raw_data.get('also_known_as')
#     # 한글 이름이 있는 배우면 본명, 한글명, profile_path, 인기도를 저장한다.
#     for other_name in known_as:
#         if re.match(r'[가-힣]', other_name[0]):
            
#             actor_id = raw_data.get('id')
#             name = raw_data.get('name')
#             popularity = raw_data.get('popularity')
#             profile_path = raw_data.get('profile_path')
#             korean_name = other_name
#             Actor.objects.create(actor_id=actor_id, name=name, popularity=popularity, profile_path = profile_path, korean_name = other_name)

#             print(f'배우{actor_id} 집어넣는중')
#             break


'''
영화, 배우의 중개 테이블 추가

'''

# for i in range(0, 99):
#     movies = Movie.objects.all()[i*10:i*10 + 10]

#     for movie in movies:
#         movie_id = movie.id
#         print(f'영화 번호 {movie_id}')
#         get_credits_url = TMDB_BASE_URL + f'/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language={LANGUAGE_CODE}'

#         raw_data = requests.get(get_credits_url).json()
#         # 영화의 cast 를 6까지 보고, 만약 그 배우가 내 DB에 존재하면 추가함
#         cnt = 0
#         for cast in raw_data.get('cast'):
#             actor_id = cast.get('id')
#             actor = Actor.objects.filter(actor_id=actor_id) 
#             if actor.exists():
#                 Cast.objects.create(actor=actor[0], movie=movie)

#             print(f'배우{actor_id}을 영화 {movie_id}에 연결')
#             cnt += 1
#             if cnt == 6:
#                 cnt = 0
#                 break
    
