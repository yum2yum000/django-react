import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
//
import Register from './views/Register.vue'
//
// import Loading from 'vue-loading-overlay';
import NotFound from './views/NotFound'


Vue.use(Router)



const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/register',
            name: 'register',
            component: Register
        },

        {
            path: '/404',
            name: '404',
            component: NotFound
        },

        {
            path:'*',
            redirect:{name:'404'}
        }


    ]
})



export default router
