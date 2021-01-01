<template>
    <div class="col-md-12">
        <div class="hasshadow"><div>
            <div class="shadowhead">
                ایجاد پست
            </div>
            <loading loader="dots" :active.sync="isLoading"
                     :can-cancel="true"></loading>
            <div class="row justify-content-center mt-5">
                <div class="col-lg-12">
                    <form @submit.prevent="create">
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
    import Service from '@/services/Service.js'
    import {mapGetters} from 'vuex'
    import store from '@/store/store'
    export default {
        name: "PostCreate",
        validations:{
            post:{
                title: { required},
                content: { required}

            }
        },
        computed: {
            ...mapGetters('login', ['userInfo'])
        },
        created(){
            if(!this.userInfo){
                store.dispatch('login/getUser')
            }
        },
        data(){
            return{
                post:{},
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
        methods:{
            create(){
                this.$v.$touch()
                if(!this.$v.$invalid){
                this.buttonClick=true;
                    this.isLoading=true,
                Service.createPost(this.post).then((res)=>{
                    console.log('created post',res)
                    this.isLoading=false,
                    this.buttonClick=false;
                    if (res.status === 201){
                        this.error='پست با موفقیت ایجاد شد'
                    }
                }).catch((e)=>{
                    this.buttonClick=false;
                    this.isLoading=false,
                    console.log(e.response)
                    if (e.response && e.response.status === 400) {

                        if(e.response.data.post)
                        {
                            this.error='لطفا ورودی ها خود را کنترل کنید'
                        }


                    }
                })
            }
            }
        }
    }
</script>

<style scoped>

</style>