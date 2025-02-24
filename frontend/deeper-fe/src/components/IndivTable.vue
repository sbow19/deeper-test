<script setup lang="ts">

// Default button
import Button from './PageButton.vue';

// Table headers
const headers = [
    { title: 'Username', key: 'username' },
    { title: 'Roles', key: 'roles' },
    { title: 'Timezone', key: 'timezone' },
    { title: 'Is Active?', key: 'active' },
    { title: 'Last Updated At', key: 'last_updated' },
    { title: 'Created At', key: 'created_at' },
]

// User data fetch
import { ref } from 'vue';
const props = defineProps({
  data: {
    type: Object, 
    required: true
  }
});

const data = ref(props.data);

</script>

<template>
    <v-container>
        <v-card color="primary" min-height="65vh" width="100%">
            <!-- Display table when data fetched-->
            <v-data-table v-if="data" fixed-header height="50vh" :items="data" :headers="headers">
                <!-- Table rows template -->
                <template v-slot:item="{ item }">
                    <tr>
                        <td>{{ item.username }}</td>
                        <td>
                            <ul>
                                <li v-for="role in item.roles.filter(role => role !== '')" :key="role">
                                    {{ role }}
                                </li>
                            </ul>
                        </td>
                        <td>{{ item.preferences.timezone }}</td>
                        <td>{{ item.active }}</td>
                        <td>{{ item.last_updated }}</td>
                        <td>{{ item.created_at }}</td>
                    </tr>
                </template>

            </v-data-table>
            
        </v-card>

        <v-container class="d-flex justify-space-between align-center">
            <RouterLink :to="'/'">
            <Button title="Back">
                

            </Button>
            </RouterLink>
            <Button title="Edit">

            </Button>
            <Button title="Delete">

            </Button>
            
        </v-container>


    </v-container>
</template>
