<template>
    <div class="col-md-12">
        <div class="hasshadow"><div>
            <div class="shadowhead">
                ویرایش پست
            </div>
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
    export default {
        name: "PostCreate",
        validations:{
            post:{
                title: { required},
                content: { required}

            }
        },
        created(){
            store.dispatch('login/getPost',
                this.$route.params.id
            ).then((res)=>{
                console.log('44444444444',res)
                this.post.title=res.title
                this.post.content=res.content
                this.post.id=res.id
                console.log('user',this.post)
            })
        },
        data(){
            return{
                post:{
                    title:'',
                    content:''
                },
                error:'',
                buttonClick:false
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
            update(){
                this.$v.$touch()
                if(!this.$v.$invalid){
                this.buttonClick=true;
                    store.dispatch('login/editPost',this.post).then((res)=>{
                   console.log(res)

                    }).catch((e)=>{
                        console.log(e.response)
                    })
                }


            }
        }
    }
</script>

<style scoped>

</style>