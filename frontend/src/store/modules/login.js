import Service from '@/services/Service.js'
import router from'@/router'
export const namespaced = true

export const state = {
    user: null,
    username:'',
    posts:[],
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
    SET_POSTS(state,posts){
        state.posts=posts
    },

    DELETE_POST(state,id){
       let index= state.posts.findIndex(item=>item.id==id)
        state.posts.splice(index,1)
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
    },
    EDIT_POST(state,post){
        state.posts=[...state.posts.map(item=>item.id !== post.id ?  item:{...post})]
    },
    FILTER_POST(state,value){
        state.posts=value
        console.log('bnn',state.posts)
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
    },
    getPost({ commit, getters }, id) {

        let post = getters.getPostById(id)

        if (post) {
            commit('SET_POST', post)
            return post
        } else {
            return Service.getPost(id)
                .then(response => {
                    console.log('o',response)
                    commit('SET_POST', response.data)
                    return response.data
                })

        }
    },
    getUser ({ commit }) {
        return Service.getUser().then((res)=>{
            commit('SET_USERINFO',res.data)
            console.log('ll',res)
            if(!res.data.user.email)
            {
                let end =new Date(res.data.user.date_joined)
                const now=new Date()
                const distance=now.getTime()-end.getTime()
                const convertToDay=(24 * 60 * 60 *1000)
                const day=Math.floor(distance/convertToDay)
                console.log('day',day)
                if(day<=7){
                    commit('SET_CONFIRMDAY',day)
                }
                else{
                    commit('CLEAR_CONFIRMDAY')
                    router.push({name:'newEmail'})
                }
            }

        })
    },
    updateUser ({ commit },user) {
        return Service.updateUser(user).then((res)=>{
            commit('UPDATE_USERINFO',res.data)
            return res;
        })
    },
    editPost({ commit},post ) {

        return Service.editPost(post)
            .then((res) => {
                commit('EDIT_POST',post)
                return res
            })
            .catch(error => {
                console.log(error)
            })
    },
    filterPosts({ commit},value ) {
        return Service.filterPosts(value).then((res)=>{

            commit('FILTER_POST',res.data)
            return res
        }).catch((e)=>{
            console.log(e.response)
        })
    },





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
    posts(state){
        return state.posts
    },
    userInfo(state){
        return state.userInfo
    },
    getPostById:state=>id=>{
        return state.posts.find(post=>post.id===id)
    }
}