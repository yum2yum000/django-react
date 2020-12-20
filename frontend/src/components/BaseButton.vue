<template>
    <div>
        <button :class="buttonClass" v-on="$listeners"  v-bind="$attrs"><slot></slot></button>
    </div>
</template>

<script>
    export default {
        inheritAttrs:false,
        props:{
          buttonClass:{
              type:String,

          }
        },
        name: "BaseButton",
        methods:{

        }
    }
</script>

<style scoped>

</style>