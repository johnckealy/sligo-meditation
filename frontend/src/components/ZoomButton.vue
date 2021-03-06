<template>
  <div>
    <a :href="zoomLink || null" target="_blank">
      <img alt="zoom icon" style="width: 40px; height: 40px" src="~assets/zoom-icon.png"  />
      <q-tooltip>
        <span class="text-body1"> {{ tooltipText }} </span>
      </q-tooltip>
    </a>
  </div>
</template>

<script>
export default {
  props: ["isPast", 'zoomLink'],
  computed: {
    tooltipText() {
      if (this.isPast) {
        return "This session has finished";
      } else if (!this.zoomLink) {
        return "This sesssion hasn't started yet";
      } else {
        return "Click to enter this Zoom session";
      }
    },
  },
};
</script>

<style>
</style>