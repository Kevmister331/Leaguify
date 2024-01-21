<script setup>
import { ref } from 'vue';
import Button from 'primevue/button';
import Dropdown from 'primevue/dropdown';
import teemoImage from '@/assets/teemo.jpg';
import items from '@/assets/champions.json'


const message = ref('');
const selectedItem = ref(null); // Ref for the selected item

const showMessage = () => {
    message.value = `Selected Champion: ${selectedItem.value.name}`;
};
</script>

<template>
  <div class="container">
    <h2>Leaguify</h2>
    <Dropdown :options="items" optionLabel="name" v-model="selectedItem" filter>
      <template #item="slotProps">
        <div class="dropdown-item">
          <img v-if="slotProps.option.imageUrl" :src="slotProps.option.imageUrl" class="dropdown-image" />
          <span>{{ slotProps.option.name }}</span>
        </div>
      </template>
    </Dropdown>
    <Button class='button' label="Confirm Selection" @click="showMessage"></Button>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<style scoped>

.button {
  margin: 10px;
}
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding-top: 4rem;
}


</style>
