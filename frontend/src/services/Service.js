import axios from 'axios'

const apiClient = axios.create({
    baseURL: `http://127.0.0.1:8000/`,
    withCredentials: false, // This is the default
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',

    },

})


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
        return apiClient.put('/users/login/',{update:''})

    },
    updateUser(data){
        console.log('899999',data)
        return apiClient.put('/users/login/',{update:'data',...data
        })

    },
    getProducts(perPage, page) {
        return apiClient.get('/products?_limit='+ perPage + '&_page=' + page)
    },

    removeProduct(id) {
          console.log(id)
        return apiClient.delete('/products/'+id)
    },
    editProduct(product) {

        return apiClient.patch('/products/'+product.id,{name:product.name,price:product.price,img:product.img,category:product.category})
    }
}
