<template>
    <v-container>
      <!-- Modal (v-dialog) -->
       <v-dialog v-model="props.modalOpen">
        <v-card>
          <v-card-title class="headline">Create User</v-card-title>
  
          <!-- Modal content with form -->
          <v-card-text>
            <v-form v-model="valid" @submit.prevent="submitForm">
              <v-text-field
                v-model="form.username"
                label="Username"
                required
              ></v-text-field>
  
              <v-text-field
                v-model="form.password"
                label="Password"
                type="password"
                required
              ></v-text-field>


              <v-switch
                v-model="form.is_user_manager"
                label="Is User Manager"
                class="mt-4"
              ></v-switch>
              <v-switch
                v-model="form.is_user_admin"
                label="Is User Admin"
                class="mt-4"
              ></v-switch>
              <v-switch
                v-model="form.is_user_tester"
                label="Is User Tester"
                class="mt-4"
              ></v-switch>
  
              <v-switch
                v-model="form.active"
                label="Is Active"
                class="mt-4"
              ></v-switch>
            </v-form>
          </v-card-text>
  
          <!-- Modal actions (buttons) -->
          <v-card-actions>
            <v-btn color="blue darken-1" @click="handleClose">Cancel</v-btn>
            <v-btn color="green darken-1" @click="submitForm" :disabled="!valid">Create</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  const emit = defineEmits(['close', 'error'])
  

  const handleClose = ()=>{
    emit("close")
  }
  
  
  // Form model
  const form = ref({
    username: '',
    password: '',
    active: false,
    is_user_manager: false,
    is_user_admin: false,
    is_user_tester: false,
    created_at: ''
  });

  
  // Validity check for form
  const valid = ref(false);
  
  
  // Submit form
  const submitForm = async () => {

    // Add ISO STRING DATE 
    const currentDate = new Date();
    const isoDateString = currentDate.toISOString();

    const formData = new FormData();

    // Append form fields to FormData
    formData.append('username', form.value.username);
    formData.append('password', form.value.password);
    formData.append('created_at', isoDateString);
    formData.append('is_user_manager', form.value.is_user_manager);
    formData.append('is_user_admin', form.value.is_user_admin);
    formData.append('is_user_tester', form.value.is_user_tester);
    formData.append('is_user_active', form.value.active);
    // Wait for response from backend
    response = await fetch('http://127.0.0.1:5000/users/create', {
      method: 'POST', 

      body: formData, 
    })

    if(repsonse.status_code === 200){
      emit("close")
    } else {
      console.log(response)
    }
    
    // You can perform your form submission here, like an API call
  };

const props = defineProps({
  modalOpen: {
    type: Boolean, 
    required: true
  }
});
  </script>
  
  <style scoped>
  /* Add any custom styles for your modal if needed */
  </style>
  