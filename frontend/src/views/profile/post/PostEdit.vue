<template>
    <div class="col-md-12">
        <div class="hasshadow"><div>
            <div class="shadowhead">
                ویرایش پست
            </div>
            <loading loader="dots" :active.sync="isLoading"
                     :can-cancel="true"></loading>
            <div class="row justify-content-center mt-5">
                <div class="col-lg-12">
                    <form @submit.prevent="update">
                        <div class="row">
                            <div class="col-lg-6">
                                <div class="input-container">
                                    <BaseInput type="text" inputClass="input--style-4" label="عنوان" v-model="post.title"  @blur="$v.post.title.$touch()" ></BaseInput>
                                    <div v-if="$v.post.title.$error">
                                        <p class="text-right error" v-if="!$v.post.title.required"> عنوان باید وارد شود</p>
                                </div>
                                </div>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-lg-6">
                                <div class="input-container">
                                    <label class="label">متن</label>
                                    <textarea v-model="post.content"  @blur="$v.post.content.$touch()" class="textarea--style-4" type="text" ></textarea>
                                    <div v-if="$v.post.content.$error">
                                        <p class="text-right error" v-if="!$v.post.content.required"> متن باید وارد شود</p>
                                    </div>
                                </div>
                            </div>

                        </div>

                        <div v-if="error" class="text-right error mt-2 mr-3">
                            {{error}}
                        </div>
                        <div class="p-t-15 text-center ">
                            <BaseButton buttonClass="btn btn--radius-2 submit" type="submit" :disabled="$v.$anyError || buttonClick" >ایجاد</BaseButton>
                        </div>

                    </form>
                </div>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
    import { required} from 'vuelidate/lib/validators'
    import store from '@/store/store'
    import {mapGetters} from 'vuex'
    export default {
        name: "PostEdit",
        validations:{
            post:{
                title: { required},
                content: { required}

            }
        },
        created(){
            if(!this.userInfo){
                store.dispatch('login/getUser')
            }
            this.isLoading=true;
            store.dispatch('post/getPost',
                this.$route.params.id
            ).then((res)=>{
                this.post.title=res.title
                this.post.content=res.content
                this.post.id=res.id
                this.isLoading=false;
                console.log('user',this.post)
            }).catch(()=>{
                this.isLoading=false;
            })
        },
        data(){
            return{
                post:{
                    title:'',
                    content:''
                },
                error:'',
                buttonClick:false,
                isLoading:false,
            }
        },
        watch:{
            post: {
                handler() {
                    this.error=''
                },
                deep: true
            },
        },
        computed: {
            ...mapGetters('login', ['userInfo'])
        },
        methods:{
            update(){
                this.$v.$touch()
                if(!this.$v.$invalid){
                this.buttonClick=true;
                    this.isLoading=true;
                    store.dispatch('post/editPost',this.post).then((res)=>{
                        this.buttonClick=false;
                        this.isLoading=false;
                        if (res.status === 200){
                            this.error='پست با موفقیت ویرایش شد'
                        }

                    }).catch((e)=>{
                        this.isLoading=false;
                        console.log('g',e.response)
                    })
                }


            }
        }
    }
</script>

<style scoped>

</style>