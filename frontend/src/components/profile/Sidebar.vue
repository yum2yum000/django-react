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
                    <router-link to="/">
                        ویرایش پروفایل
                    </router-link>
                  </div>
                    <div class=" half col-6">
                        <router-link to="/">
                           تغییر رمز عبور
                        </router-link>
                    </div>
                </div>
            </div>

            <div class="dashCard menu">
                <ul>
                    <li class="showmenu2 active">
                        <i class="lnr lnr-menu header-icons"></i>     منوی حساب کاربری
                      </li>
                    <div class="menu2" style="display: block;">
                        <li>
                            <a href="https://hotlymall.com/panel">
                                <i class="lnr lnr-home header-icons"></i>
                         داشبورد
                          </a></li>

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
        computed:{
            ...mapGetters('login', ['username'])
        }
    }
</script>

<style scoped>

</style>