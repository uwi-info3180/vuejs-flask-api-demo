<template>
    <div id="sidebar" class="d-flex flex-column flex-shrink-0 p-3 text-bg-dark" style="width: 280px;">
        <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none">
            <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="24" height="24" />
            <span class="fs-4 ml-3">VueJS & Flask API</span>
        </a>
        <hr>
        <ul class="nav nav-pills flex-column mb-auto">
            <li class="nav-item">
                <RouterLink to="/" class="nav-link active" aria-current="page">
                    <i class="bi bi-house-door-fill"></i>
                Home
                </RouterLink>
            </li>
            <li>
                <RouterLink to="/about" class="nav-link text-white">
                    <i class="bi bi-info-circle-fill"></i>
                About
                </RouterLink>
            </li>
            <li>
                <RouterLink to="/todos" class="nav-link text-white">
                    <i class="bi bi-list-task"></i>
                Todos
                </RouterLink>
            </li>
            <li>
                <RouterLink to="/articles" class="nav-link text-white">
                    <i class="bi bi-newspaper"></i>
                Articles
                </RouterLink>
            </li>
        </ul>
        <hr>
        <button class="btn btn-success" @click="generateToken">
            <i class="bi bi-key-fill"></i>
            Generate JWT Token
        </button>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { RouterLink } from "vue-router";

const emits = defineEmits(['show-modal'])

let token = ref("");

onMounted(() => {
    token.value = localStorage.getItem('token');
});

function generateToken() {
    console.log('token is being generated')
    fetch('/api/v1/generate-token')
    .then(resp => resp.json())
    .then(data => {
        token.value = data.token;
        localStorage.setItem('token', data.token)
        emits('show-modal', { message: "Token Successfully Generated!", token: token.value});
    })
    .catch(err => {
        console.log(err)
        emits('show-modal', "Token Generation failed!");
    })
}
</script>

<style>
#sidebar {
    height: 100vh;
}
</style>