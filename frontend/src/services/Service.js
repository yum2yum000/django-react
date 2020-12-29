import apiClient from '@/services/config.js'
import axios from "axios"


export default {
    setToken (token) {
        apiClient.defaults.headers.common['Authorization'] = `Token ${token}`;

    },
    createUser(user) {
       return apiClient.post('/users/', user)
    },
    loginUser(user) {
        return apiClient.post('/users/login/', user)
    },
    getUser() {
        return apiClient.put('/users/profile/',{update:''})

    },
    getPosts(){
        return apiClient.get('/posts/user/')
    },
    getPost(id){
        return apiClient.get('/posts/user/'+id)
    },
    editPost(post){
        console.log('c',post)
        return apiClient.put('/posts/user/'+post.id+'/',{title:post.title,content:post.content})
    },
    updateUser(data){
        return apiClient.put('/users/profile/',{update:'data',...data
        })

    },
    updatePassword(data){
        console.log('899999',data)
        return apiClient.put('/users/profile/',{update:'password',...data
        })

    },
    // getProducts(perPage, page) {
    //     return apiClient.get('/products?_limit='+ perPage + '&_page=' + page)
    // },
    createPost(post){
        return apiClient.post('/posts/user/',post)
    },
    deletePost(id){
        return apiClient.delete('posts/user/'+id)
    },

    filterPosts(value){
        console.log('0',value)
        return axios.get('http://127.0.0.1:8000/posts/search/',{ params: {
                title: value,
                content: value,
            }}

        )
    }


}
