<template>
    <div class="col-md-12">
        <div class="hasshadow"><div>
            <div class="shadowhead">
               لیست پست ها
            </div>
            <BaseInput @keyup="fetchPosts" type="text" inputClass="input--style-4" label="جستجو" v-model="value" ></BaseInput>
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
    import Service from '@/services/Service'

    import {mapGetters} from 'vuex'
    export default {
        name: "PostLists",
        components: {
            PostList
        },
        methods:{
            fetchPosts(){
                console.log(this.value)
               Service.filterPosts(this.value).then((res)=>{
                    console.log(res)
                }).catch((e)=>{
                    console.log(e.response)
               })
            }
        },
        data(){
            return{
                error:'',
                value:''

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