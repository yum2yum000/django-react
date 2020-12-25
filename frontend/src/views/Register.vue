<template>
    <div>
        <div class="page-wrapper bg-gra-02 p-t-130 p-b-100 font-poppins">
            <div class="wrapper wrapper--w680 p-3">
                <div class="card card-4">
                    <div class="card-body">
                        <h2 class="title text-right">فرم ثبت نام</h2>
                        <form @submit.prevent="register">
                            <div class="row row-space">
                                <div class="input-container">
                                    <BaseInput inputClass="input--style-4" label=" نام کاربری" v-model="user.username"  @blur="$v.user.username.$touch()"></BaseInput>
                                    <div v-if="$v.user.username.$error">
                                        <p class="text-right error" v-if="!$v.user.username.required">نام کاربری باید وارد شود</p>
                                    </div>
                                </div>
                                <div class="input-container">
                                    <BaseInput type="password" inputClass="input--style-4" label=" رمز عبور" v-model="user.password"  @blur="$v.user.password.$touch()"></BaseInput>
                                    <div v-if="$v.user.password.$error">
                                        <p class="text-right error" v-if="!$v.user.password.required"> رمز عبور باید وارد شود</p>
                                        <p class="text-right error" v-if="!$v.user.password.minLength"> رمز عبور باید حداقل 8 حرف باشد</p>
                                        <p class="text-right error" v-if="!$v.user.password.valid"> رمز عبور باید شامل حرف و  عدد باشد</p>
                                    </div>
                                </div>
                            </div>
                            <div class="row row-space">
                                <div class="input-container">
                                    <BaseInput type="email" inputClass="input--style-4" label="ایمیل" v-model="user.email"  @blur="$v.user.email.$touch()"></BaseInput>
                                    <div v-if="$v.user.email.$error">
                                        <p class="text-right error" v-if="!$v.user.email.required"> ایمیل باید وارد شود</p>
                                        <p class="text-right error" v-if="!$v.user.email.email"> ایمیل باید فرمت معتبر باشد</p>
                                        <p class="text-right error" v-if="!$v.user.email.valid"> ایمیل نمی تواند شامل حروف بزرگ باشد </p>
                                    </div>
                                </div>
                                <div class="input-container">
                                    <BaseInput type="text" inputClass="input--style-4" label="درباره شما" v-model="user.bio" ></BaseInput>
                                </div>
                            </div>

                            <div class="row row-space">
                                <div class="input-container">
                                    <BaseInput type="text" inputClass="input--style-4" label="نام" v-model="user.first_name" ></BaseInput>
                                </div>
                                <div class="input-container">
                                    <BaseInput type="text" inputClass="input--style-4" label="نام خانوادگی" v-model="user.last_name" ></BaseInput>
                                </div>
                            </div>



                            <div class="row row-space">
                                <div class="input-container">
                                    <div class="input-group">
                                        <BaseInput   type="text" inputClass="input--style-4" label="شماره موبایل" v-model="user.phone" ></BaseInput>
                                    </div>


                                </div>
                                <div class="input-container">
                                    <div class="input-group">
                                        <label class="label">آدرس</label>
                                        <textarea v-model="user.adres" class="textarea--style-4" type="text" ></textarea>
                                    </div>
                                </div>

                            </div>
                             <div v-if="error" class="text-right error">
                                 {{error}}
                             </div>
                            <div class="p-t-15 text-center ">
                                <BaseButton buttonClass="btn btn--radius-2 submit" type="submit" :disabled="$v.$anyError || buttonClick"  >ثبت نام</BaseButton>
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
    import Service from '@/services/Service.js'
    import store from '@/store/store'
    import { required,minLength,email } from 'vuelidate/lib/validators'
    export default {
        name: "Register",
        validations:{
            user:{
                username: { required },
                password: { required,minLength:minLength(8),
                    valid: function(value) {
                        const containsLetter = /[A-Za-z]/.test(value)
                        return containsLetter
                    }
                },
                email:{required,email,
                    valid: function(value) {
                        const containsLetter = /[A-Z]/.test(value)
                        return !containsLetter
                    }
                }

            }
        },
        data(){
            return{
                user:{},
                error:'',
                buttonClick:false

            }
        },
        methods:{
            register(){
            this.$v.$touch()
            if(!this.$v.$invalid){
            this.buttonClick=true;
            Service.createUser(this.user).then((res)=>{
                console.log('register success',res)
                if (res.status === 200){
                    this.error='ثبت نام با موفقیت انجام شد'
                    setTimeout(()=>{
                        console.log('233',res)
                        store.dispatch('login/login',{
                            user:{
                                username:this.user.username,
                                password:this.user.password
                            },
                            saveLog:null
                        }).then((res)=>{
                            console.log('login success',res)
                            this.$router.push({name:'home'})
                        }).catch((e)=>{
                            console.log('login failed',e.response)
                            if (e.response && e.response.status === 400) {
                                this.error='رمز عبور یا نام کاربری صحیح نمی باشد'

                            }
                        })
                    },1000)
                }

            }).catch((e)=>{
                console.log('register failed',e.response)
                this.buttonClick=false;
                if (e.response && e.response.status === 400) {
                    if(e.response.data.password)
                    {
                        this.error='رمز عبور قوی انتخاب نمایید'
                    }
                    else if(e.response.data.phone)
                    {
                        this.error='موبایل باید به طور صحیح وارد شود'
                    }
                    else
                    {
                        this.error='لطفا ورودی ها را کنترل نمایید.'
                    }

                }
                else if (e.response && e.response.status === 406) {
                    if(e.response.data.username)
                    {
                        this.error='نام کاربری  تکراری است'
                    }
                    else if(e.response.data.email)
                    {
                        this.error=' ایمیل تکراری است'
                    }

                }
            })
            }
          }

        }
    }
</script>

<style scoped>
.input-container{
    width:45%;
}
</style>