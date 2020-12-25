<template>
    <div class="col-md-12">
        <div class="hasshadow"><div>
            <div class="shadowhead">
                ویرایش اطلاعات
            </div>
            <div class="row justify-content-center mt-5">
                <div class="col-lg-12">
                    <PostList :posts="posts"></PostList>
                </div>
            </div>
        </div>
        </div>
    </div>

</template>

<script>
    import PostList from '@/components/post/PostList'
    import store from '@/store/store'
    import {mapGetters} from 'vuex'
    export default {
        name: "PostLists",
        components: {
            PostList
        },
        data(){
            return{
                error:'',

            }
        },
        computed: {
            ...mapGetters('login', ['posts'])
        },
        created(){
            store.dispatch('login/getPosts').then(()=>{


            }).catch(()=>{
                this.error='مشکلی در دریافت اطلاعات رخ داده است'
            })

        }
    }
</script>

<style scoped>

</style>