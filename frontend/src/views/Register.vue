<template>
    <div>
        <div class="page-wrapper bg-gra-02 p-t-130 p-b-100 font-poppins">
            <div class="wrapper wrapper--w680">
                <div class="card card-4">
                    <div class="card-body">
                        <h2 class="title text-right">فرم ثبت نام</h2>
                        <form @submit.prevent="add">
                            <div class="row row-space">
                                <div class="input-container">
                                    <div class="input-group">
                                        <label class="label">نام</label>
                                        <input v-model="user.first_name" class="input--style-4" type="text" >
                                    </div>
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
                                        <label class="label">نام کاربری</label>
                                        <input v-model="$v.user.username.$model" class="input--style-4" type="text" >
                                    </div>
                                </div>
                                <div class="input-container">
                                    <div class="input-group">
                                        <label class="label">رمز عبور</label>
                                        <input v-model="user.password" class="input--style-4" type="password" >
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
                                        <input v-model="user.adres" class="input--style-4" type="text" >
                                    </div>
                                </div>
                            </div>

                            <div class="p-t-15">
                                <button class="btn btn--radius-2 btn--blue">ثبت نام</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import UserService from '@/services/UserServices.js'
    import { required } from 'vuelidate/lib/validators'
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
                user:{}
            }
        },
        methods:{
            add(){
                UserService.createUser(this.user).then((res)=>{
                    console.log(res)
                });

            }
        }
    }
</script>

<style scoped>
.input-container{
    width:45%;
}
</style>