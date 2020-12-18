import axios from 'axios'

const apiClient = axios.create({
    baseURL: `http://127.0.0.1:8000/`,
    withCredentials: false, // This is the default
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
    },

})

export default apiClient
