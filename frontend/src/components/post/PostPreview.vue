<template>

        <div>
            <div class="box">
                <i class="fas fa-quote-left quote" aria-hidden="true" style="font-size:12px;color:#c5245e"></i>
                <p class="content">{{title}} </p>
                <p >{{content}}</p>
                <div class="content">
                    <div class="info">
                        <div class="job">
                            <router-link :to="{ name: 'postEdit', params: { id: id } }"> <i class="fas fa-edit"></i> </router-link>


                            <div  class="uk-container uk-container-center uk-margin-top">
                                <span @click="showModal = true" class="uk-button uk-button-primary delete" ><i class="fas fa-trash mr-2" ></i></span>
                                <DeleteModal @apply="deletePost(id)" class="delete" @closeModal="showModal=false" :show="showModal">
                                </DeleteModal>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </div>


</template>

<script>

    import store from '@/store/store'
    import DeleteModal from '@/components/Modal/DeleteModal'
    export default {
        name: "PostPreview",
        components:{
            DeleteModal
        },
        data(){
            return{
                showModal: false
            }
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
    .uk-button-primary {
        position: absolute;
        top: 0;
        left: 26px;
    }
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