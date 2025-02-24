<script setup lang="ts">
    import { defineProps } from 'vue';

const props = defineProps({
  title: {
    type: String,
    required: true,
  },
  onClick: {
    type: Function, 
    required: true
  }
});
</script>

<template>
  
  
  <v-btn color="secondary" @click="props.onClick">{{ title }}</v-btn>
</template>