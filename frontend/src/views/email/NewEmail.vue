<template>
    <div>
        <div class="page-wrapper bg-gra-02 p-t-130 p-b-100 font-poppins">
            <div class="wrapper wrapper--w680 p-3">
                <div class="card card-4">
                    <div class="card-body">
                        <h2 class="title text-right">ایمیل جدید</h2>
                        <form @submit.prevent="register">
                            <!--<div class="row row-space">-->
                                <!--<div class="input-container">-->
                                    <!--<BaseInput inputClass="input&#45;&#45;style-4" label=" نام کاربری"   ></BaseInput>-->
                                    <!--&lt;!&ndash;<div v-if="$v.user.username.$error">&ndash;&gt;-->
                                        <!--&lt;!&ndash;<p class="text-right error" v-if="!$v.user.username.required">نام کاربری باید وارد شود</p>&ndash;&gt;-->
                                    <!--&lt;!&ndash;</div>&ndash;&gt;-->
                                <!--</div>-->

                            <!--&lt;!&ndash;<div class="p-t-15 text-center ">&ndash;&gt;-->
                                <!--&lt;!&ndash;<BaseButton buttonClass="btn btn&#45;&#45;radius-2 submit" type="submit" :disabled="$v.$anyError || buttonClick"  >ثبت نام</BaseButton>&ndash;&gt;-->
                            <!--&lt;!&ndash;</div>&ndash;&gt;-->
                            <!--<div class="text-center mt-4 home">-->
                                <!--<router-link to="/">بازگشت به صفحه اصلی</router-link>-->
                            <!--</div>-->
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

    export default {
        name: "Register",
        data(){
            return{
                user:{},
                error:'',
                buttonClick:false

            }
        },
        methods:{
            register(){
            console.log('f')

                }




        }
    }
</script>

<style scoped>
.input-container{
    width:45%;
}
</style>