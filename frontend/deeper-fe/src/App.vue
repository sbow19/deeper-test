<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <v-container elevation width="95%">
      <v-card color="primary" tonal>
        <v-container>
          <v-card-title>
            <span class="headline">Deeper Systems Users Management System</span>
          </v-card-title>
        </v-container>

      </v-card>
    </v-container>
  </header>

  <RouterView />
</template>

<style scoped></style>
