<script setup>
import { ref, onMounted } from 'vue'
import TodoForm from "@/components/TodoForm.vue";

let todos = ref([])

onMounted(() => {
    fetch('/api/v1/todos')
    .then((resp) => resp.json())
    .then((data) => {
        todos.value = data.todos;
    })
    .catch((err) => console.log(err));
})

const update = (e) => {
    todos.value = e;
};
</script>

<template>
    <main class="container py-5">
        <h1 class="display-1 mb-3">Todos</h1>
        <TodoForm :todos="todos" @add-item="update" />
        <ul>
            <li v-for="todo in todos" :key="todo.id">{{ todo.title }}</li>
        </ul>
    </main>
</template>
