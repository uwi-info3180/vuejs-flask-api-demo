<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
let article = ref({});
let loading = ref(false);

onMounted(() => {
    loading.value = true;

    fetch(`/api/v1/articles/${route.params.id}`)
        .then((resp) => resp.json())
        .then((data) => {
            article.value = data.data;
            loading.value = false;
        })
        .catch((err) => {
            console.log(err)
            loading.value = false;
        })
});
</script>

<template>
    <main class="container py-5">
        <h1 class="display-3">{{ article.title }}</h1>
        <p class="text-muted">Posted on {{ article.created_on }}</p>
        <div class="photo my-3">
            <img :src="article.photo" class="img-fluid" width="400" />
        </div>
        <p>{{ article.body }}</p>
        <RouterLink to="/articles" class="btn btn-sm btn-primary"><i class="bi bi-chevron-left"></i> Return to Articles</RouterLink>
    </main>
</template>

<style>
.photo {
    background: #f0f0f0;
    display: flex;
    justify-content: center;
}

img {
    object-fit: cover;
}
</style>