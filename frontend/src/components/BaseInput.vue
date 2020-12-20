<template>
    <div class="input-group">
        <label v-if="label">{{label}}</label>
        <input :class="$attrs.inputClass" :type="$attrs.type" @input="updateValue" :value="value"  v-on="listeners">
    </div>
</template>

<script>
    import {formFieldMixin} from '@/mixins/formFieldMixin'
    export default {
        inheritAttrs:false,
        mixins:[formFieldMixin],
        name: "BaseInput",

        computed:{
            listeners(){
                return{
                    ...this.$listeners,
                    input:this.updateValue
                }
            }
        },

    }
</script>

<style scoped>

</style>