<script setup>
import { ref } from "vue";
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
import AppSidebar from "@/components/AppSidebar.vue";
import Modal from "@/components/Modal.vue";

let modalMessage = ref("");
let token = ref("");

function showModal(e) {
  console.log("show modal");

  const modal = document.querySelector('#exampleModal');
  const myModal = bootstrap.Modal.getOrCreateInstance(modal);
  modalMessage.value = e.message;
  token.value = e.token;
  myModal.show();
}
</script>

<template>
  <div class="d-flex flex-nowrap">
    <AppSidebar @show-modal="showModal" />
    <div class="container-fluid">
      <AppHeader />
      <RouterView />
      <Modal :message="modalMessage" :token="token" />
      <AppFooter />
    </div>
  </div>
</template>

<style scoped>

</style>
