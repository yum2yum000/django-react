<template>
    <div>
        <div class="page-wrapper bg-gra-02 p-t-130 p-b-100 font-poppins">
            <div class="wrapper wrapper--w680 p-3">
                <div class="card card-4">
                    <div class="card-body">
                        <h2 class="title text-right">فرم ورود</h2>
                       <app-form :onSubmit="login">
                            <div class="row row-space">
                                <div class="input-container">
                                        <BaseInput label="نام کاربری" v-model="user.username" inputClass="input--style-4" type="text"></BaseInput>
                                </div>
                                <div class="input-container" style="position:relative">
                                        <BaseInput  label="رمز عبور" v-model="user.password" inputClass="input--style-4" type="password"></BaseInput>
                                        <span class="showpassword" @mouseover="showText" @mouseleave="showPassword"> <i class="fas fa-eye eye-password" ></i></span>
                                </div>
                                <label >
                                    <input type="checkbox" name="rememberme" v-model="saveLog" style="width:20px">
                                    <span class="um-field-checkbox-option"> مرا به خاطر بسپار</span>
                                </label>
                            </div>


                            <div class="p-t-15 text-center">
                                <button class="btn btn--radius-2 submit">ورود</button>
                            </div>
                            <div v-if="error" class="text-right error mt-3">
                                {{error}}
                            </div>
                       </app-form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import AppForm from '@/components/ui/AppForm'
    import { required } from 'vuelidate/lib/validators'
    import store from '@/store/store'
    export default {
        name: "Login",
        components:{
            AppForm
        },
        validations:{
            user:{
                username: { required },
                password: { required }

            }
        },
        data(){
            return{
                user:{},
                saveLog:false,
                error:'',
                buttonClick:false,
                passwordFieldType:'password'
            }
        },
        watch:{
            user: {
                handler() {
                    this.error=''
                },
                deep: true
            }
        },
        methods:{
            showText(){
                this.passwordFieldType='text'
            },
            showPassword(){
                this.passwordFieldType='password'
            },
           login(){
               store.dispatch('login/login',{
                   user:this.user,
                   saveLog:this.saveLog
               }).then((res)=>{
                   console.log('login success',res)
                   this.$router.push({name:'home'})
               }).catch((e)=>{
                   console.log('login failed',e.response)
                   if (e.response && e.response.status === 400) {
                           this.error=e.response.data.error

                   }
               })
           }

        }
    }
</script>

<style scoped>
    .input-container{
        width:100%;
    }
    .eye-password{
        position: absolute;
        top: 46px;
        left: 11px;
    }



</style>