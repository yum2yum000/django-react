<template>
        <div class="modal" v-show="show">
            <div class="modal-wrapper">
                <div class="modal-container">
                    <content select=".modal-header">
                        <div class="modal-header">
                            <h3>
                                پیغام
                            </h3>
                        </div>
                    </content>
                    <div class="modal-body">
                       آیا برای حذف پست اطمینان دارید؟
                    </div>
                    <div class="modal-footer uk-clearfix">
                        <button @click="deleteItem"  class="btn-modal btn btn-success ml-2">بله</button>
                        <button @click="closeModal"  class="btn-modal btn btn-primary">بستن</button>
                    </div>
                </div>
            </div>
        </div>
</template>

<script>
    export default {
        name: "DeleteModal",
        props: {
            show: {
                type: Boolean,
                required: true,
            }
        },
        methods: {
            closeModal() { //the method to close the modal
                this.$emit('closeModal')
            },
            close() {
                this.$emit('update:dialog', false)
            },
            deleteItem()
            {
                this.$emit('apply')

            }
        }
    }
</script>

<style scoped>
    .modal {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.7);
        display: table;
        transition: opacity 0.3s ease;
    }
    .modal-wrapper {
        display: table-cell;
        vertical-align: middle;
    }
    .modal-container {
        background: #fff;
        width: 450px;
        border-radius: 5px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
        transition: all 0.3s ease;
        margin: 0 auto;
        padding: 20px 30px;
    }
    .modal-footer {
        margin-top: 15px;
    }
    .modal-enter, .modal-leave {
        opacity: 0;
    }
    .modal-enter .modal-container, .modal-leave .modal-container {
        -webkit-transform: scale(1.1);
        transform: scale(1.1);
    }
    .login-btn {
        background: purple;
        color: #1d1d1d;
        cursor: pointer;
        font-size: 2em;
        padding: 1.5rem;
        border: 0;
        transition: all 0.5s;
    }
    .btn-modal{
        padding: 5px 28px!important;
        line-height: 21px!important;
    }
</style>