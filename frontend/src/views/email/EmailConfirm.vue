<template>
    <div>
        <div class="page-wrapper bg-gra-02 p-t-130 p-b-100 font-poppins">
            <div class="wrapper wrapper--w680 p-3">
                <div class="card card-4">
                    <div class="card-body">
                        <h2 class="title text-right">تبریک</h2>

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