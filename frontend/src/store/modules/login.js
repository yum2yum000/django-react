import Service from '@/services/Service.js'
import router from'@/router'
export const namespaced = true

export const state = {
    user: null,
    username:'',
    userInfo:'',
    mailConfirm:'',
    confirmDay:-1

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
        Service.setToken(credentials.userData.token)
    },
    CLEAR_USER_DATA () {
        localStorage.removeItem('user')
        sessionStorage.removeItem('user')
        location.reload()
    },
    SET_USERNAME(state,username){
        state.username=username
    },

    SET_USERINFO(state,userInfo){
        state.userInfo=userInfo.user
        if(userInfo.user.email){
            state.mailConfirm=true
        }
        else{
            state.mailConfirm=false
        }
    },
    UPDATE_USERINFO(state,data){
        state.userInfo=data.user
    },
    SET_CONFIRMDAY(state,day){
        state.confirmDay=7-day
    },
    CLEAR_CONFIRMDAY(state){
        state.confirmDay=-1
    }

}
export const actions= {
    login({commit}, credentials) {
        return Service.loginUser(credentials.user).then((res) => {
            commit('SET_USER_DATA', {userData: res.data, saveLog: credentials.saveLog})
        })

    },
    logout({commit}) {
        commit('CLEAR_USER_DATA')
    },
    setUsername({commit}, username) {
        commit('SET_USERNAME', username)
    },
    getUser({commit}) {
        return Service.getUser().then((res) => {
            commit('SET_USERINFO', res.data)
            console.log('user',res.data)
            if (!res.data.user.email) {
                let end = new Date(res.data.user.date_sent)
                const now = new Date()
                const distance = now.getTime() - end.getTime()
                const convertToDay = (24 * 60 * 60 * 1000)
                const day = Math.floor(distance / convertToDay)
                console.log('day', day)
                if (day <= 7) {
                    commit('SET_CONFIRMDAY', day)
                } else {
                    commit('CLEAR_CONFIRMDAY')
                    router.push({name: 'newEmail'})
                }
            }

        })
    },
    updateUser({commit}, user) {
        return Service.updateUser(user).then((res) => {
            commit('UPDATE_USERINFO', res.data)
            return res;
        })
    }

}
export const getters= {
    loggedIn (state) {
        return !!state.user
    },
   mailConfirm (state) {
        return !!state.mailConfirm
    },
    username(state){
        return state.username
    },
    confirmDay(state){
        return state.confirmDay
    },
    userInfo(state){
        return state.userInfo
    }
}