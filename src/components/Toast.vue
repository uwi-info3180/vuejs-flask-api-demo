<script setup>
const props = defineProps(['message'])
</script>

<template>
<div class="toast align-items-center text-bg-primary border-0 bottom-0 start-50 translate-middle-x" role="alert" aria-live="assertive" aria-atomic="true">
  <div class="d-flex">
    <div class="toast-body">
      {{ message }}
    </div>
    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
  </div>
</div>
</template>