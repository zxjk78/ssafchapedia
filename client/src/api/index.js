import axios from 'axios'

const LOGIN_URL = '/dj-rest-auth/login/'
const SIGNUP_URL = '/dj-rest-auth/registration/'
const ARITICLE_LIST_URL = '/articles/'

const axiosInstance = axios.create({
  baseURL:'http://localhost:8000/api/v1',
})

axiosInstance.interceptors.request.use(
  (config)=>{
    const token = JSON.parse(localStorage.getItem('authToken'))
    if (token){
      config.headers.Authorization = `Token ${token}`
    }
    return config
  },
  (error)=>{
    return Promise.reject(error)
  },
)

const login = async (body) => {
  const res = await axiosInstance.post(LOGIN_URL, body)
  return res
}

const signup = async (body) => {
  const res = await axiosInstance.post(SIGNUP_URL, body)
  return res 
}

const fetchArticleList = async () => {
  const res = await axiosInstance.get(ARITICLE_LIST_URL)
  return res
}

export {
  login,
  signup,
  fetchArticleList,
}