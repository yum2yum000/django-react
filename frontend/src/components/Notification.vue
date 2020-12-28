<template>
    <div>
        <div class="alert alert-error" v-if="!confirmShow && show && loggedIn && confirmDay>=0" >
            <p>لطفا ایمیل خود را تایید نمایید   <span>(زمان باقی مانده  {{confirmDay}}روز)</span></p>
             <button @click="show=false" class="close">&times;</button>
        </div>
    </div>
</template>

<script>
    export default {
        inheritAttrs:false,
        props:{
         confirmShow:{
             type:Boolean,
             required:true
         },
            confirmDay:{
                type:Number,
                required:true,
            },
            loggedIn:{
                type:Boolean,
                required:true,
            }
        },
        data(){
          return{
             show:true
          }
        },
        name: "notification",
        methods:{

        }
    }
</script>

<style scoped>
    .alert p{
        top: 0;
        text-align: right;
        position: absolute;
        font-size: 18px;
    }
    .alert-error {
        background-color: #e9e9e9;
    }
    .alert {
        position: fixed;
        top:62px;
        border-radius:0!important;
        height:2px;
        box-sizing: border-box;
        color: #212529;;
        font-size: 1.5em;
        margin: 0 auto;
        margin-bottom: 1em;
        width: 100%;
        z-index:999;
    }
    .alert button{
        position:absolute;
        top:-3px;
    }
</style>