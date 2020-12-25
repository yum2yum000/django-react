import apiClient from '@/services/config.js'


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
    updateUser(data){
        return apiClient.put('/users/profile/',{update:'data',...data
        })

    },
    updatePassword(data){
        console.log('899999',data)
        return apiClient.put('/users/profile/',{update:'password',...data
        })

    },
    getProducts(perPage, page) {
        return apiClient.get('/products?_limit='+ perPage + '&_page=' + page)
    },
    createPost(post){
        return apiClient.post('/posts/user/',post)
    },
    deletePost(id){
        return apiClient.delete('posts/user/'+id)
    },

    removeProduct(id) {
          console.log(id)
        return apiClient.delete('/products/'+id)
    },
    editProduct(product) {

        return apiClient.patch('/products/'+product.id,{name:product.name,price:product.price,img:product.img,category:product.category})
    }
}
