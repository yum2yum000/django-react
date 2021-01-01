import axios from 'axios'
import { baseUrl } from '@/config'

const apiClient = axios.create({
    baseURL: baseUrl,
    withCredentials: false, // This is the default
    headers: {
        Accept: 'application/json',



    },

})

export default apiClient