<template>
    <div class="col-md-12">
        <div class="hasshadow"><div>
            <div class="shadowhead">
                ویرایش اطلاعات
            </div>
            <div class="row justify-content-center mt-5">
                <div class="col-lg-12">
                    <form @submit.prevent="update">
                        <div class="row">
                            <div class="col-lg-6">
                                <div class="input-container">
                                    <BaseInput type="text" inputClass="input--style-4" label="نام" v-model="user.first_name" ></BaseInput>
                                </div>
                            </div>
                            <div class="col-lg-6">
                                <BaseInput type="text" inputClass="input--style-4" label="نام خانوادگی" v-model="user.last_name" ></BaseInput>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-lg-6">
                                <div class="input-container">
                                    <BaseInput type="text" inputClass="input--style-4" label="درباره شما" v-model="user.bio" ></BaseInput>
                                </div>
                            </div>

                            <div class="col-lg-6">
                                <div class="input-container">
                                    <BaseInput type="text" inputClass="input--style-4" label="شماره تلفن" v-model="user.phone" ></BaseInput>
                                </div>
                            </div>

                        </div>
                        <div class="row ">
                            <div class="col-lg-6">
                                <div class="input-container">
                                    <label class="label">آدرس</label>
                                    <textarea v-model="user.adres" class="textarea--style-4" type="text" ></textarea>
                                </div>
                            </div>

                            <div class="col-lg-6">
                                <div class="input-container">
                                    <BaseInput type="email" inputClass="input--style-4" label="ایمیل" v-model="user.email"  @blur="$v.user.email.$touch()"></BaseInput>
                                    <div v-if="$v.user.email.$error">
                                        <p class="text-right error" v-if="!$v.user.email.required"> ایمیل باید وارد شود</p>
                                        <p class="text-right error" v-if="!$v.user.email.email"> ایمیل باید فرمت معتبر باشد</p>
                                    </div>
                                </div>
                            </div>

                        </div>
                        <div v-if="error" class="text-right error mt-2 mr-3">
                            {{error}}
                        </div>
                        <div class="p-t-15 text-center ">
                            <BaseButton buttonClass="btn btn--radius-2 submit" type="submit"   >ویرایش</BaseButton>
                        </div>

                    </form>
                </div>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
    import { required,email } from 'vuelidate/lib/validators'
    import {mapGetters} from 'vuex'
    import store from '@/store/store'

    export default {
        name: "ProfileEdit",
        validations:{
            user:{
                email:{required,email}
            }
        },
        data(){
            return{
                user:{
                    first_name:'',
                    last_name:'',
                    bio:'',
                    email:'',
                    phone:'',
                    adres:'',
                },
                error:''
            }
        },
        computed: {
            ...mapGetters('login', ['userInfo'])
        },
        created(){
            this.getUser()
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
            getUser(){
                  if(this.userInfo)
                  {
                      this.setInfUser()
                  }
                  else{
                      store.dispatch('login/getUser').then(()=>{
                          this.setInfUser()
                      })
                  }

            },
            setInfUser(){
                let user=this.userInfo
                this.user.last_name=user.last_name
                this.user.first_name=user.first_name
                this.user.email=user.email
                this.user.bio=user.bio
                this.user.adres=user.adres
                this.user.phone=user.phone
            },
            update(){
                this.$v.$touch()
                if(!this.$v.$invalid){
                    store.dispatch('login/updateUser',this.user).then((res)=>{
                        if (res.status === 200){
                            this.error='اطلاعات با موفقیت ویرایش شد'
                        }
                    }).catch((e)=>{
                        console.log(e.response)
                        if (e.response && e.response.status === 400) {
                            if(e.response.data.email)
                            {
                                this.error=e.response.data.email
                            }
                            else if(e.response.data.phone)
                            {
                                this.error=e.response.data.phone
                            }
                            else{
                                this.error='لطفا ورودی ها را کنترل نمایید'
                            }


                        }
                    })

            }
            }
        }
    }
</script>

<style scoped>

</style>