import axios from 'axios'

const LOGIN_URL = '/accounts/login/'
const SIGNUP_URL = '/accounts/signup/'
const ARTICLE_LIST_URL = '/articles/'

// movie
const MOVIE_SEARCH_LIST_URL = '/movies/search'
const MOVIE_URL = '/movies/movie'
// actor
const ACTOR_SEARCH_LIST_URL = '/people/search'

// review
const REVIEW_LIST_URL = '/reviews/'
const REVIEW_CREATE_URL = '/reviews/new/'
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


//account

const login = async (body) => {
  const res = await axiosInstance.post(LOGIN_URL, body)
  return res
}

const signup = async (body) => {
  const res = await axiosInstance.post(SIGNUP_URL, body)
  return res 
}

//movie

const fetchArticleList = async () => {
  const res = await axiosInstance.get(ARTICLE_LIST_URL)
  return res
}
const fetchMovieSearchList = async (keyword) => {
  const res = await axiosInstance.get(MOVIE_SEARCH_LIST_URL, {params:{keyword: keyword}})
  return res
}
const fetchMovie = async (movieId) => {
  const movieURL = MOVIE_URL + `/${movieId}/`
  const res = await axiosInstance.get(movieURL)
  return res
}


//people

const fetchActorSearchList = async (keyword) => {
  const res = await axiosInstance.get(ACTOR_SEARCH_LIST_URL, {params:{keyword: keyword}})
  return res
}


//review

const fetchReviewList = async () => {
  const res = await axiosInstance.get(REVIEW_LIST_URL)
  return res
}

const createReview = async (body) => {
  const res = await axiosInstance.post(REVIEW_CREATE_URL, body)
  return res
}





export {
  //account
  login,
  signup,
  //movie
  fetchMovie,
  fetchMovieSearchList,
  fetchArticleList,
  //people
  fetchActorSearchList,
  //review
  fetchReviewList,
  createReview,
}