import Service from '@/services/Service.js'
export const namespaced = true

export const state = {
    user: null,
    username:'',
    posts:[]

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
    SET_POSTS(state,posts){
        state.posts=posts
    },
    DELETE_POST(state,id){
       let index= state.posts.findIndex(item=>item.id==id)
        state.posts.splice(index,1)
    }

}
export const actions= {
    login({commit},credentials){
       return Service.loginUser(credentials.user).then((res)=>{
            commit('SET_USER_DATA', {userData:res.data,saveLog:credentials.saveLog})
        })

    },
    logout ({ commit }) {
        commit('CLEAR_USER_DATA')
    },
    setUsername({commit},username){
        commit('SET_USERNAME',username)
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
    }

}
export const getters= {
    loggedIn (state) {
        return !!state.user
    },
    username(state){
        return state.username
    },
    posts(state){
        return state.posts
    }
}