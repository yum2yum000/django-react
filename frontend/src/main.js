import Vue from 'vue'
import App from './App.vue'
import router from './router'
Vue.config.productionTip = false
import Vuelidate from 'vuelidate'
Vue.use(Vuelidate)
Vue.component('BaseInput', BaseInput)
Vue.component('BaseButton',BaseButton)
import BaseInput from '@/components/BaseInput'
import BaseButton from '@/components/BaseButton'
import './assets/css/bootstrap.min.css';
import './assets/css/style.css';
import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'
new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
