<template>
    <div >
        <div class="bg-slider">
         <div class="container">
             <div class="row searchbox2" id="row-554569930">
                 <div class="col-12">

                             <div class="custom-search">
                                 <div class="text-field">
                                     <input type="text" value="" name="s" id="search" placeholder="نام کاربر مورد نظر را وارد نمایید"></div>
                                 <div class="search-top">
                                     <i class="fas fa-search"></i>
                                 </div>
                                 <p></p>
                             </div>

                     </div>


             </div>
         </div>
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
    background-image:url('../assets/images/header-min.jpg');
    height:700px;
}
.searchbox2 {
    position: absolute;
    bottom: 120px;
    left: 50%;
    width:60%;
    transform: translateX(-50%);
    background: #fff;
    padding-top: 14px;
    border-top-left-radius: 25px;
    border-bottom-left-radius: 25px;
    border-top-right-radius: 25px;
    border-bottom-right-radius: 25px;
    box-shadow: 3px 2px 20px 8px #2f064d29;
}
#homesearch .custom-search {
    display: table;
    border: 2px solid #c7cad7;
    border-radius: 15px;
    overflow: hidden;
    margin: 0 auto;
}
.search-top{
    color:purple;
    font-size:25px;
    float:left;
}

    .text-field{
        float:right;
        width:50%;
    }
</style>