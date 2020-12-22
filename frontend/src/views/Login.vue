<template>
    <div>
        <div class="page-wrapper bg-gra-02 p-t-130 p-b-100 font-poppins">
            <div class="wrapper wrapper--w680 p-3">
                <div class="card card-4">
                    <div class="card-body">
                        <h2 class="title text-right">فرم ورود</h2>
                        <form @submit.prevent="login">
                            <div class="row row-space">
                                <div class="input-container">
                                    <div class="input-group">
                                        <label class="label">نام کاربری</label>
                                        <input v-model="user.username" class="input--style-4" type="text" >
                                    </div>
                                </div>
                                <div class="input-container">
                                    <div class="input-group">
                                        <label class="label">رمز عبور</label>
                                        <input v-model="user.password" class="input--style-4" type="password" >
                                    </div>
                                </div>
                                <label >
                                    <input type="checkbox" name="rememberme" v-model="saveLog" style="width:20px">
                                    <span class="um-field-checkbox-option"> مرا به خاطر بسپار</span>
                                </label>
                            </div>


                            <div class="p-t-15 text-center">
                                <button class="btn btn--radius-2 submit">ورود</button>
                            </div>
                            <div class="text-center mt-4 home">
                                <router-link to="/">بازگشت به صفحه اصلی</router-link>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

    import { required } from 'vuelidate/lib/validators'
    import store from '@/store/store'
    export default {
        name: "Login",
        validations:{
            user:{
                username: { required },
                password: { required }

            }
        },
        data(){
            return{
                user:{},
                saveLog:false
            }
        },
        methods:{
           login(){
               store.dispatch('login/login',{
                   user:this.user,
                   saveLog:this.saveLog
               }).then((res)=>{
                   console.log('hhhhh',res)
                   this.$router.push({name:'home'})
               }).catch((e)=>console.log(e.response))
           }

        }
    }
</script>

<style scoped>
    .input-container{
        width:100%;
    }

</style>