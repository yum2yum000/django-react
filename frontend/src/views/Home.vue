<template>
    <div >
        <div class="bg-slider">

        </div>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex'
    import store from '@/store/store'
    export default {
        name: "Home",
        computed: {
            ...mapGetters('login', ['loggedIn'])
        },
        created(){
            if(this.loggedIn){
                store.dispatch('login/getUser')
            }
        }

    }
</script>

<style scoped>
.bg-slider{
    background-image:url('../assets/images/banner.jpg');
    height:700px;
}
</style>