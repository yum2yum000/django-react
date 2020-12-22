<template>
    <div>
        <div class="page-wrapper bg-gra-02 p-t-130 p-b-100 font-poppins">
            <div class="wrapper wrapper--w680 p-3">
                <div class="card card-4">
                    <div class="card-body">

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

    import { required } from 'vuelidate/lib/validators'
    import axios from 'axios'
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
            login(){
                axios.put("http://127.0.0.1:8000/users/login/",{bio:'passwor766d'}).then((res)=>
                {console.log(res)})
                    .catch((e)=>{
                    console.log('kkkk')
                    console.log(e.reponse)
                })
            }

        }
    }
</script>

<style scoped>
    .input-container{
        width:100%;
    }

</style>