<template>
  <div class="row justify-end">
    <div class="col-md-6 col q-ma-lg">
      <q-toolbar-title>Contact Me</q-toolbar-title>
      <q-form @submit="onSubmit">
        <q-input
          class="q-my-sm bg-white"
          outlined
          hide-bottom-space
          v-model="contactFormEmail"
          placeholder="Enter your E-mail Addess..."
          lazy-rules="ondemand"
          :rules="[
            (val) =>
              (val && val.length > 0) || 'Please include your email address',
            (v) => /.+@.+\..+/.test(v) || 'The email you entered is not a valid address',
          ]"
        />
        <q-input
          class="q-my-sm bg-white"
          outlined
          hide-bottom-space
          v-model="contactFormBody"
          placeholder="Write your message here..."
          type="textarea"
          lazy-rules="ondemand"
          :rules="[
            (val) => (val && val.length > 0) || 'Please provide a message',
          ]"
        />
        <q-btn
          :label="loading ? 'Submitting...' : 'Submit'"
          class="full-width"
          type="submit"
          color="primary"
        />
      </q-form>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    contactFormEmail: "",
    contactFormBody: "",
    loading: false,
  }),
  methods: {
    async onSubmit() {
      this.loading = true;
      try {
        const response = await this.$axios.post("/contact_form_details/", {
          email: this.contactFormEmail,
          message: this.contactFormBody,
        });
        this.$q.notify({
          message: "Your message was sent successfully!",
        });
      } catch {
        this.$q.notify({
          color: "red-6",
          icon: "error",
          message:
            "There was a problem sending your message! Please try again.",
        });
      }
      this.contactFormEmail = "";
      this.contactFormBody = "";
      this.loading = false;
    },
  },
};
</script>

<style lang="scss">
</style>