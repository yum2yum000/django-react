<template>
    <div class="col-md-12">
        <div class="hasshadow"><div>
            <div class="shadowhead">
                ویرایش رمز عبور
            </div>
            <div class="row justify-content-center mt-5">
                <div class="col-lg-12">
                    <form @submit.prevent="update">
                        <div class="row">
                            <div class="col-lg-6">
                                <div class="input-container">
                                    <BaseInput type="password" inputClass="input--style-4" label="رمز عبور جدید" v-model="user.password"  @blur="$v.user.password.$touch()" ></BaseInput>
                                    <div v-if="$v.user.password.$error">
                                    <p class="text-right error" v-if="!$v.user.password.required"> رمز عبور باید وارد شود</p>
                                    <p class="text-right error" v-if="!$v.user.password.minLength"> رمز عبور باید حداقل 8 حرف باشد</p>
                                    <p class="text-right error" v-if="!$v.user.password.valid"> رمز عبور باید شامل حرف باشد</p>
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
    import { required,minLength } from 'vuelidate/lib/validators'
    import Service from '@/services/Service.js'
    export default {
        name: "ProfileEdit",
        validations:{
            user:{
                password: { required,minLength:minLength(8),
                    valid: function(value) {
                        const containsLetter = /[A-Za-z]/.test(value)
                        return containsLetter
                    }
                },
            }
        },
        data(){
            return{
               user:{},
                error:''
            }
        },
        methods:{
            update(){
                this.$v.$touch()
                if(!this.$v.$invalid){
                Service.updatePassword(this.user).then((res)=>{
                    if (res.status === 200){
                        this.error='اطلاعات با موفقیت ویرایش شد'
                    }
                }).catch((e)=>{
                    console.log(e.response)
                    if (e.response && e.response.status === 400) {

                        if(e.response.data.password)
                        {
                            this.error='ایمیل  تکراری است'
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