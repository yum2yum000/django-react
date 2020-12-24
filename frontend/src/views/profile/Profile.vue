<template>
    <div class="profile">
        <div class="space-80"></div>
        <div class="container-all dashboard pr-2 pl-2">
            <div class="row">
                 <Sidebar></Sidebar>
                <div class="contentside">
                    <div class="row rtl">
                        <router-view></router-view>
                    </div>
                </div>
           </div>
        </div>
    </div>
</template>

<script>
    import Sidebar from '@/components/profile/Sidebar'
    import Service from '@/services/Service.js'

    export default {
        name: "Profile",
        components:{
            Sidebar
        },
        created(){

        },
        methods:{
            meh(){
                Service.getUser().then((res)=>{
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