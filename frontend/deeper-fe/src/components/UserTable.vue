<script setup lang="ts">

// Default button
import Button from './PageButton.vue';

// Create user modal 
import CreateUser from './modals /CreateUser.vue';

// Table headers
const headers = [
    { title: 'Username', key: 'username' },
    { title: 'Roles', key: 'roles' },
    { title: 'Timezone', key: 'timezone' },
    { title: 'Is Active?', key: 'active' },
    { title: 'Last Updated At', key: 'last_updated' },
    { title: 'Created At', key: 'created_at' },
    { title: 'Actions', key: 'actions' },
]

// Default items
const items = [
    {
        username: 'No data',
        roles: 'No data',
        timezone: "No data",
        active: "No data",
        last_updated: "No data",
        created_at: "No data",
        actions: null
    }
]


// User data fetch
import { ref, onMounted } from 'vue';

// State variables
const data = ref(items);
const loading = ref(true);
const error = ref(null);

// Async function to fetch data
const fetchData = async () => {
    try {
        /**
         * Fetch user data on local Flask server at /users/getall
         */
        const response = await fetch('http://127.0.0.1:5000/users/getall');

        // Check if the response is OK
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Parse the JSON data
        const rawData = await response.json();

        // Convert some data
        for (const user of rawData) {
            let date = new Date(user["created_at"] * 1000);

            user["created_at"] = date.toLocaleDateString();

        }

        data.value = rawData

    } catch (err) {
        error.value = err.message; // Set error message if fetch fails
    } finally {
        loading.value = false; // Set loading to false after fetch attempt
    }
};

// Fetch data when the component is mounted
onMounted(() => {
    fetchData();
});

const modalOpen = ref(false)

// Handle open modal
const handleCreateUser = ()=>{
    modalOpen.value = true
}
const handleClose = ()=>{
    modalOpen.value = false
}

</script>

<template>
    <v-container>
        <v-card color="primary" min-height="65vh" width="100%">
            <!-- Display loading state -->
            <v-card v-if="loading">
                <v-card-title>Loading...</v-card-title>
            </v-card>

            <!-- Display error state -->
            <v-card v-if="error">
                <v-card-title>Error getting user data</v-card-title>
                <v-card-text>{{ error }}</v-card-text>
            </v-card>

            <!-- Display table when data fetched-->
            <v-data-table v-if="data" fixed-header height="50vh" :items="data" :headers="headers">
                <!-- Table rows template -->
                <template v-slot:item="{ item }">
                    <tr>
                        <td>
                            <RouterLink :to="'/user'">
                                {{ item.username }}
                            </RouterLink>
                        </td>
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
                        <td>
                            <Button title="Delete">

                            </Button>
                            <Button title="Edit">

                            </Button>
                        </td>
                    </tr>
                </template>

            </v-data-table>
        </v-card>
    </v-container>
    <v-container class="d-flex justify-center align-center">
        <Button title="Create" :onClick="handleCreateUser"></Button>
    </v-container>
    <v-container v-if="modalOpen">
        <CreateUser :modalOpen="modalOpen" @close="handleClose"/>
    </v-container>
</template>
