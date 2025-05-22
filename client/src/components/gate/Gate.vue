<template>
    <div id="page">
        <div id="container">
            <div id="gate">
                <Door
                    @entered="handle_entered"
                    @forgot="forgot"
                    v-if="form === FORMS.DOOR"
                />

                <Register
                    @registered="handle_registered"
                    v-else-if="form === FORMS.REGISTER"
                />

                <Forgot
                    @navigate_to_door="handle_navigate_to_door"
                    v-else-if="form === FORMS.FORGOT"
                />

                <span @click="handle_form_switch" class="navigate">{{ message }}</span>
            </div>

            <div id="marketing">

            </div>
        </div>
    </div>
</template>

<style>
#page {
    background-color: #fafafa;
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}

#container {
    position: relative;
    height: 350px;
    width: 700px;
    background: white;
    border: 1px solid #f1f1f1;
    border-radius: 5px;
    display: flex;
}

#gate {
    padding: 16px;
    display: flex;
    flex-direction: column;
}
 
#form {
    display: flex;
    flex-direction: column;
    height: 100%;
}

#form .block {
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
}

#form .block .title {
    margin-bottom: 5px;
}

#form input {
    padding: 8px;
    border: 1px solid #ebebeb;
    color: rgb(70, 70, 70);
    border-radius: 5px;
}

#form input::placeholder {
    color: #9e9e9e;
}

#form button {
    cursor: pointer;
    padding: 8px;
    border: 1px solid #ebebeb;
    background-color: #212121;
    color: #E0E0E0;
    border-radius: 5px;
}

.navigate {
    font-size: 0.9rem;
    cursor: pointer;
}

#marketing {
    height: 100%;
    width: 100%;
}
</style>

<script setup>
    import { ref, computed } from 'vue';

    import Door from './forms/Door.vue';
    import Register from './forms/Register.vue';
    import Forgot from './forms/Forgot.vue';

    const FORMS = {
        DOOR: 'door',
        REGISTER: 'register',
        FORGOT: 'forgot'
    };

    const form = ref(FORMS.DOOR);

    const get_message = (form) => {
        if(form === FORMS.REGISTER) {
            return 'Have an account? Enter here.'
        }

        if(form === FORMS.DOOR) {
            return 'Need an account? Register here.'
        }
    };

    const message = computed(() => get_message(form.value));

    const handle_form_switch = () => {
        switch (form.value) {
            case FORMS.DOOR: {
                form.value = FORMS.REGISTER;

                break;
            }
            case FORMS.REGISTER: {
                form.value = FORMS.DOOR;

                break;
            }
            default: {
                form.value = FORMS.DOOR;

                break;
            }
        }
    };

    const handle_registered = (data) => {
        // console.log("DEBUG::enter::handle_registered::this", this);
        // console.log("DEBUG::enter::handle_registered::data", data);
        // console.log("DEBUG::enter::handle_registered::document.cookies", document.cookies);
    };

    const handle_entered = (data) => {
        // console.log("DEBUG::enter::handle_entered::this", this);
        // console.log("DEBUG::enter::handle_entered::data", data);
        // console.log("DEBUG::enter::handle_entered::document.cookies", document.cookies);
    };

    const handle_navigate_to_door = () => {
        form.value = FORMS.DOOR;
    }

    const forgot = () => {
        form.value = FORMS.FORGOT;
    };
</script>
