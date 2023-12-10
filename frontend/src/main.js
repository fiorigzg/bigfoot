import { createApp } from 'vue';
import { createPinia } from 'pinia';
import VueHighlightJS from 'vue3-highlightjs'
import 'highlight.js/styles/mono-blue.css'

import '@/assets/main.css';
import Research from '@/pages/Research.vue';
import Home from '@/pages/Home.vue';


const pinia = createPinia();
const app = createApp(Home);

app.use(pinia);
app.use(VueHighlightJS)
app.mount('#app');  