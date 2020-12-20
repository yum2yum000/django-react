<template>
    <div>
        <footer>
            <div class="footer">
                <div class="container">
                    <div class="row pdn-top-30">
                        <div class="col-xl-5 col-lg-5 col-md-4 col-sm-12">
                            <div class="Follow text-center mt-2">
                                <h3 class="white mt-2">ما را دنبال کنید</h3>
                            </div>
                            <ul class="location_icon">
                               <li><router-link to="/"><img src="@/assets/images/facebook.png" alt=""></router-link></li>
                               <li><router-link to="/"><img src="@/assets/images/Twitter.png" alt=""></router-link></li>
                               <li><router-link to="/"><img src="@/assets/images/instagram.png" alt=""></router-link></li>
                               <li><router-link to="/"><img src="@/assets/images/linkedin.png" alt=""></router-link></li>
                            </ul>
                        </div>
                        <div class="col-xl-7 col-lg-7 col-md-8 col-sm-12">
                            <div class="Follow mt-4 text-center">
                                <h3>دریافت خبرنامه</h3>
                            </div>
                            <div class="email-container">
                                <input class="Newsletter" placeholder="ایمیل خود را وارد کنید" type="Enter your email">
                                <button class="Subscribe">ارسال</button>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
            <div class="copyright">
                <div class="container">
                    <p class="text-center">تمامی حقوق متعلق به ماست </p>
                </div>
            </div>
        </footer>
    </div>
</template>

<script>
    export default {
        name: "Footer"
    }
</script>

<style scoped>

</style>