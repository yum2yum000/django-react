<template>

        <div>
            <div class="box">
                <i class="fas fa-quote-left quote" aria-hidden="true" style="font-size:12px;color:#c5245e"></i>
                <p class="content">{{title}} </p>
                <p >{{content}}</p>
                <div class="content">
                    <div class="info">
                        <div class="job">
                            <router-link to="/"> <i class="fas fa-edit"></i> </router-link>
                            <span class="delete" @click="deletePost(id)"><i class="fas fa-trash mr-2" ></i></span>
                            <!--<DeleteModal class="delete"></DeleteModal>-->

                        </div>
                    </div>
                </div>
            </div>
        </div>


</template>

<script>

    import store from '@/store/store'
    export default {
        name: "PostPreview",
        components:{

        },
        props:{
            id: {
                type: String,
                required: true
            },
            title:{
                type: String,
                required: true
            },
            content:{
                type: String,
                required: true
            }

        },
        methods:{
            deletePost(id){
                store.dispatch('login/deletePost',id).then(()=>{


                }).catch(()=>{
                    this.error='مشکلی در دریافت اطلاعات رخ داده است'
                })
            }
        }
    }
</script>

<style scoped>
        .box {
            background: #fff;
            border-radius: 3px;
            padding: 25px;
            -webkit-box-shadow: 7px 5px 30px rgba(72,73,121,0.15);
            box-shadow: 7px 5px 30px rgba(72,73,121,0.15);

        }
        .box i.quote {
            font-size: 20px;
            color: #17a2b8;
        }
        .box .content {
            padding-top: 10px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
    .content{
        display: inline-block!important;
        margin-right: 10px;
    }
    .info{
        position: absolute;
        left: 32px;
    }
    .delete{
        cursor:pointer;
        color:#c5245e;
    }

</style>