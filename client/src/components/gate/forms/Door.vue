<template>
    <div id="form">
        <div class="block">
            <span class="title">Email</span>

            <input type="text" v-model="form.email" placeholder="a@b.com" />
        </div>

        <div class="block">
            <span class="title">Password</span>

            <input type="password" v-model="form.password" />
        </div>

        <button type="button" @click="enter">Enter</button>

        <span class="navigate" @click="forgot">Forgot password?</span>
    </div>
</template>

<script setup>
import axios from 'axios';
import { reactive, defineEmits } from 'vue';

const emit = defineEmits([
    'entered',
    'forgot'
]);

const form = reactive({
    email: '', 
    password: ''
});

const forgot = () => {
    emit('forgot');
};

const enter = async () => {
    axios.post(
        "https://api.localhost/api/enter",
        {
            email: form.email,
            password: form.password,
        },
        {
            withCredentials: true,
        }
    ).then((response) => {
        console.log("DEBUG::enter::response.data", response.data);

        emit('entered');
    }).catch((error) => {
        console.log("DEBUG::enter::error", error);
    });
}
</script>
