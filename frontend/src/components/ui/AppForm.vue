<template>
                        <form @submit.prevent="onSubmit">
                           <slot></slot>
                        </form>

</template>

<script>
    export default {

        props:{
            onSubmit:{
                type:Function,
                required:true
            }
        }
    }
</script>

<style scoped>


</style>