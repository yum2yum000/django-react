<template>
    <div class="pageaside">
        <div class="sticky">
            <div class="dashCard">
                <ul>
                    <li class="first-card">
                        <div class="c-profile__user-avatar" style="display: inline-grid;">
                            <img src="https://hotlymall.com/storage/avatars/default.jpg" alt="09118012388">
                        </div>
                        <p class="firstname d-inline-block">{{username}}</p></li>
                </ul>
                <div class="row">
                    <div class=" half col-6">
                    <router-link :to="{name:'profileEdit'}">
                        ویرایش پروفایل
                    </router-link>
                  </div>
                    <div class=" half col-6">
                        <router-link :to="{name:'profileChangepassword'}">
                           تغییر رمز عبور
                        </router-link>
                    </div>
                </div>
            </div>

            <div class="dashCard menu">
                <ul>
                    <li @click="meh" class="showmenu2 active" >
                            منوی حساب کاربری
                      </li>
                    <div class="menu" v-show="show">
                        <li>
                            <router-link :to="{name:'postCreate'}">
                         ایجاد پست
                            </router-link>
                        </li>

                    </div>
                </ul>

            </div>
        </div>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex'
    export default {
        name: "Sidebar",
        data(){
            return{
                show:true
            }
        },
        methods:{
            meh(){
                this.show=!this.show
                console.log(this.show)
            }
        },
        computed:{
            ...mapGetters('login', ['username'])
        }
    }
</script>

<style scoped>

</style>