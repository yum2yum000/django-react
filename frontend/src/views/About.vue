<template>
    <div>
        <div class="bg fill bg-fill  bg-loaded">
            <h1 class="entry-title">
                <strong>درباره ما</strong>
            </h1>
        </div>
        <div class="container">
            <div class="row">
                <div class="col-lg-6 mt-5 text-right">
                    <br><br><br>
                    دیجیتال مارکتینگ روشی نوین در تبلیغات روز دنیا می باشد این روش شامل بازاریابی از طریق محتوا , ایمیل , پاپ آپ , شبکه های اجتماعی و تبلیغات بنری و هر نوع تبلیغی که در بستر اینترنت باشد را شامل میشود از مزایای این نوع تبلیغ قیمت مناسب و بازدهی فوق العاده زیاد آن می باشد
                    <br>
                    <br>
                    <br>
                    تیم ما با چندین سال تجربه طراحی سایت، همیشه تلاش کرده است تا رضایت مشتریان را جلب کند و تعهدات نسبت به نیازها خواسته شده را به نحو احسن انجام دهد.
                    <br><br>
                    هدف ما رونق کسب‌وکار شماست.
                </div>
                <div class="col-lg-6 mt-5">
                    <div class="aboutSectionPicture">
                   <p> <img src="@/assets/images/it.jpg" alt=""></p>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
    export default {
        name: "About"
    }
</script>

<style scoped>
    .bg-fill{
        background-image:url('../assets/images/head5.jpg');
        height:400px;
        background-size: cover !important;
        background-repeat: no-repeat !important;
        background-position: 50% 50%;
    }
    .entry-title{
        color: white;
        position:absolute;
        top: 30%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    .aboutSectionPicture {
        padding: 40px;
        position: relative;
    }
    .aboutSectionPicture img {
        -webkit-box-shadow: 0 0 20px 0 rgba(0,0,0,.25);
        box-shadow: 0 0 20px 0 rgba(0,0,0,.25);
        border-radius: 10px;
        width: 100%;
    }
</style>