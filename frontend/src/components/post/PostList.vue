<template>
    <div class="container">
        <div class="row">
            <PostPreview v-for="post in posts"
                         :key="post.id" :title="post.title" :content="post.content" :id="post.id.toString()" class="col-lg-4 mt-2"></PostPreview>

        </div>
    </div>
</template>

<script>
    import PostPreview from '@/components/post/PostPreview'
    export default {
        name: "PostList",
        props:{
         posts:{
             type:Array,
             required: true
         }
        },
        components: {
            PostPreview
        },
    }
</script>

<style scoped>

</style>