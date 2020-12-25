import Service from '@/services/Service.js'
export const namespaced = true

export const state = {
    username:'',
    posts:[],
    userInfo:''

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
    SET_POSTS(state,posts){
        state.posts=posts
    },
    DELETE_POST(state,id){
       let index= state.posts.findIndex(item=>item.id==id)
        state.posts.splice(index,1)
    },
    GET_USER(state,user){
        state.userInfo=user
    }


}
export const actions= {
    login({commit},credentials){
        console.log('333333',credentials)
       return Service.loginUser(credentials.user).then((res)=>{
           console.log('55',res)
            commit('SET_USER_DATA', {userData:res.data,saveLog:credentials.saveLog})
        })

    },
    logout ({ commit }) {
        commit('CLEAR_USER_DATA')
    },
     deletePost({commit},id){
         return Service.deletePost(id)
             .then(() => {

                 commit('DELETE_POST', id)
             })
             .catch(error => {
                 console.log(error)

             })
    },
    getPosts ({ commit }) {
        return Service.getPosts().then((res)=>{
            commit('SET_POSTS',res.data)
        })
    },
    getUser ({ commit }) {
        return Service.getUser().then((res)=>{
            commit('GET_USER',res.data)
        })
    }


}
export const getters= {
    loggedIn (state) {
        return !!state.user
    },
    userInfo(state){
        return state.userInfo
    },
    posts(state){
        return state.posts
    }
}