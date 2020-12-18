<template>
    <div >
        <Navbar></Navbar>
        <div class="bg-slider">

        </div>
        <br><br>
        <Footer></Footer>
    </div>
</template>

<script>
    import Navbar from '@/components/Navbar'
    import Footer from '@/components/Footer'
    export default {
        name: "Home",
        components:{Navbar,Footer}
    }
</script>

<style scoped>
.bg-slider{
    background-image:url('../assets/images/banner.jpg');
    height:700px;
}
</style>