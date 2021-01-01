import Vue from 'vue'
import Vuex from 'vuex'

import * as login from '@/store/modules/login.js'
import * as post from '@/store/modules/post.js'


Vue.use(Vuex)

export default new Vuex.Store({
    modules:{
       login,post
    },
    state: {


    },


})
