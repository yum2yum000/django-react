import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
//
import Register from './views/Register.vue'
import Login from './views/Login.vue'
import ProfileEdit from './views/profile/ProfileEdit.vue'
import ProfileUser from './views/profile/ProfileUser.vue'
import Profile from './views/profile/Profile.vue'
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
            path: '/login',
            name: 'login',
            component: Login,
            meta: { requiresVisitor: true }
        },
        {
            path: '/profile/',
            name: 'profile',
            component: Profile,
            redirect: "profile/user",
            meta: { requiresAuth: true },
            children:[
                {
                    path: 'edit/:id',
                    name: 'profileEdit',
                    component: ProfileEdit,
                    props:true,
                },
                {
                    path: 'user',
                    name: 'profileUser',
                    component: ProfileUser,
                    props:true,
                },


            ]

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

router.beforeEach((to, from, next) => {
    let loggedIn;
    if(localStorage.getItem('user')){
        loggedIn = localStorage.getItem('user')
    }
    else if(sessionStorage.getItem('user')){
        loggedIn = sessionStorage.getItem('user')
    }

    if (to.matched.some(record => record.meta.requiresAuth) && !loggedIn) {
        next('/')
    }
    else if (to.matched.some(record => record.meta.requiresVisitor)) {
        if (loggedIn) {
            next({
                path: '/',
            })
        }
       else{
            next()
       }
    }
    else{
        next()
    }
})

export default router
