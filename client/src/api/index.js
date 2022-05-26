import axios from 'axios'

// auth: dj-rest-auth 의 토큰 기반 인증 기능 이용
const LOGIN_URL = '/auth/login/'
const SIGNUP_URL = '/auth/signup/'
const GET_USER_INFO = '/auth/user/'

// accounts
const ACCOUNT_URL = '/accounts/' 
const PROFILE_URL = '/profile/'
// const MYINFO_URL = '/accounts/myinfo/'
// const PROFILE_URL = '/accounts/<str:username>/profile'

//DEFAULT_URL은 중간에 pk 등이 들어갈 때도 사용 가능
// movie
const MOVIE_SEARCH_LIST_URL = '/movies/search'
const MOVIE_URL = '/movies/movie'
const MOVIE_RANDOM = '/movies/random'
const MOVIE_RECOMMEND = '/movies/recommend'
// const MOVIE_LIST_URL = '/movies/'
// const MOVIE_DETAIL_URL = '/movies/<int:movie_pk>/detail/'
// const MOVIE_SEARCH_LIST_URL = '/movies/search'

// actor
const ACTOR_DEFAULT_URL = '/people/'
const ACTOR_SEARCH_LIST_URL = '/people/search'
const ACTOR_DETAIL_URL = '/detail/'
// const ACTOR_URL = '/actors/'
// const ACTOR_DETAIL_URL = '/actors/<int:actor_pk>/detail/'
// const ACTOR_SEARCH_LIST_URL = '/actors/search'

// review
const REVIEW_URL = '/reviews/'
const REVIEW_LIST_URL = '/reviews/'
// const REVIEW_LIST_URL = '/reviews/'
// const USER_REVIEW_LIST_URL = '/reviews/<str:username>/list/'
// const REVIEW_CREATE_URL = '/reviews/new/'


const axiosInstance = axios.create({
  baseURL:'http://localhost:8000/api/v1',
})

axiosInstance.interceptors.request.use(
  (config)=>{
    const token = localStorage.getItem('authToken')
    if (token){
      config.headers.Authorization = `Token ${token}`
    }
    return config
  },
  (error)=>{
    return Promise.reject(error)
  },
)


//auth: django restframework

const login = async (body) => {
  const res = await axiosInstance.post(LOGIN_URL, body)
  console.log(res)
  return res
}

const signup = async (body) => {
  const res = await axiosInstance.post(SIGNUP_URL, body)
  return res 
}

const getMyInfo = async () => {
  const res = await axiosInstance.get(GET_USER_INFO)
  return res 
}

const fetchUserProfile = async (username)=> {
  const res = await axiosInstance.get(ACCOUNT_URL + username + PROFILE_URL)
  return res
}


//movie

const fetchMovieSearchList = async (keyword) => {
  const res = await axiosInstance.get(MOVIE_SEARCH_LIST_URL, {params:{keyword: keyword}})
  return res
}
const fetchMovie = async (movieId) => {
  const movieURL = MOVIE_URL + `/${movieId}/`
  const res = await axiosInstance.get(movieURL)
  return res
}

const fetchMovieList = async () => {
  const movieURL = MOVIE_URL + '/'
  const res = await axiosInstance.get(movieURL)
  return res
}

const fetchMovieRandom = async () => {
  const movieURL = MOVIE_RANDOM + '/'
  const res = await axiosInstance.get(movieURL)
  return res
}
const fetchMovieRecommend = async()=> {
  const movieURL = MOVIE_RECOMMEND + '/'
  const res = await axiosInstance.get(movieURL)
  return res
}
//people

const fetchActorSearchList = async (keyword) => {
  const res = await axiosInstance.get(ACTOR_SEARCH_LIST_URL, {params:{keyword: keyword}})
  return res
}
const fetchActorDetail = async (actorId) => {
  const res = await axiosInstance.get(ACTOR_DEFAULT_URL + actorId + ACTOR_DETAIL_URL)
  return res
}


//review

const fetchReviewList = async () => {
  const res = await axiosInstance.get(REVIEW_LIST_URL)
  return res
}
const fetchReviewGet = async (movieId) => {
  const res = await axiosInstance.get(REVIEW_LIST_URL + movieId +'/')
  return res
}
const fetchUserReviewList = async (username, page) => {
  const res = await axiosInstance.get(REVIEW_LIST_URL + username + '/list/', {params:{page: page}})
  return res
}

const reviewExist = async (movieId) => {
  const res = await axiosInstance.get(REVIEW_URL + movieId + `/exist/`)
  return res
}
const createReview = async (movieId, body) => {
  const res = await axiosInstance.post(REVIEW_URL + movieId + `/new/`, body)
  return res
}
const updateReview = async (movieId, body) => {
  const res = await axiosInstance.put(REVIEW_URL + movieId + `/new/`, body)
  return res
}





export {
  //auth
  login,
  signup,
  //account
  getMyInfo,
  fetchUserProfile,
  //movie
  fetchMovie,
  fetchMovieSearchList,
  fetchMovieList,
  fetchMovieRandom,
  fetchMovieRecommend,
  //people
  fetchActorSearchList,
  fetchActorDetail,
  //review
  fetchReviewList,
  fetchReviewGet,
  fetchUserReviewList,
  createReview,
  updateReview,
  reviewExist,
}