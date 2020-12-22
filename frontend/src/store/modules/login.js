import Service from '@/services/Service.js'
import axios from 'axios'
export const namespaced = true

export const state = {
    user: null

}
export const mutations = {
    SET_USER_DATA (state, credentials) {
        state.user = credentials.userData
        console.log(credentials.userData)
        if(credentials.saveLog){
            console.log('3333333333333')
            localStorage.setItem('user', JSON.stringify(credentials.userData))
        }
        else{
            sessionStorage.setItem('user', JSON.stringify(credentials.userData))
        }
        axios.defaults.headers.common['Authorization'] = `Token ${
            credentials.userData.token
            }`
        console.log(axios.defaults.headers)
    },
    CLEAR_USER_DATA () {
        localStorage.removeItem('user')
        sessionStorage.removeItem('user')
        location.reload()
    }

}
export const actions= {
    login({commit},credentials){
        console.log('credentials',credentials)
       return Service.loginUser(credentials.user).then((res)=>{
            commit('SET_USER_DATA', {userData:res.data,saveLog:credentials.saveLog})
        })

    },
    logout ({ commit }) {
        commit('CLEAR_USER_DATA')
    }
}
export const getters= {
    loggedIn (state) {
        return !!state.user
    }
}