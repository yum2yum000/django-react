<template>
    <div >
        <div class="bg-slider">

        </div>
        <div class="container">
                <div class="row justify-content-center mt-5">
                    <div class="col-lg-12">
                        <PostList :posts="posts"></PostList>
                    </div>
                </div>
        </div>

    </div>
</template>

<script>
    import {mapGetters} from 'vuex'
    import store from '@/store/store'
    import Service from '@/services/Service.js'
    import PostList from '@/components/post/PostList'
    export default {
        name: "Home",
        components: {
            PostList
        },
        computed: {
            ...mapGetters('login', ['loggedIn','userInfo'])
        },
        data(){
            return{
                posts:[]
            }
        },
        created(){
            if(this.loggedIn && !this.userInfo){
                store.dispatch('login/getUser')
            }
            Service.fetchAllPosts().then((res)=>{
                console.log(res)
                this.posts=res.data
            })
        },
        mounted () {
            window.scrollTo(0, 0)
        }

    }
</script>

<style scoped>
.bg-slider{
    background-image:url('../assets/images/banner.jpg');
    height:700px;
}
</style>