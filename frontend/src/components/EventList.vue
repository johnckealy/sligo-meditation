<template>
  <div class="q-pa-sm">
    <q-toolbar class="bg-primary text-white shadow-2">
      <q-toolbar-title v-if="events.length != 0"
        >Upcoming Sessions</q-toolbar-title
      >
      <q-toolbar-title class="" v-else
        >There are no upcoming sessions right now. Check back
        soon!</q-toolbar-title
      >
    </q-toolbar>

    <q-list bordered>
      <q-item
        clickable
        v-for="event in events"
        :key="event.id"
        class="q-my-sm"
        v-ripple
        @click="openDialog(event)"
      >
        <q-item-section avatar>
          <q-icon size="35px" :name="event.icon"></q-icon>
        </q-item-section>

        <q-item-section>
          <q-item-label class="text-body1">{{ event.title }}</q-item-label>
          <q-item-label class="text-body1" caption>{{
            event.start_time
          }}</q-item-label>
        </q-item-section>

        <q-item :disabled="!event.zoom_link">
          <zoom-button :zoomLink="event.zoom_link" :isPast="event.is_past" />
        </q-item>
      </q-item>

      <q-separator />
      <q-item-label header>Past Sessions</q-item-label>

      <q-item v-if="past_events.length == 0">
        There are no past sessions.
      </q-item>

      <q-item
        v-for="past_event in past_events"
        :key="past_event.id"
        class="q-mb-sm"
        clickable
        v-ripple
        @click="openDialog(past_event)"
      >
        <q-item-section avatar>
          <q-icon size="35px" :name="past_event.icon"></q-icon>
        </q-item-section>

        <q-item-section>
          <q-item-label class="text-body1">{{ past_event.title }}</q-item-label>
          <q-item-label class="text-body1" caption>{{
            past_event.start_time
          }}</q-item-label>
        </q-item-section>

        <q-item disabled>
          <zoom-button :zoomLink="null" :isPast="past_event.is_past" />
        </q-item>
      </q-item>
    </q-list>

    <q-dialog v-model="dialog">
      <q-card>
        <q-card-section class="row items-center">
          <span class="text-right q-ml-sm text-subtitle2">
            <q-icon size="20px" class="q-px-xs" name="query_builder"></q-icon>
            {{ dialogData.start_time }}</span
          >
        </q-card-section>

        <q-card-section class="row items-center">
          <q-icon size="35px" :name="dialogData.icon"></q-icon>
          <span class="q-ml-sm text-h6">{{ dialogData.title }}</span>
        </q-card-section>

        <q-card-section class="row items-center">
          <span class="q-ml-sm text-subtitle1">{{
            dialogData.description
          }}</span>
        </q-card-section>

        <q-card-section v-if="!dialogData.is_past && dialogData.zoom_link"
          >Click the Zoom button below to enter the session</q-card-section
        >

        <q-card-actions
          :disabled="dialogData.is_past || !dialogData.zoom_link"
          class="justify-center"
        >
          <zoom-button
            :zoomLink="dialogData.zoom_link"
            :isPast="dialogData.is_past"
          />
        </q-card-actions>
        <q-btn no-caps flat label="Close" color="primary" v-close-popup />
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import ZoomButton from "./ZoomButton.vue";
export default {
  components: { ZoomButton },
  data() {
    return {
      events: [],
      past_events: [],
      dialog: false,
      dialogData: {},
    };
  },
  mounted() {
    this.getEvents();
  },
  methods: {
    openDialog(event) {
      this.dialogData.title = event.title;
      this.dialogData.start_time = event.start_time;
      this.dialogData.description = event.description;
      this.dialogData.icon = event.icon;
      this.dialogData.zoom_link = event.zoom_link;
      this.dialogData.is_past = event.is_past;
      this.dialog = true;
    },
    async getEvents() {
      const response = await this.$axios.get("/events/");
      this.events = response.data.filter((event) => {
        return !event.is_past;
      });
      this.past_events = response.data.filter((event) => {
        return event.is_past;
      });
    },
  },
};
</script>

<style>
</style>