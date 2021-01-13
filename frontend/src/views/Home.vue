<template>
    <div >
        <div class="bg-slider">
            <div class="container">
                <div class="row searchbox2" id="row-554569930">
                    <div class="col-12">

                        <div class="custom-search">
                            <div class="text-field">
                                <multiselect @open="asyncFind" placeholder="نام کاربر مورد نظر خود را وارد کنید"
                                             v-model="user"
                                             :options="options"
                                             :selectLabel=" meh"
                                             :hide-selected="true"
                                             selectedLabel="انتخاب شده"
                                             deselectLabel="حذف"
                                             label="username"
                                             track-by="name"
                                             openDirection="bottom"
                                             :showNoOptions="false"
                                             :optionHeight="7"


                                >
                                    <template slot="noResult">گزینه‌ای یافت نشد</template>

                                </multiselect>
                            </div>
                            <div class="search-top">
                                <i class="fas fa-search"></i>
                            </div>
                            <p></p>
                        </div>

                    </div>


                </div>
            </div>
        </div>

        <div class="container latest-top">
            <div class="row justify-content-center mt-5">
                <div class="col-lg-12 text-center">
                    <span class="latest">  آخرین مطالب</span>
                </div>
            </div>
        </div>
        <div class="container">
            <div class="row justify-content-center mt-5 mb-3">
                <div class="col-lg-6 mb-5">
                    <div class="row searchbox3" id="row-554569930">
                        <div class="col-12">
                            <div class="custom-search">
                                <div class="text-field">
                                    <input @input="input" type="text"  placeholder="جستجو در بین مطالب..."></div>
                                <div class="search-top">
                                    <i class="fas fa-search"></i>
                                </div>
                                <p></p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-12" id="posts">
                    <PostList :results="posts.results"></PostList>
                    <div class="load-wrapp" v-if="isLoading">
                        <div class="load-1">
                            <div class="line"></div>
                            <div class="line"></div>
                            <div class="line"></div>
                        </div>
                    </div>
                    <div class="text-center mt-5" v-if="!scroll &&!filter">دیگر اطلاعاتی برای نمایش وجود ندارد </div>
                    <div class="text-center mt-5" v-if="noData">داده ای یافت نشد </div>

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
    import Multiselect from 'vue-multiselect'
    export default {
        name: "Home",
        components: {
            PostList,Multiselect
        },
        data(){
            return{
                posts:{
                    results:[

                    ]
                },

                perPage: 2,
                eventsTotal:'',
                currentPage:0,
                count:'',
                filter:false,
                isLoading:false,
                scroll:true,
                noData:false,
                searchValue:'',
                options: [
                ],
                searchData:true,
                meh:'',
                user: null,
            }
        },
        created(){
            if(this.loggedIn && !this.userInfo){
                store.dispatch('login/getUser')
            }
            this.fetchPosts()
            window.addEventListener('scroll', this.infiniteScroll)
        },
        mounted () {
            window.scrollTo(0, 0)
        },
        computed: {
            ...mapGetters('login', ['loggedIn','userInfo']),

        },
        watch:{
            user:function(value){
                this.$router.push({ name: 'profileUser', params: { id: value.id } })
            },
        },
        methods:{
            service(){
                if(this.searchValue!=='')
                {
                    store.dispatch('post/filterPosts',this.searchValue).then((res)=>{
                         this.filter=true
                        this.scroll=false

                        this.posts.results=res?.data
                        if(this.posts.results.length>=1){
                            this.noData=false
                        }
                        else{
                            this.noData=true
                        }
                    })
                }
                else{
                    this.posts.results=[]
                    this.scroll=true
                    this.noData=false
                    this.filter=false
                    this.currentPage=0
                    this.fetchPosts();
                }
            },
            fetchPosts(){
                Service.fetchAllPosts(
                    this.perPage,
                    this.currentPage,
                ).then((res)=>{
                    console.log('reees',res)
                    if (res.data.results.length >=1 ) {
                        res.data.results.forEach((item) =>
                            this.posts.results.push(item))
                        this.isLoading=false
                    }
                    else {
                        this.isLoading=false
                        this.scroll=false
                    }

                })
            },
            input(e){
                this.searchValue=e.target.value
                this.service()
            },
            infiniteScroll(){
                window.onscroll=()=>{
                    const { scrollTop, scrollHeight, clientHeight } = document.documentElement;
                    if ((scrollTop + clientHeight >= scrollHeight - 30) && this.scroll) {
                        console.log('vian1',this.count)
                        console.log('vian2',this.perPage*this.currentPage)
                                this.isLoading=true
                            setTimeout(() => {
                                this.currentPage++;
                                this.fetchPosts()

                            },500
                        )

                    }
                }

            },
            asyncFind () {
                if(this.searchData==true)
                {

                    Service.getAll(
                    ).then((res)=>{

                        this.options=res.data
                        this.searchData=false

                    }).catch(()=>{

                    })
                }

            }


        },
        destroyed () {
            window.removeEventListener('scroll', this.infiniteScroll);
        },

    }
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
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
    .load-1 .line:nth-last-child(1) {
        animation: loadingA 1.5s 1s infinite;
    }
    .load-1 .line:nth-last-child(2) {
        animation: loadingA 1.5s 0.5s infinite;
    }
    .load-1 .line:nth-last-child(3) {
        animation: loadingA 1.5s 0s infinite;
    }

    .line {
        display: inline-block;
        width: 15px;
        height: 15px;
        border-radius: 15px;
        margin-right:5px;
        background-color: #301d47;
    }
    .load-wrapp{
        margin-top: 44px;
        text-align: center;
        height: 10px;
        display: flex;
        justify-content: center;
    }
    @keyframes loadingA {
    0 {
        height: 15px;
    }
    50% {
        height: 35px;
    }
    100% {
        height: 15px;
    }
    }
    .latest{
        border-bottom: 2px solid purple;
    }


</style>