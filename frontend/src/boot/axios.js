import Vue from 'vue'
import axios from 'axios'

axios.defaults.baseURL = process.env.AXIOS_BASE_URL;

Vue.prototype.$axios = axios
