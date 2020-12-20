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
                                        <p class="text-right error" v-if="!$v.user.password.containsNumberLetter"> رمز عبور باید شامل حرف و  عدد باشد</p>
                                    </div>
                                </div>
                            </div>
                            <div class="row row-space">
                                <div class="input-container">
                                    <BaseInput type="text" inputClass="input--style-4" label="نام" v-model="user.first_name" ></BaseInput>
                                </div>
                                <div class="input-container">
                                    <div class="input-group">
                                        <label class="label">نام خانوادگی</label>
                                        <input v-model.trim="user.last_name" class="input--style-4" type="text" >
                                    </div>
                                </div>
                            </div>

                            <div class="row row-space">
                                <div class="input-container">
                                    <div class="input-group">
                                        <label class="label">شماره تلفن</label>
                                        <input v-model="user.phone" class="input--style-4" type="text" >
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
                                <BaseButton buttonClass="btn btn--radius-2 submit" type="submit" :disabled="$v.$anyError"  >ثبت نام</BaseButton>
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
    import { required,minLength } from 'vuelidate/lib/validators'
    export default {
        name: "Register",
        validations:{
            user:{
                username: { required },
                password: { required,minLength:minLength(8),
                    valid: function(value) {
                        const containsLetter = /[A-Za-z]/.test(value)
                        const containsNumber = /(?=.*\d)/.test(value)
                        console.log(containsNumber && containsLetter)
                        return containsNumber && containsLetter
                    }
                }

            }
        },
        data(){
            return{
                user:{},
                error:'',

            }
        },
        methods:{
            register(){
            this.$v.$touch()
            if(!this.$v.$invalid){

            Service.createUser(this.user).then((res)=>{
                if (res.status === 200){
                    this.error='ثبت نام با موفقیت انجام شد'
                    setTimeout(()=>{
                        this.$router.push({name:'login'})
                    },1000)
                }

            }).catch((e)=>{
                if (e.response && e.response.status === 400) {
                    console.log(e.response.data)
                    this.error='لطفا ورودی ها را کنترل نمایید.'
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