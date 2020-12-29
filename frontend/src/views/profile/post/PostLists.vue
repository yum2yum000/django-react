<template>
    <div class="col-md-12">
        <div class="hasshadow"><div>
            <div class="shadowhead">
               لیست پست ها
            </div>
            <span>جستجو</span>
            <input class="input--style-4" label="جستجو" type="text" @input="input">
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
        methods:{
            input(e){
                this.searchValue=e.target.value
                this.service()
            },

            fetchPosts(){
                store.dispatch('login/getPosts').then(()=>{


                }).catch(()=>{
                    this.error='مشکلی در دریافت اطلاعات رخ داده است'
                })
            },
            service(){
                if(this.searchValue!=='')
                {

                    store.dispatch('login/filterPosts',this.searchValue).then((res)=>{
                    console.log(res)
                })}
                else{
                    this.fetchPosts();
                }
            }
        },
        data(){
            return{
                error:'',
                value:'',
                searchValue:''

            }
        },
        computed: {
            ...mapGetters('login', ['posts'])
        },
        created(){
            this.fetchPosts();

        }
    }
</script>

<style scoped>

</style>