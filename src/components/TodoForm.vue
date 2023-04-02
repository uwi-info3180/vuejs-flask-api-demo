<script setup>
import { ref } from 'vue';

const props = defineProps(['todos'])
const emits = defineEmits(['add-item'])

let todo = ref("")

const addTodo = () => {
    const form = document.querySelector("#todoForm");
    let formData = new FormData(form);

    fetch('/api/v1/todos', {
        method: 'POST',
        body: formData,
    })
    .then((resp) => resp.json())
    .then((data) => {
        console.log(data);
        // todos.value = data.todos;
        emits('add-item', data.todos)

    })
    .catch((err) => console.log(err));
};
</script>

<template>
<form @submit.prevent="addTodo" id="todoForm">
    <div class="row">
        <div class="col-md-4">
            <div class="input-group mb-3">
                <input v-model="todo" name="todo" class="form-control" placeholder="Enter an item" />
                <button class="btn btn-primary" type="submit">Add</button>
            </div>
        </div>
    </div>
</form>
</template>