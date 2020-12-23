import Service from '@/services/Service.js'
export const namespaced = true

export const state = {
    user: null,
    username:'',

}
export const mutations = {
    SET_USER_DATA (state, credentials) {
        state.user = credentials.userData
        console.log(credentials.userData)
        if(credentials.saveLog){
            localStorage.setItem('user', JSON.stringify(credentials.userData))
        }
        else{
                if(!localStorage.getItem('user'))
                {
                    sessionStorage.setItem('user', JSON.stringify(credentials.userData))
                }
        }
        // axios.defaults.headers.common['Authorization'] = `Token ${
        //     credentials.userData.token
        //     }`
        Service.setToken(credentials.userData.token)
    },
    CLEAR_USER_DATA () {
        localStorage.removeItem('user')
        sessionStorage.removeItem('user')
        location.reload()
    },
    SET_USERNAME(state,username){
        state.username=username
    }

}
export const actions= {
    login({commit},credentials){
       return Service.loginUser(credentials.user).then((res)=>{
           console.log('455',res)
            commit('SET_USER_DATA', {userData:res.data,saveLog:credentials.saveLog})
        })

    },
    logout ({ commit }) {
        commit('CLEAR_USER_DATA')
    },
    setUsername({commit},username){
        console.log('kkkkl',username)
        commit('SET_USERNAME',username)
    }
}
export const getters= {
    loggedIn (state) {
        return !!state.user
    },
    username(state){
        return state.username
    }
}