<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-bg ftco_navbar  ftco-navbar-light site-navbar-target" id="ftco-navbar">
            <div class="container">
                <button @click="show=!show" class="navbar-toggler js-fh5co-nav-toggle fh5co-nav-toggle" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="oi oi-menu"></span> فهرست
                </button>
                <router-link :to="{name:'register'}" :class="{order:!show}" class="navbar-brand">
                    <img src="@/assets/images/top-icon.png" alt="">
                </router-link>
                <div :class="{collapse:!show}" class=" navbar-collapse text-right" id="ftco-nav" >
                    <ul class="navbar-nav nav ml-auto">
                        <li class="nav-item ml-3"><router-link to="/" class="nav-link active">خانه</router-link></li>
                        <li class="nav-item ml-3"><router-link to="/" class="nav-link active">درباره ما</router-link></li>
                        <li class="nav-item ml-3"><router-link to="/" class="nav-link active">بلاگ</router-link></li>
                        <li class="nav-item ml-3"><router-link to="/" class="nav-link active">تماس با ما</router-link></li>


                    </ul>
                </div>

            </div>
        </nav>
    </div>
</template>

<script>
    export default {
        name: "Navbar",
        data(){
            return{
                show:false
            }
        }
    }
</script>

<style scoped>
.order{
    order:2!important;
}
    .navbar-bg{
        background: rgba(0,0,0,0.4);
        color:white!important;
    }
    .nav-item a{
        color:white!important;
    }
    .navbar{
        position:absolute;
        width:100%;
    }
</style>