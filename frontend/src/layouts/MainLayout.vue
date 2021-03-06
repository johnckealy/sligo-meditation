<template>
  <q-layout view="lHh Lpr lFf">
    <q-header reveal elevated>
      <q-toolbar class="justify-between glossy q-pa-md">
        <q-btn
          flat
          dense
          icon="chevron_right"
          aria-label="Menu"
          v-if="!drawerOpen"
          @click="drawerOpen = !drawerOpen"
        >
          More
        </q-btn>

        <div class="row inline">
          <q-toolbar-title> Sligo Meditation </q-toolbar-title>
          <img
            alt="icon of person meditating"
            style="width: 30px; height: 30px"
            src="~assets/meditating-white.png"
          />
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="drawerOpen" bordered side="left">
      <div style="max-width: 350px">
        <q-toolbar class="bg-primary text-white shadow-2">
          <q-toolbar-title class="row justify-end">
            <q-btn
              icon="chevron_left"
              aria-label="drawer menu"
              @click="drawerOpen = !drawerOpen"
            ></q-btn>
          </q-toolbar-title>
        </q-toolbar>

        <q-list
          class="items-center content-start q-my-sm text-h6 text-weight-regular"
          bordered
        >
          <q-item class="items-center" clickable v-ripple>
            <q-icon
              size="25px"
              class="q-pa-sm"
              name="self_improvement"
            ></q-icon>
            About
          </q-item>
          <q-item class="items-center" clickable v-ripple>
            <q-icon size="25px" class="q-pa-sm" name="coffee"></q-icon>
            Something else
          </q-item>
        </q-list>
      </div>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <div class="q-py-lg"></div>

    <div class="row bg-secondary items-end">
      <div class="text-center col-md-6 col-12">
        <contact-form />
      </div>
      <div class="text-center col-md-6 col-12">
        <h6>2021 | Ted Kelly</h6>
      </div>
    </div>
  </q-layout>
</template>

<script>
import ContactForm from "../components/ContactForm.vue";
export default {
  components: { ContactForm },
  name: "MainLayout",
  data: () => ({
    drawerOpen: false,
  }),
  mounted() {
    this.$q.notify.setDefaults({
      color: "green-4",
      textColor: "white",
      icon: "cloud_done",
      message: "Successful",
      position: "bottom",
      timeout: 6000,
      actions: [{ icon: "close", color: "white" }],
    });
  },
  meta: {
    title: "Sligo Meditation",
    titleTemplate: (title) => `${title} - Home`,
    meta: {
      description: {
        name: "description",
        content:
          "Sligo meditation, meditations sessions based in Rosses Point and Co. Sligo",
      },
      keywords: { name: "keywords", content: "Sligo Meditation" },
      equiv: {
        "http-equiv": "Content-Type",
        content: "text/html; charset=UTF-8",
      },
      ogTitle: {
        name: "og:title",
        template(ogTitle) {
          return `${ogTitle} - Sligo Meditation`;
        },
      },
    },
    noscript: {
      default: "This is content for browsers with no JS (or disabled JS)",
    },
  },
};
</script>
