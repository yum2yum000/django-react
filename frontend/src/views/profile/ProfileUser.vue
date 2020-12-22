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
    import Service from '@/services/Service.js'
    import store from '@/store/store'
    export default {
        name: "ProfileUser",
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
            }
        },
        created(){
          this.getUser()
        },
        methods:{
            getUser(){
                Service.getUser().then((res)=>{
                    let user=res.data.user
                    this.user.last_name=user.last_name
                    this.user.first_name=user.first_name
                    this.user.email=user.email
                    this.user.bio=user.bio
                    this.user.adres=user.adres
                    this.user.phone=user.phone
                    console.log('this/user',this.user)
                    store.dispatch('login/setUsername',this.user.username)
                }).catch((e)=>{
                    console.log(e.response)
                })
            },
            update(){
                Service.updateUser(this.user).then((res)=>{
                    console.log(res)
                }).catch((e)=>{
                    console.log(e.response)
                })
            }
        }
    }
</script>

<style scoped>

</style>