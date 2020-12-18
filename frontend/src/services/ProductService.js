import axios from 'axios'

const apiClient = axios.create({
    baseURL: `http://127.0.0.1:8000/`,
    withCredentials: false, // This is the default
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
    },

})

export default {

    createUser(user) {
        console.log(user)
        axios.post('http://127.0.0.1:8000/users/', user)
    },
    getProducts(perPage, page) {
        return apiClient.get('/products?_limit='+ perPage + '&_page=' + page)
    },
    getUser(id) {
        return apiClient.get('/users/'+ id)
    },
    removeProduct(id) {
          console.log(id)
        return apiClient.delete('/products/'+id)
    },
    editProduct(product) {

        return apiClient.patch('/products/'+product.id,{name:product.name,price:product.price,img:product.img,category:product.category})
    }
}
