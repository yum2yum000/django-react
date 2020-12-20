export const formFieldMixin={
    props:{
        label:{
            type:String,
            default:''
        },
        value:[String,Number]


    },
    methods:{
        updateValue(b){
            this.$emit('input',b.target.value)
        }
    }

}